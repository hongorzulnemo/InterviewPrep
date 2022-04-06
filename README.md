## Software engineer intern for Morgan Stanley

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

____________________________________________________________________
Data Structure    |  List  |  Tuple  |  Set  |  Dictionary          |
____________________________________________________________________
Duclicate elements|  yes   |   yes   |  no   |  no(keys)/yes(values)|
____________________________________________________________________
Different elements|  yes   |   yes   |  yes  |  yes/yes             |
____________________________________________________________________

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



