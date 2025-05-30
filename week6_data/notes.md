# Lesson 12 Lists

Goals:
1. Create a new list of values
2. Add values to a list
3. Retrieve values from a list

Youtube link: https://youtu.be/VXmWokBE3eY?si=k52dHQ6ahG_QzJix

* Variables have limitations:
    - it only adds two numbers

```
def add_two_numbers(num1, num2):
    return num1 + num2
```
So we're going to learn how to write programs that can reason about arbitrarily many values.

Goals:
1. Understand what a data structure is
2. Writing code to use lists
3. Understanding lists as parameters

**Our first lists**
- Lists begin and end with brackets and consist of ``elements``
- Elements are separated by ``commas``
- Every element in a list is assigned a position. The position of an element in a list is called it's ``index``. List indices start from 0.
- In programming we count from 0

**Accesing elements in a list**
```
names = ["Brahm", "Waymond", "Gwen"]
            0         1         2
# accesing the list specifically the element at index 0 which is equal to Brahm
first_element = names[0] # "Brahm"
```
We can access:

Negative indices **count backwards** from the end of the list 
and we can say that waymond is -2 and brham is -3
```
names = ["Brahm", "Waymond", "Gwen"]

last_element = names[-1] #  "Gwen"
```
Updating elements in a list:
```
names = ["Brahm", "Rebecca", "Gwen"]

names[1] = "Rebecca" #  "Gwen"
```
Getting the number of elements in a list: it counts from 1 as human does.
```
names = ["Brahm", "Rebecca", "Gwen"]

num_names = len(names) #3
```
**The formal term for putting elements inside the is **apending****

Here we insert that 42 at the very end of the list:
```
my_list.append(42)
```
Removing from a list:
- the pop function always removes by **index**
- the remove function instead of removing from a position, it removes the **first** instance of a  value from the list. 
```
my_list.pop()
# or
my_list.remove(42)
```
for loops:
```
numbers = [1,2,3,4]

for elem in numbers:
    print(elem)
```
How we can add elements to the list?
- extends takes all of the elements in one list (in this case, **another**) and inserts them in **my_list**
- combined is the product of **my_list** + **another**, so is basically a new list of the combined values on each list. The plus operator makes a new list
```
my_list = [42, 100, 10]
another = [2, 3, 4]
my_list.extend(another)
# or
my_list = [42, 100, 10]
another = [2, 3, 4]
combined = my_list + another
```
**Indices**
```
my_list = [42, 100, 10, 100]
idx = my_list.index(100) # Get's the first 100 or finds the first index of an elem in a list
```
insert:
```
my_list = 42, 100, 100
my_list.insert(1, 27) # will insert the elem at index 1
[42, 27, 100, 10]
```
there's functions: max(my_list), min, sum

live session:

- Strings are not mutable
- indexes start counting at 0
- list start with []
-  push operations
- with pop you give the index, 
- the remove asks for the element. 
- built in function len()
- dictorionaries, are mutable, just like lists
- make sure keys are in a dictionary or have some check to see if they are before trying to access or delete data
- keys have to be unique
- keys can be anything that is hashable, are often strings, though
- you can overwrite the previous values.
- print(type(fruit_list))
- w3school for programming for data structures 
- Tutorialspoint
- StackOverflow
- ChatGPT
- data accuracy, data integrity, is important to check null strings
- choice function to pick random elements, is part of the random lib
- infinite loop
