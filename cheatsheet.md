# Basics:

## Declaring a variable
```
x = 14
```

## If Statement:
```
  if condition1:
    action1()
  elif condition2:
    action2()
  else:
    action3()
```

## For Loop
```
for i in range(10):
  print(i)
```

## While Loop
```
while x < 10:
  print(x)
```

## Comment
```python
# This is a comment
```

# Arithmetic 
| Action           | Code     |
|------------------|----------|
| Increment x by 1 | `x += 1` |
| Decrement x by 1 | `x -= 1` |


# Lists:

| Action                     | Code                                         |
|----------------------------|----------------------------------------------|
| Create an empty list       | `names = []`                                 |
| Create a list              | `names = ['Martha', 'Erin', 'Rupert']`       |
| Find the length of a list  | `len(names)`                                 |
| Get the 1st item (index 0) | `names[0]`                                   |
| Get the 2nd item (index 1) | `names[1]`                                   |
| Get the last item          | `names[-1]`                                  |
| Get the first x items      | `names[:x]`                                  |
| Get the last x items       | `names[-x:]`                                 |
| Get the 2nd and 3rd        | `names[1:3]`                                 |
| To reverse items on a list | `names[::-1]`                                |
| Looping through a list     | `for name in names:`                         |
| Adding items to a list     | `names.append('other')`                      |
| Combining lists            | `names + ['other', 'other']`                 |
| Repeat a list              | `names * 2`                                  |
| Filter a list              | [`name for name in names if name[0] == 't']` |


# Strings:
 A string is a series of characters.
 For example: The string "Hello" must be put in quote marks "" or single quotes ''.
 A string can be treated as a list of letters.
 All commands in the list section above work e.g.


| Action                            | Code                          |
|-----------------------------------|-------------------------------|
| Length of string                  | `len("Hello, World")`         |
| Define a string to be a variable  | `word = "Hello"`              |
| 1st letter                        | `word[0]`                     |
| Replace l with p (case sensitive) | `word.replace('l', 'p')`      |
| Split into list of words          | `word_description.split(' ')` |



# Functions:
| Action             | Code                 |
|--------------------|----------------------|
| declare a function | `def example(word):` |
| call a function    | `example('hello')`   |




