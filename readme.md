# Random

by import the random module, we can generate random number, select a random element from a collection, or shuffle a collection.

# Exception

exceptions are events that interrupt the normal execution flow, so we need to deal with it by `try` block,  the keyword `else` is used to indicate the code block that will be executed if no exceptions threw.

# I/O

to deal with the file reading and writing, we can import the os module.

If we write a file with a `w` mode, it will overwrite the content, if we want to append content, we should use the `a` mode.

In order to copy, we need to import shutil module, there are three methods for copying:

- copyfile(): copys only the content of the file
- copy(): used mostly, copyfile() + permission mode + destination could be a directory
- copy2(): copy() + copys metadata (file's creation and modification times)

As for deleting, there are three methods used for different occasions:

- os.remove(): used for deleting file
- os.rmdir(): used for deleting empty directory
- shutil.rmtree(): used for deleting non-empty directory

# Modules

A python file containing functions and classes, etc. Used for module programming to separate program into parts.

# Object oriented programming

in Python, we have class variables and instance variables, the differences between them are as follows:

- instant variables: defined in the constructor
- class variables: defined out of the constructor, can be accessed by instance or class, we can modify the class variables for all the instances, but if it's modified through instance, then it'll be independent from class variables, that means it can not be modified through class again.

Python support multiple inheritance, so a child class can inheritance from multiple parent classes.

Method Chain is a pattern used for a sequential method calling, every method return itself.

Super() method can used to access the parent class, by using the pattern, we can transfer some common code between children' classes to the parent class. 