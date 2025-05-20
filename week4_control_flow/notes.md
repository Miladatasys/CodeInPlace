# Today's route

**Goals**:

* Create a while loop in python
* Create an if/else statement in python
* Construct a boolean expression

### REVIEW: 

Three important things you need to know if you want to work variables:

1. **Create** a new variable
```
age = 37
```
2. **Use** the variable
```
print(f"age is: {age}")
```
3. **Modify** or change the value (right hand side) of the variable
```
age = age + 1
```
### You can use arithmetic operators
- Adittion ``+``
- Substraction ``-``
- Multiplication ``*``
- Division ``/``

Route of Control flow:

1. Review
2. While/If
3. Booleans
4. For loops
5. Mountain (Core Python)

# While/If

```
while front_is_clear():
    body
```
```
if beepers_present():
    body
```
- While Loop Redux:

    - The condition should be a **boolean** which is either True or False

| Operator | Meaning                | Example           | Value |
|----------|------------------------|-------------------|--------|
| `==`     | equals                 | `1 + 1 == 2`      | True   |
| `!=`     | does not equal         | `3.2 != 2.5`      | True   |
| `<`      | less than              | `10 < 5`          | False  |
| `>`      | greater than           | `10 > 5`          | True   |
| `<=`     | less than or equal to  | `126 <= 100`      | False  |
| `>=`     | greater than or equal to | `5.0 >= 5.0`   | True   |

> *All have equal precedence*

## Spot the difference #1

Set's the value of a variable named x to be 7. Creates the variable if it didn't exist.
```
x = 7
```
Checks if a variable named x has the value 7
```
x == 7
```

## Spot the difference #2
Checks if x is the number 5
```
x == 5
```
Checks if x is the string 5
```
x == "5"
```
**You should use the one that's appropiate for the value that's inside x.**

## Comparison Operators
```
num = int(input("Enter a number: "))
if num == 0:
    print("That number is 0")
else: print("That number is not 0")
```
## If Else Revisited
This code is "fine" But could be much better. 
```
num = int(input("Enter a number: "))
if num == 0:
    print("That number is 0")
else:
    if num > 0:
        print("Your number is positive")
    else:
        print("Your number is negative")
```
Here is **how**:
```
num = int(input("Enter a number: "))
if num == 0: # If this condition is false...
    print("That number is 0")
elif num > 0: # Then check if this is true
    print("Your number is positive")
else:
    print("Your number is negative")
```

### Logical Operators
Logical operators are used to combine conditional statements and return Boolean values (`True` or `False`). These operators evaluate expressions based on logic rules and are typically used in control flow and decision-making.

They follow a specific **order of precedence**, which determines the order in which they are evaluated:
1. `not`
2. `and`
3. `or`


| Operator | Example                          | Result |
|----------|----------------------------------|--------|
| `not`    | `not (2 == 3)`                   | True   |
| `and`    | `(2 == 3) and (-1 < 5)`          | False  |
| `or`     | `(2 == 3) or (-1 < 5)`           | True   |


### Boolean Variables

Boolean variables are used to store values that represent **truth values**: `True` or `False`. These are often the result of comparisons or logical conditions and are essential for control flow in programming.

#### Storing Comparison Results

```
# Store expressions that evaluate to True/False
x = 1 < 2         # True
y = 5.0 == 4.0    # False
```
In these examples:
- x is assigned the result of the comparison 1 < 2, which evaluates to ``True``.
- y is assigned the result of the comparison 5.0 == 4.0, which evaluates to False

**Direct Assignment:**
```
# Directly set to True/False
is_sheltering = True
is_raining = False
```
Boolean variables can also be directly assigned with ``True`` or ``False`` values to represent states or conditions.

**Conditional Check with User Input**:
```
play_again = input('Play again? "y" or "n"') == 'y'

if play_again:
    ...
```
**In this example:**

- The input() function asks the user whether they want to play again.

- The result is compared to 'y' — if the user types 'y', play_again is True, otherwise it's False.

- The if play_again: statement then executes the block only if the condition is True.

Tip: Boolean variables help make code more readable and logical, especially in conditions and loops.


# For Loops in Python

Main goal: **Recognize for loops in console programming and also, understand how to use the variable ``i`` or index variable**
```
def main():
    for i in range(100):
        print(f"Python rocks socks! {i}") # I can use the variable i
```
You can use it in:
- arithmetic expressions
- print statements

- Another example: **Generating Even Numbers** that produce the same output:
```
 0
 2
 4
```
```
# Method 1: Multiply i by 2
for i in range(3):      # i = 0, 1, 2
    print(i * 2)        # prints 0, 2, 4
```
```
# Method 2: Use step in range()
for i in range(0, 6, 2):  # start at 0, stop before 6, step by 2
    print(i)              # prints 0, 2, 4
```

**- Multiple lines inside a for loop:**
```
def main():
    for i in range(100):
        print(f"You rock! {i}")
        print("Keep learning")
```

**Key concepts**
- range(start, stop, step) allows fine control:
    - ``start``: where the loop begins (inclusive)

    - ``stop``: where the loop ends (exclusive)

    - ``step``: how much to increment each time (e.g., 2 to skip by twos)

**When to Use These**:

- Want a loop to iterate a fixed number of times? → ``range(n)``

- Want to generate even numbers or any custom step? → ``range(start, stop, step)``

- Want to index into a list or string? → ``for i in range(len(my_list))``

# Live sessions
- Type casting
- Type function it's useful 
- Practice boolean operators 
- 