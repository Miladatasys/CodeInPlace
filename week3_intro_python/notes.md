# **Week 3: Intro to Python**

## **Lesson Goals**
1. Write a console program
2. Create Variables
3. Print to screen
4. Get user input

### Welcome to Python
```
"""
File: helloWorld.py
-------------------
This is our first python program. It is customary to have a programmer's first program write "hello world"
(inspire by the first program in Brian Kernighan and 
Dennis Ritchie's classic book, 'The C programming language)
"""
def main():
    print("Hello World!")

if __name__ == '__main__':
    main()
```

- Print + Input

**1. Variables serve to store values:**

    ```
    def main():
        print("Running my program...")
        my_name = "Mila"
        print(f"{my_name}")

    if __name__ == '__main__':
        main()
    ```
    - ``f"{}"`` these brackets will be at the terminal, instead of the words 'my_name' will show the value inside the variable.
    - The way you create variables is creaing a name or descriptive words separated by ``_`` and the ``=`` sign to separate the value`.
    
**2. Input functions:**

    ```
    your_name = input("What is your name? ")
    ```

- The terminal we'll ask the user to insert or write their name and when the human hits enter, the program will continue it will then finish the line showing the input inside the variable. 

**3. One final example:**

This time, instead of having just one variable and one call input, we'll have three. 

    ```
    def main():
        dish = input("Enter a type of food: ")
        person = input("Name a person: ")
        adjective = input("Provide an adjective: ")
        print(f"My favorite meal is {dish}, specially when it's {adjective} and cooked by {person}.")

    if __name__ == '__main__':
        main()
    ```
### **TIP:**

YOU CAN GO BACK IN TIME, USING THE ARROW RIGHT TO **RUN** SAME AS YOU DID WITH KAREL to see the steps ran by the program

## Numbers in Python
**Lesson Goals**
1. Use number variables
2. Change the type of a Variables
3. Use constants

```
def main():
    print("This program adds two numbers.")
    num1 = input("Enter first number: ")
    """
    Here we're taking the value   convert it into a number with int(value)
    """
    num1 = int(num1) 
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total is " + str(total) + ".")


if __name__ == '__main__':
    main()
```
* Here, we're converting the input of the user that is text (even if the user input is for example, 9) to an integer with the ``int`` to be the number equivalent to store it in the variable or ``num1 or num2`` to after the sum store them inside the total variable.
* The equal sign is called asignment. 


* Let's analyze this part, specially the + signs and str:
```
print("The total is " + str(total) + ".")
```
We're trying to create and add strings together. 
-   The **+** operator **concatenates** strings together.
- You can use , to separate things in the print statement, what will happend is that they'll be treated as spaces.

1. ``print`` is a function or command that says: print out all the text in between the two quotes (can be single quotes or double) to the terminal.
    - There is a time when you're constrained to use single vs the double quotes and that's when:

    **double quotes when the text contains single quotes**
    ```
    print("no, you didn't") -> no, you didn't 
    ``` 
    **or single quotes when text contains double quotes**
    ```
    print('say "hi" Karel') -> say "hi" Karel
    ```
2. ``input`` function or command that gets some text input from the user. It's going to prints any text inside the single or double quotes AND after it prints that text will sit there and wait for the user to type something in and after the user type and hits enter, that text the user has written basically comes back and is put into a variable that it's been declared. 
    * Remember that input is consider text even if the user entered a number, so if you want to take that text and treat it like a number you have to change it's type. 
    ``` 
    num1 = input("Enter first number: ")
    ``` 
3. What is a variable?

* A variable is a place to store information in a program. 
* It associates a name with a value
* You can create a new variable by assigning a value:

    **x = 10**
    * The idea here is the right hand side is the value that we want to assign, the left hand is the name of the variable.  
    * The first time we specify a particular name we're creating that variable or **declaring** the variable. 
    * The value can change with a new assignment:

    **x = 5**
    * You can set the value using mathematical expressions

    **x = 5 + 7**

4. Variable assignment
* You use the equal sign ``=`` to assign to a variable
    - Subsequent assignments give the variables a **new value** 
* Assignment is not the same as "equals" in math
    - Assigments: **first evaluate**  right-hand side, then **asiggn** to the variable on the left-hand side.
    - The ``=`` sign it's known as an assignment statement, which you're doing is assigning a value to a variable. You're not creating a equality by using = literally.
    - Consider the following code:
    ```
    total = 5
    total = total + 1
    ```
- Variables are only visible inside the function in which tey're created (called "scope" of the variable)

5. Variable names **must**:
- Start with a letter or an underscore ``_``
- Contain only letters, digits, or underscores.
- Cannot be a "built in" command in Python (e.g., **for**)
- Are case-sensitive:
    -Hello is **not** the name as hello
- Should:
    - Be descriptive of the value they refer to
    - Be in snake case (e.g., num_students)

6. Suitcase Analogy
*  When you store info in a variable it becomes a python **object**

7. Types
* What **type** of information variables carries
* **Integers** don't have decimal values, even if it's a .0 A decimal value is a **float** which is a real number 
* **str** or string are text of characters between single/ double quotes
* **bool** it's a logical value with a capital True/False (they're the only values)

8. Why do we have int and float?
    Depends of the question, for example:
    
How much do I weight? 
* Answer can be a real valued number
- There is no "next" number

Or How many children do I have?
* Answer is an integer
- There is a well defined "next" number. 
