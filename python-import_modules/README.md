# 0x02. Python - import & modules
## About
An introductory project on:
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs
## Requirements
- python3 (version 3.8.5)
- pep8  2.7.
## File Descriptions
### Mandatory
**[0-add.py](0-add.py)** - imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
  * should not be executed when imported

**[1-calculation.py](1-calculation.py)** - imports functions from the file `calculator_1.py` and uses all of its functions
  * should not be executed when imported

**[2-args.py](2-args.py)** - prints the number of and the list of its arguments.
  * The output should be:
    * Number of argument(s) followed by `argument` or `arguments`, followed by
    * `:` (or `.` if no argument where passed) followed by
    * a new line, followed by (if at least one argument)
    * one argument per line:
      * the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
  * should not be executed when imported

**[3-infinite_add.py](3-infinite_add.py)** - prints the result of the addition of all arguments
  * should not be executed when imported

**[4-hidden_discovery.py](4-hidden_discovery.py)** - prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc)
  * print only names that do not start with `__`
  * should not be executed when imported

**[5-variable_load.py](5-variable_load.py)** - imports the variable `a` from the file `variable_load_5.py` and prints its value.
  * should not be executed when imported

### Advanced
**[100-my_calculator.py](100-my_calculator.py)** - imports all functions from the file calculator_1.py and handles basics operations.
- Usage: `./100-my_calculator.py a operator b`
 - If the number of arguments is not 3, your program has to:
  - print `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line
  - exit with the value `1`
 - `operator` can be:
  - `+` for addition
  - `-` for subtraction
  - `*` for multiplication
  - `/` for division
 - If the operator is not one of the above:
  - print `Unknown operator. Available operators: +, -, * and /` followed with a new line
  - exit with the value `1`
 - You can cast `a` and `b` into integers by using `int()` (you can assume that all arguments will be castable into integers)
 - The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported

**[101-easy_print.py](101-easy_print.py)** - prints #pythoniscool, followed by a new line, in the standard output.
- Your program should be maximum 2 lines long
- You are not allowed to use `print` or `import sys` in your file `101-easy_print.py`


**[103-fast_alphabet.py](103-fast_alphabet.py)** - prints the alphabet in uppercase, followed by a new line.
- Your program should be maximum 3 lines long
- You are not allowed to use:
  - any loops
  - any conditional statements
  - `str.join()`
  - any string literal
  - any system calls