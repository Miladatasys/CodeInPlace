# First meeting
### Learning Goals
* For loops, while loops and if statements
* Final project
* Celebrate:
    - Doing graphics
    - Data science
    - Final project it's optional but IS IMPORTANT FOR YOU!

### Section Page
* recorded lesson
* Worked or solved programs to watch
* Reading text book (karel's robot, python)

### Make-up session
* If you loose your session
* You can change your session twice

### TeachNow
* Pop-up it's a teacher that want's to teach somebody online (it's kind of random and fun)

### Certification at the end
If you complete Code In Place :) - YOU NEED TO GO TO YOUR SECTION IN ORDER TO GET IT. 

### Some context
Code In Place has it's own IDE ( intergrating development environment)
* What if you finish early the assigments? Don't stop, you can go to check-out and try to solve next week assignment. Help others, answer questions, or learn to teach.
* GET CREATIVE WHILE PROGRAMMING :D
* Don't do what just people told you, create.

# Lesson 1. For loops

## **Control Flow**
Control flow is like a mountain

You're in the horizon and these are your next steps:

1. for loops
2. while loops
3. if
4. if/else
5. Control Flow (the mountain)

**Comments**

1. Multi-line comment:
```
    """
    comment
    -------
    Another comment, could be an explanation of the code, doc
    """
```
2. One line comment
```
    # Karel turns to the right
```

**Functions**

Descriptive names 

(snake_case) is a convention that sets every word in the function is separated by an underscore 
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```
**Software engineering principle**:

Aim to make programs readable by **humans**

**Today's Goal**
1. **Code** using loops and conditions
2. **Trace** programs that use loops and conditions

- Definition: Sequence step to do something over and over
- The way we know what statements are outside of the body of the for loop is those statements that'll not longer indented

General form:
```
for i in range(count):
    statements # note indenting
```


**vocab**

count: number of times

statements: body of the loop

```
def turn_right():
    for i in range(3):
        turn_left() # note indenting
```
Practical example:
```
def main():
    # body in the loop
    for i in range(4):
        put_beeper()
        move()
        turn_left()
```
- Note: you need the postcondition of a loop to match the precondition
    ( what's expected to be true, match the condition that were before the loop so you can do the body of the loop successfully)

