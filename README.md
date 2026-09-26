# 📖 Learning Log: Learn Python Programming by Fabrizio Romano & Heinrich Kruger

This repository documents my learning journey as I follow along and apply the concepts from the book [Learn Python Programming]() by [Fabrizio Romano]() and [Heinrich Kruger]().

## 🧭 Table of Contents

- [🧠 What I learned](#🧠-what-i-learned)
    - [Python objects & object mutability](#python-objects--object-mutability)
    - [Choosing the right data structure](#choosing-the-right-data-structure)
    - [Assignment expressions](#assignment-expressions)
    - [Scopes & namespaces](#scopes--namespaces)
    - [Functions guidelines](#functions-guidelines)
- [🌱 Continued Development](#🌱-continued-development)
- [📚 Useful resources](#📚-useful-resources)
- [👩🏽‍💻 Author](#👩🏽‍💻-author)

## 🧠 What I learned

### Python objects & object mutability

*Everything* in Python is an object. Every object has the following characteristics:

- an ```identity (ID)```
- a ```type```
- a ```value```

Below is an example of an instruction in `Python`:

```python
name = 42
```

When the above instruction is executed, an object with an `id`, `type` and `value` is created. The name `age` is used to point to and retrieve the object depending on the scope of the instruction within the `Python` program.

This can be illustrated as follows:

```mermaid
flowchart LR
    markdown("`**age**`")
    newLines("`id: 4333712608
    type: *int*
    value: 42`")
    markdown --> newLines
```

Below, `age` is a name that is initially set to point to an *`int`* object of value `42`, which is **immutable** i.e., it cannot change.

Another *`int`* object of value `43` is then created and the name `age` is set to point to it.
Therefore, `42` was not changed to `43`, but the name `age` was set to point to a different location.

```bash
>>> age = 42
>>> id(age)
4333712608
>>> age = 43
>>> id(age)
4333712640
```

```mermaid
flowchart TD
    markdown("`**age**`")
    newLines_01("`id: 4333712608
        type: *int*
        value: 42`")
    newLines_02("`id: 4333712640
        type: *int*
        value: 43`")
    markdown --> newLines_02
```

### Choosing the right data structure

Ease of use, performance and giving precedence to what matters the most within the context at hand strongly determine the data structure to be used.

A good indicator that the appropriate data structure has been used is the nature of the code written in order to manipulate it.

If the code logic comes easily and flows naturally, then the appropriate data structure has been selected. 
However, if the code gets unnecessarily complicated, then the choice of data structure may need to be reconsidered.

### Assignment expressions

These allow binding a value to a name in places where normal assignment statements aren't allowed e.g. in `if` and `while` statements.

Assignment expressions use `:=` (known as the **walrus operator**) instead of the normal assignment operator `=`.

When used in an `if` statement,

```python
value = 13
modulus = 5

remainder = value % modulus

if remainder:
    print(f"Not divisible! The remainder is {remainder}.")
```

becomes

```python
...

if remainder := value % modulus:
    print(f"Not divisible! The remainder is {remainder}.")
```

When simplifying a `while` loop,

```python
flavors = ["pistachio", "malaga", "vanilla", "chocolate"]
prompt: "Choose your flavor: "

print(flavors)

while True:
    choice = input(prompt)
    if choice in flavors:
        break
    print(f"Sorry, '{choice}' is not a valid option.")

print(f"You chose '{choice}'.")
```

becomes

```python
...

while (choice := input(prompt)) not in flavors:
    print(f"Sorry, '{choice}' is not a valid option.")

print(f"You chose '{choice}'.")
```

### Scopes & namespaces

`Python` searches for names in scopes according to the **LEGB** rule: **local**, **enclosing**, **global** and **built-in** scopes.

```mermaid
---
title: LEGB
---
flowchart BT
    Global --> Built-in
    Enclosing --> Global
    Local --> Enclosing
```

This shadowing of names can be altered using either of the statements `global` or `nonlocal`.

The `nonlocal` statement changes this behaviour by working in enclosing scopes whereas the `global` statement does so by working in the global scope.

### Functions guidelines

Some guidelines to follow when writing functions include:

- **Functions should do one thing:** easy to describe in one short sentence. Those that do multiple things can be split into smaller functions that do one thing.
- **Functions should be small:** easier to test and write.
- **The fewer the input parameters, the better:** a lot of parameters in a function make it harder to manage, among other issues.
- **Functions should be consistent in their return values:** write functions that return in a consistent way regardless of the logic behind them.
E.g. returning `False` and `None` are not the same thing even within a Boolean context where they both evaluate to `False`.
`False` means there is information while `None` means there is no information.
- **Functions should have no side effects:** **pure functions** are a concept in functional programming that adhere to two main principles:
    - *Deterministic output:* given the same set of inputs the output produced will always be the same.
    The function's behaviour is not dependent on any external or global state that might change during execution.
    - *No side effects:* do not cause any observable side effects in the system.
    They do not alter any external state e.g. modifying global variables or performing I/O operations like reading from or writing to a file or the display.

## 👩🏽‍💻 Author

| Platform | Link |
| :--- | :--- |
| **Technical Blog** | [https://grace-sampao.github.io/](https://grace-sampao.github.io/) |
| **LinkedIn** | [Grace Sampao](https://www.linkedin.com/in/grace-sampao) |
| **X (formerly Twitter)** | [@grace-sampao](https://x.com/grace_sampao) |
| **Email** | sampaograce@gmail.com |
