# AirBnB Clone - The Console

## Description

Project 0x00 - AirBnB clone - The console
The first step in the full web application: the AirBnB clone.
Starting with the two major complonents the data models and the storage engine.

## Unit Tests

All unit tests are found in the tests directory

## How to start

Starting the console, which is a command interpreter, you run the executable script "console.py" from the root directory of this repository.

Commands are seperated by line breaks.

## How to use it
There are various commands for the interpreter which you would input when prompted.

### Create

Creates a new instance of the given class and saves it.

* create CLASS

This command prints the ID of the new object, which is a random UUID, which can be used for other commands

### Show

Prints a description of the specified object.

* show CLASS ID

### Destroy

Destroys a specific object

* destroy CLASS ID
* CLASS.destroy(ID)

### All

Prints all objects in storage, or all objects in storage of particular class.

* all [CLASS]
* CLASS.all()

Output looks like a Python list of strings (["object1", "object2" ...])

### Update

Updates one or more attributes on the specified object.

* update CLASS ID NAME
* CLASS.update(ID, NAME)

## Authors

* Victor kipkirui koech
* 
