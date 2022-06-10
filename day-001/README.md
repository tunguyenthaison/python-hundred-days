# python-hundred-days

## Day 001: Band name generator

--- 

1. Create a greeting for your program.

2. Ask the user for the city that they grew up in.

3. Ask the user for the name of a pet.

4. Combine the name of their city and pet and show them their band name.

5. Make sure the input cursor shows on a new line, see the example at [replit](https://replit.com/@appbrewery/band-name-generator-end)

---

## Objectives:

* Learn how to use `input` with python, by default 
    ```python
        >>> pet = input("Please enter name: ")
    ```
    return a string without a newline
    ```python
        Please enter a name: abc
        >>> 
    ```
* Learn to `print`  in python without adding a new line to the end of the string 
    ```python
        >>> print("Please enter: ", end='')
    ```
    This returns
    ```python
        Please enter: >>> 'Madison'
        'Madison'
    ```