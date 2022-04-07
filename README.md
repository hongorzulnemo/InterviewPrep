## Software engineer intern prep for Morgan Stanley

### Python3:
The **dictionary key** must be of a type that is **immutable**. 

**Immutable types: **
- integer, 
- float, 
- string,
- boolean,
- tuple. 
**Mutable types: **
- list, 
- dictionary, 
- sets.

---------------------------------------------------------------------
Data Structure    |  List  |  Tuple  |  Set  |  Dictionary          |
---------------------------------------------------------------------
Duclicate elements|  yes   |   yes   |  no   |  no(keys)/yes(values)|
---------------------------------------------------------------------
Different elements|  yes   |   yes   |  yes  |  yes/yes             |
---------------------------------------------------------------------

**Operations done in list:**
1. **append()** : adds one element at the time
example: zoo.append("monkey")  
2. **extend()** : adds more than one element at the time  
example: zoo.extend(["monkey", "lion", "elephant"])
3. **insert()** : adds element at a girn position in the list
example: zoo.insert(1, "snake")
4. **remove()** : removes only one element at the time. For duplicates, it removes the first occured element.
example: zoo.remove("hamster")
5. **pop()** : remove an element from any position in the list.
example: zoo.pop("fly")
6. **slice** : returns sublist without modifying original list.
example: zoo[start:end] the element at start is included, end in excluded.
7. **reverse()** : To reverse a list by modifying the original one
example: zoo.reverse()
To reverse a list by modifying the original one:
example: zoo[::-1]
8. **len()** : returns the length of the list
example: len(zoo) 
9. **min() & max()** : return minimum and maximum value in the list only when all elements have same type.
example: max([1, 2, 3]) | min([1, 2, 3])
10. **count()** : returns the number of occurrences of a given element in the list.
example: zoo.count("monkey")
11. **concatenate** : used to merge two lists and return a single list
example: zoo + ["donkey", "cat"]  
12. **multiply** : multiplies each element by given value
example: [1,2,3]*2
13. **index()** : returns the position of the first occurrence of the given element.
example: zoo.index("fish")
14. **sort()** : sorts the list in ascending order modifying the original list.
example: zoo.sort()
15. **sorted()** : returns a sorted list of the specified iterable object.
example: orderedZoo = sorted(zoo)
17. **clear()** :  erases all the elements from the list and empties them.
example: zoo.clear()


**Instance Attribute**

An instance attribute is a Python variable belonging to only one object. It is only accessible in the scope of the object and it is defined inside the constructor function of a class. For example, __init__(self,..).

**Class Attribute**

A class attribute is a Python Variable that belongs to a class rather than a particular object. This is shared between all other objects of the same class and is defined outside the constructor function __init__(self,…), of the class.

**Differences Between Class and Instance Attributes**

The difference is that class attributes are shared by all instances. When you change the value of a class attribute, it will affect all instances that share the same exact value. The attribute of an instance on the other hand is unique to that instance.
