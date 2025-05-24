# Graphics

**Learn by doing**

How humans learn?
Cover in video:
* Coding platform: ``code.org ``
* Machine learning 
* Deep Learning Algorithms (recurrent neural network) to analyze student learning process
* Coding is a new way to think: Keep challenging yourself. 

link https://youtu.be/vcOYlnZBP84?si=1bzgX03wTXcHSCdm
link https://youtu.be/-Dqlvfz7_X8?si=q7IyyIV9w_x_nkDv
How to draw things?

hello world of graphics: 
```
def main():
    canves = Canvas(800, 200)
    canvas.create_rectangle(20, 100, 100, "blue")
```
meanings:

1. 20, 20 is a location on the canvas.
    - The first 20 means pixels from the left
    - The second pixels from the top. 
    this define one point
2. To create a rectangle you need the bottom right point and that is 100, 100

**Couple of functions:**
```
canvas.create_line(x1, y1, x2, y2)
```
```
canvas.create_oval(x1, y1, x2, y2)
```
```
canvas.create_text(x1, y1, text='hi')
```
there're parameters like, color and font too.

Centered square:
https://youtu.be/dU6S3Z41xBU?si=21Yu3G-q7MS_n8ZR

Example using for loop:
https://youtu.be/fPOUg-M3n-U?si=bzhDyUkOjbE_siz8

**Important to understand:**

A 2D coordinate system is a way of locating points on a flat surface (like a computer screen or piece of paper) 
using **two numbers:**
- **X coordinate**: how far **left** or **right** a point is
- **Y coordinate**; how far **up** or **down** a point is

```
(x, y)
```
**How it works on a computer screen**

On a screen or canvas in programming:
- The top-left corner is ``(0,0)``.
- As **X increases**, you move to the **right**
- As **Y increases**, you move **down**
```
(0, 0)       → X increases →
   ┌──────────────────────┐
   │                      │
   │                      ↓ Y increases
   │                      │
   │                      │
   └──────────────────────┘
```
Example coordinates on a 300x300 canvas:

If your canvas is:
```
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
```
then:

1. Top-left: (0, 0)
- ``*`` is at the very top-left.
- X = 0 (far left), Y = 0 (top)

```
[Canvas: 300x300]

(x, y) = (0, 0)
* ← Top-left corner

*-------------------------->
|
|
|
v

```

2. Top-right: (300, 0)
- ``*`` is at the very top-right.
- X = 300 (far right), Y = 0 (top)
```
[Canvas: 300x300]

(x, y) = (300, 0)
                            * ← Top-right corner

<--------------------------*
|
|
|
v
```
3. Bottom-left: (0, 300)
- ``*`` is at the very bottom-left.
- X = 0 (far left), Y = 300 (bottom)

```    
[Canvas: 300x300]

(x, y) = (0, 300)
*
|
|
|
v
*--------------------------→

^ Bottom-left corner
```
4. Bottom-right: (300, 300)

- ``*`` is at the very bottom-right.
- X = 300, Y = 300
```
[Canvas: 300x300]

(x, y) = (300, 300)

|
|
|
v
                             *
<---------------------------*

^ Bottom-right corner
```

5. Center: (150, 150)

- ``*`` is in the center of the canvas.
- Half of 300 is 150 → X = 150, Y = 150

```
[Canvas: 300x300]

           ↑
           |
           |
           *
           |
           |
           ↓
   ←-----------------------→
      (x, y) = (150, 150)
```
I need to connect:
1. The top with the left
2. The bottom with the right

## Live session:
    - Functions, local scope,
    - Local variables
    - Parameters
    - null or void
    - return type

    - Graphics
        - 0,0 origin point
        - tangents

# Lesson Functions

**Goals:**
1. Define functions that take parameters
2. Define functions that return values

- Calling functions:
    One thing they all have in common is they all have parenthesis, do a task but one thing that's slighly different...Some of the have information that was given to them when they did their task.
    ```
    # Hello world is information
    print("hello world)

    #0.42 is the information
    float("0.42")

    # The coordinates of the rectangle are information
    canvas.create_rectangle(0,0, 100, 100, "red")
    ```
    and this begs the question: **How could we write this functions, that take in information?** and some of the functions **give back information** like:
    ```
    result = input("string please!")
    ```
https://youtu.be/yhA5FjQSB4g?si=3ttQmmt9u1ER_XTB

Anatomy of a function:

When working with functions, it's important to distinguish how a function is defined versus how it is used. There are two main components:

### 1. Function Definition

```
def average(a, b):  # parameters: placeholders for incoming values
    sum = a + b
    return sum / 2  # returns the result back to the caller
```
- ``def``: Keyword that tells Python you're defining a function.

- ``average``: Name of the function.

- ``a, b``: Parameters – variable names used to receive the input.

- ``return``: Ends the function and sends back a result to the caller.

Think of parameters as placeholders for actual values that the function will receive when called.

### 2. Function Call

This is where you use the function by providing actual values (arguments).

```
def main():
    mid = average(5.0, 10.2)  # arguments: actual data passed to the function
    print(mid)  # this prints the returned value
```
- ``average(5.0, 10.2)``: This is a function call with arguments 5.0 and 10.2.

-   The function``average``:  will be executed using those values.

-   The ``return value``: of the function replaces the call (i.e., mid becomes 7.6)

Think of a function call like using a tool you've made: you're putting in inputs (arguments), and it gives you back a result.

### What Does return Mean in a Function?

The ``return`` statement ends a function and sends a result back to the part of the program where the function was called.

Think of it like this:

- A function is like a **machine**.
- You `**give it input**` (arguments),
- **It does some work** (the code inside),
- Then **it gives you output** using ``return``.

- If there's no return, the function returns None
- That value can be saved or used
-You can return anything (Numbers, strings, lists, objects, etc.)