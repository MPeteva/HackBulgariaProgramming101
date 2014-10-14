TasksForCourseProgramming101Apply
=================================
# ExOH

Implement a function with the following signature: `ExOh(str)`

`str` is of type string.

The function should return `true` if there is an **equal number of x's and o's** in `str`.
It should return `false` otherwise.

Things to know:

* Only these two letters will be entered in the string, no punctuation or numbers. 
* You don't have to check for valid input.
* **You can use any language you know.**

Examples:

```python
ExOh('xoxoox') # true
ExOh('oooxoo') # false
```

# AB Check

You have the implement a function, with the following signature: `ABCheck(str)`.


The argument `str` is of type string.

The function should return `true` if the characters `a` and `b` **are separated by exactly 3 places anywhere in the string at least once.**

Otherwise return `false`

For example - `"lane borrowed"` would result in `true` because **there is exactly three characters between `a` and `b`**. .

**You can use any language you know.**

Examples:

```python
ABCheck("after badly") # false
ABCheck("Laura sobs") # true
```

# DashInsert

You have to implement a function with the following signature - `dashInsert(num)`

* The argument `num` is of type integer.
* The function should return a string


Insert dashes `'-'` between each two neighboring odd numbers in `num`. 

Don't count zero as an odd number.

**You can use any language you know.**

Examples:

```python
dashInsert(99946)
"9-9-946"
dashInsert(56730)
"567-30"
```

