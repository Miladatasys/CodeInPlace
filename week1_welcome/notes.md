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

# Lesson 1. **For** loops

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

- count: number of times

- statements: body of the loop

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

# Lesson 2. **While** loops and **If** statements

While loops: When we want to do something over and over but we're not exactly sure how many times you want to do it  when you start out

Sintax: 
```
while condition:
    statements # note indenting
```
**vocab**

- condition: true or false (boolean)
- body of the while loop: is indented
- Bug: moth (bug) Grace Hopper was the first one to debug

While condition is true, then executes the body of the statement, if is false does not execute the body. and it's a loop so goes back up and checks the condition again and keeps doing it until the condition it's false. 

Example:
```
def move_to_wall():
    while front_is_clear():
        move() # note indenting, this is the body of the loop, a single statement
```

* Karel has a lot of built-in conditions (you can read them in docs)

Look this example: this code has a bug, why?
```
# Place beeper line
def main():
    while front_is_clear():
        put_beeper()
        move()
```
The idea is that we're missing a beeper on the final corner, so what are we going to do?

```
def main():
    while front_is_clear():
    put_beeper()
    move()
put_beeper() # add final put_beeper() 
```
now it's fixed! with an statement outside the body of the while loop, so when the entire loop is done, it execute the next statement remaining outside **(kudos to indentation)**

- General pattern: Fence Post Problem:

    The "off-by-one" error (or fencepost problem) occurs when you mistakenly count the gaps between items instead of the items themselves, like building a 10-meter fence with posts every meter and thinking you need 10 posts when you actually need 11 (since the first post starts at 0 meters and the last at 10 meters) - similarly in programming, loops often need careful handling of starting/ending points because computers count from 0 (like range(5) producing 0-4) while humans naturally think from 1, leading to either missing the last iteration or going one step too far when processing sequences.

    example:
    **Problem:** Move Karel forward 5 times (should end 5 spaces right of start)
    from karel.stanfordkarel import *
```
def main():
    # Wrong version (off-by-one - only moves 4 times)
    for i in range(4):  # ← Classic mistake! range(4) = 0,1,2,3 (4 iterations)
        move()           #    but we wanted 5 moves
    
    # Correct version
    for i in range(5):  # range(5) = 0,1,2,3,4 (5 iterations)
        move()          # Now Karel moves exactly 5 times

if __name__ == '__main__':
    main()
```

- range(n) gives you n iterations (from 0 to n-1)

- If you want n actions, you need range(n)

- The error occurs when you confuse the number of actions with the count of loop iterations

This is the programming equivalent of the fencepost problem - thinking you need 4 posts to make 4 gaps when you actually need 5 posts.

* A program executes one line at a time.
    - the **while** loop checks its condition only at the start of the code block and before repeating. 

### When you want to do something over and over you might want to have a loop. The question is which kind of loop: for, while?

- **for** Loop: KNOW how many times (definite loop)
    - because you **count** some number of times

- **while** Loop: DON'T know how many times (indefinite loop)
    - until some condition is no longer true, but you don't know how many times you need to repeat it until it's true 

## While Loops and If statements

**If** statement:

Is not a loop, it says: If and it has some condition here that's the same kind of notion of a condition that you saw on while loops and if that condition is true then what it will do is it execute the set of statements in the body of the loop and then keep executing from what comes after the loop. If the condition is false it will not do the body of the statement, it will just execute the statements that comes after the if statement.

Again, this is not a loop, the basic ideas that comes here and it checks this condition that it's going to be true or false.
```
if condition:
    statements # note indenting
```
example: 
```
def safe_pick_up():
    if beepers_present():
    pick_beeper() # note indenting
```
### **if-else statements**

The idea behind: Take the if statement and add a little more to it.

```
if condition:
    statements # note indenting (body of the if (true statement))
else:
    statements # note indenting (body else part, this get executed when the condition is false )
```
if the condition is false, it will skip the part of the body of the if and go directly to else.

```
def invert_beepers():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()
```
**REMEMBER** this is **not** a loop, it's just checking if this condition is true or false. It's only happening once.

### Steeple Chase - putting it all together SteepChaseKarel.py

Control structure we've seen:

1. for loops
2. while loops
3. if statements