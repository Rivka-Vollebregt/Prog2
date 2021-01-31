/*********************************************************************************
 * dictionary.c
 *
 * Implements a dictionary's functionality
 *
 * Programmeren 2
 *
 * Rivka Vollebregt
 * 12164968
 *
 * dictionary.c is part of the program speller.c which scans every word in a text
 * document and if a word is in the dictionary file that is provided,
 * the word will be checked for correct spelling.
*********************************************************************************/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <ctype.h>

#include "dictionary.h"

// Create struct node
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Create variables
int HASHTABLE_SIZE = 65536;
node *hash_table[65536];
node *start = NULL;
unsigned long words = 0;

// Hash-function source: Anthony Catantan (2017)
// Create hash function
int hash_function(const char *key)
{
    int index = 0;

    // Go through every character of each word
    for (int i = 0; key[i] != '\0'; i++)
    {
        // Change the character to uppercase
        index += toupper(key[i]);
    }

    // Modulo index with hashtable_size to ensure accuracy and limit
    // the index within the size
    return index % HASHTABLE_SIZE;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Set cursor to the start of the correct linked list
    node *cursor = hash_table[hash_function(word)];

    // Go through the list
    while (cursor != NULL)
    {
        // Check if node's word is the target word regardless of case
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }

        cursor = cursor->next;
    }

    // Return false if word is not in dictionary
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open dictionary file and check if succesfull
    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        return false;
    }

    // Create variable word with appropriate length
    char word[LENGTH + 1];

    // Check entire file
    while (fscanf(file, "%s", word) != EOF)
    {
        // Allocate memory for a new node
        node *new_node = malloc(sizeof(node));

        // Check if assigning memory was succesfull
        if (new_node == NULL)
        {
            fclose(file);
            unload();
            return false;
        }

        // Copy word into new node
        strcpy(new_node->word, word);

        // Use hash function put new word in correct linked list (bucket)
        int bucket = hash_function(word);

        // Insert into linked list
        new_node->next = hash_table[bucket];
        hash_table[bucket] = new_node;

        words++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // Return the words counter
    return words;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Go through hash table and free the allocated memory
    for (int i = 0; i < HASHTABLE_SIZE; i++)
    {
        if (hash_table[i] != NULL)
        {
            // Create pointer to iterate over linked list
            node *cursor = hash_table[i];

            // Free the nodes of linked list until end of linked list
            while (cursor != NULL)
            {
                node *tmp = cursor;
                cursor = cursor->next;
                free(tmp);
            }
        }
    }

    return true;
}

