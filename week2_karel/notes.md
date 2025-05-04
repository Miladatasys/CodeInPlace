# Week 2

## **Lesson 5.Art of Problem Solving**

- Today's Goal:
    - Decompose: Be able to pproach a problem "top down".
    - Combined with the art of Stepwise Refinament: test as you go or balance testing while decomposing.

**How can you take a really big problem and solve it?**

Let's review the whole world of Karel:

- **Functions**, Karel's knows four commands but you can teach Karel new commands by defining new functions

- Karel can have **for loops** when knows how many times it has to do some action
- **while loops** for situations when you don't know how many times and keeps doing the actions until some condition is not true.
- **if statement** which is like a while loop but does not repeat. It just check the condition, if the condition is true, it does it. 
- **if / else statement** if the condition is true, we'll run the code in that specific code block (inside if), otherwise, it will run inside the else code block.

### **What are we going to learn?**
```
def art_of_problem_solving():
    # lesson plan
    decomposition()
    mountain_karel()
    rhoomba_karel()
    if extra_time():
        word_search_karel()
```

### Make pasta from scratch
Decomposing:
1. make_dough()

        # pre: ingredients
        # post: ball
        but it can have many more steps or conditions. Remember to use pre and post conditions on your comments.
2. shape_pasta()
3. cook_pasta()

### Mountain Karel, work example
Write a program that'll help Karel go from the base of a mountain, climb to the top, put a flag on the top marked by a beeper and then climb all the way down. In order to solve this problem, we're going to use an algorithm and practice decomposition.

This problem can be broken down to three steps:
1. climb up the mountain
2. plant flag
3. climb down

**Let's take the first step and break it into smaller pieces
1. clim up - ``while _____`` :

``stepup`` ->    

So step up is made out of four commands:

- left
- move
- right
- move

* We want to keep repeating as long as the front is blocked. If the front is blocked, repeat and if the front is no longer blocked, we've climbed the mountain and we are done. Now that we've taken one of our pieces and decomposed until the point where we've got a real milestone, let's **TEST AS YOU GO**, so let's test this code before we even think about climbing down the mountain. You can find the coding problem in ``examples/mountain_karel``
`
- **IMPORTANT Pro-tip for testing things up:** When trying out a new function (like stepup), follow this approach to avoid errors and ensure it works as expected:
1. **Test the Function Alone First**
    - Before writing a loop, call the function once to verify it behaves correctly.
    - Example: Run stepup() independently and check the output.

2. **Test Sequential Calls**
    - Once you confirm the function works, call it multiple times (e.g., stepup(); stepup()) to ensure repeated usage works as intended.

2. **Add a Loop Only After Validation**
    - If the function works correctly in isolation and in sequence, then wrap it in a while loop for automation.

**Why?**
This step-by-step method helps catch mistakes early and prevents debugging complex loops before the core function is reliable.
example:

```
from karel.stanfordkarel import *

def main():
    # Test step_up() in isolation first
    step_up()  # Run once to verify it works
    
    # Test sequential steps
    step_up()
    step_up()
    
    # Only after testing, use a loop (commented out for safety)
    # while front_is_blocked():
    #    step_up()

def step_up():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    main()
```

- Great programmers **write comments as they go**

** How to approach Pre/Post comments:**
1. **Ask these questions for ``pre``**:
    - What direction must karel be facing
    - Are there required beepers/walls nearby?
    - Is front/left/right clear or blocked?

2. **Ask these for ``post``**:
    - Where is Karel now?
    - What changed in the world (beeper placed/remove)?
    - Did Karel's direction change?

Common Pitfalls to Avoid:
- **Overcomplicating** ``pre``: Only list critical assumptions.
- **Vague** ``post``: Be specific about state changes.

#### Pro Tips for functions:

- A good function should do "**one** conceptual thing"
- Know what it does by looking at it's name
- Less than ten lines, 3 levels of indentation
- Reusable and easy to modify
- Well commented

There are two types of programs:

One is so complex, there is nothing obvious wrong with it. 

One is so clear, that is obviously nothing wrong with it.

#### Aside: common errors:

- Infinite loop:
    Imagine Karel is sitting in the middle of it's world and not facing any walls: 
    ```
    def turn_to_wall():
        while left_is_clear():
            turn_left()
    ```
- Pre/Post that Don't Match:
**Be really careful about this on your functions and loops**
1. What do you assume here? ``while front_is_clear():``
2. Does the end condition of the loop match the start assumptions?
```
def climb_mountain():
    while front_is_clear():
        # step up
        move()
        turn_left()
        move()
```

### Rhoomba Karel
A rhoomba robot it turns around the house cleaning all the mess

How should we approach this tricky problem? Here are a few options:

1. Spirals
2. Zigzag
3. Crazy path: allows you yo touch any corner on a rectangle that brings you in this crazy path
4. Comb: it has karel clear row, then come back, then go up a row and continue to karel's clear the whole world

If I'll have to say lightly that if you try to do one these two: ``Spirals``, ``Crazy path`` you'll find it incredible hard 
because as you get further into the algorithm , yo end up in conditions where is no walls around you and gets really hard to know if you need to stop.
So, I'd really like to focus on these two: ``Comb`` and ``Zigzag``. 

- A lot of students likes the zig zag algorithm because it has few commands and it feels efficient.
- In contrast, the comb has Karel clear row, then go all the way back, not picking up anything, and that feels a little wasteful.

But this is a real mindset shift, you have to think about how much work a computer can do. The important thing is to have a code that doesn't run bugs.
- One of the fathers of computer science as a discipline calls this **Premature optimization**  and says is the root of many of the worst bugs.

- A beautiful thing about the comb algorithm is that every single time you're done with one task, you have the exact same post condition. That consistency turns out to be critical 'cause it makes it so much easier to know if you've hit the end of the world. 

### So the point of this choice of algorithms is to highlight two ideas:

1. Don't worry too much about how many operations Karel's doing. Worry about the cleanliness of your code and how nicely you decomposed the problem.
2. Really be on the lookout for consistency. Can you have consistent assumptions that different parts of your program can make?
- You'll find a working solution in ``examples/comb.py``

That's all! If you have time, check out the wordsearch code.

## Live session

advices:
reserve keyword we don't use for names: return
a for loop 
concept in program try not repeat yourself


# Joseph session

### Utilities:

- Safety first:
```

```

-  Main character motion:
```

```

- Let's get reoriented:
```

```

- There's no place like home:
```

```

#### EXPLANATIONS:
_ or i in a for loop is just a variable name that we give to the loop index. 

