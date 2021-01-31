# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

An invented word that is the longest word in the english language and means a
lung disease called silicosis that is caused by fine particles such as ash or dust.

## According to its man page, what does `getrusage` do?

The function getrusage is used to examine the resource usage of a process and
returns resource usage measures for who, which in this case is RUSAGE_SELF.

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

If you don't use before and after but instead value, that will take up lots of memory and cause the program to be slow.


## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

first fgetc 'gets' the next character until the end of the file. It is checked to see if the charachter is any symbol other than alphabetical or an apostrofe and if it isn't the character will be added to the word array.
If the next character is a space or a punctuation mark this indicated the end of the word and a \0 is added to the word as termination signal.
The size of the word is checked and if it is too large for the buffer, the word will be skipped.
If the word conatians a number, the word is ignored and skipped.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

fscanf reads a string until a whitespace is found, but some of the words end with a punctuation instead of a whitespace which fscanf will see as part of the word.
This will cause the program to not identify correctly if a word is spelled correctly and may even cause error.
fgetc is unlikely fscanf able to identify a word regardless of the punctuation that might follow and is therefore better suited for speller.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Because the parameters should not be changed throughout running the program.
If the parameters were not defined as constant, they might be changed and since in a spellcheck accuracy is very important, this should be prevented.
