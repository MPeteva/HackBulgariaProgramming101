Week 0
=====

##1. N-th Fibonacci

The most annoying problem of all. Implement a function, called ```nth_fibonacci(n)``` that returns the n-th fibonacci number, given by the argument.

### Signature

```python
def nth_fibonacci(n):
    #implementation here
```

### Test examples

```
>>> nth_fibonacci(1)
Output: 1
>>> nth_fibonacci(2)
Output: 1
>>> nth_fibonacci(3)
Output: 2
>>> nth_fibonacci(10)
Output: 55
>>>
```

##Мore Information:

Числата на Фибоначи в математиката образуват редица, която се дефинира рекурсивно по следния начин:

    ```
    F(0) = 1
    F(1) = 1
    F(n) = F(n-1) + F(n-2)
    ```
    
Започва се с 1 и 1, а всеки следващ член на редицата се получава като сума на предходните два. Първите няколко числа на Фибоначи са

    ```
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...
    ```
    
Някои от основните свойства на числата на Фибоначи са:

    ```
    (F(n),F(m)) = F((m,n)) т.е. НОД на числата F(n) и F(m) e число на Фибоначи с индекс НОД(m,n)
    
    F(n+k) = F(k-1) * F(n) + F(k) * F(n+1)
    
    F(k)/F(kn) за произволно n т.е. F(k) дели F(kn)
    ```
### Произход

Италианският математик Леонардо Фибоначи публикува през 1202г. редица от числа, всяко от които се получава като сума от предходните двe: 1, 2, 3, 5, 8, 13, 21,… Той е научил за тази редица от числа по време на пътешествията си в страните от тогавашния Изток и редицата  е била наречена на негово име, защото я е популяризирал. 

Оказва се, че колкото по-големи са числата от редицата на Фибоначи, толкова отношението на двете последни числа се приближава до 'Златното сечение'. 

###Често редицата на Фибоначи се свързва и със следната задача:

Чифт зайци (мъжки и женски екземпляр) могат да произведат за единица време (един месец) нов чифт зайци, които продължават да се размножават (в класическата задача на Фибоначи на новородения чифт зайци са му необходими два месеца, за да дадат първото си поколение, след което продължават да се размножават всеки месец). Колко е броят на живите чифтове зайци след определено време, ако никой не унищожава зайците (и те не умират)? Отговорът се дава от последното число в редицата на Фибоначи. Разбира се, тази задача е чисто илюстративна. 

```
Example:
    1m -1 pair old
    2m -1 pair old & 1 pair young
    3m -2 pair old & 1 pair young  т.е. young --> old, previous old got new young.
    4m -3 pair old & 2 pair young
    5m -5 pair old & 3 pair young
```

### Първите 100 числа от редицата на Фибоначи
```
пореден номер |     число на Фибоначи
            1 |                     1
            2 |                     1
            3 |                     2
            4 |                     3
            5 |                     5
            6 |                     8
            7 |                    13
            8 |                    21
            9 |                    34
           10 |                    55
           11 |                    89
           12 |                   144
           13 |                   233
           14 |                   377
           15 |                   610
           16 |                   987
           17 |                  1597
           18 |                  2584
           19 |                  4181
           20 |                  6765
           21 |                 10946
           22 |                 17711
           23 |                 28657
           24 |                 46368
           25 |                 75025
           26 |                121393
           27 |                196418
           28 |                317811
           29 |                514229
           30 |                832040
           31 |               1346269
           32 |               2178309
           33 |               3524578
           34 |               5702887
           35 |               9227465
           36 |              14930352
           37 |              24157817
           38 |              39088169
           39 |              63245986
           40 |             102334155
           41 |             165580141
           42 |             267914296
           43 |             433494437
           44 |             701408733
           45 |            1134903170
           46 |            1836311903
           47 |            2971215073
           48 |            4807526976
           49 |            7778742049
           50 |           12586269025
           51 |           20365011074
           52 |           32951280099
           53 |           53316291173
           54 |           86267571272
           55 |          139583862445
           56 |          225851433717
           57 |          365435296162
           58 |          591286729879
           59 |          956722026041
           60 |         1548008755920
           61 |         2504730781961
           62 |         4052739537881
           63 |         6557470319842
           64 |        10610209857723
           65 |        17167680177565
           66 |        27777890035288
           67 |        44945570212853
           68 |        72723460248141
           69 |       117669030460994
           70 |       190392490709135
           71 |       308061521170129
           72 |       498454011879264
           73 |       806515533049393
           74 |      1304969544928657
           75 |      2111485077978050
           76 |      3416454622906707
           77 |      5527939700884757
           78 |      8944394323791464
           79 |     14472334024676221
           80 |     23416728348467685
           81 |     37889062373143906
           82 |     61305790721611591
           83 |     99194853094755497
           84 |    160500643816367088
           85 |    259695496911122585
           86 |    420196140727489673
           87 |    679891637638612258
           88 |   1100087778366101931
           89 |   1779979416004714189
           90 |   2880067194370816120
           91 |   4660046610375530309
           92 |   7540113804746346429
           93 |  12200160415121876738
           94 |  19740274219868223167
           95 |  31940434634990099805
           96 |  51680708854858323072
           97 |  83621143489848422977
           98 | 135301852344706746049
           99 | 218922995834555169026
          100 | 354224848179261915075
```

=====
##2. Sum all digits of a number

Given an integer, implement a function, called ```sum_of_digits(n)``` that calculates the sum of the digits of n.

If a negative number is given, the function should work as if it was positive.

For example, if n is ```1325132435356```, the digit's sum is 43.
If n is -10, the sum is 1 + 0 = 1

Keep in mind that in Python, there is a special operator for integer division:

```
>>> 5 / 2
2.5
>>> 5 // 2    # Закръгля на долу!!!
2
```

### Signature

```python
def sum_of_digits(n):
    # implementation
```

### Test examples

```
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```

##3. Sum all divisors of an integer

Given an integer, implement a function, called ```sum_of_divisors(n)``` that calculates the sum of all divisors of n.

For example, the divisors of 8 are 1,2,4 and 8 and ```1 + 2 + 4 + 8 = 15```
The divisors of 7 are 1 and 7, which makes the sum = 8

### Signature

```python
def sum_of_divisors(n):
    # implementation
```

### Test examples

```
>>> sum_of_divisors(8)
15
>>> sum_of_divisors(7)
8
>>> sum_of_divisors(1)
1
>>> sum_of_divisors(1000)
2340
```

### More information

For iterating over a closed range of integers [a, b] in python.

We can use the following way of doing it:

```
for i in range(a, b+1):    # Интервала е затворен от ляво и отворен от дясно!!!
    do_something(i)
```

For iterating in the reverse direction (ie. in the order b, b-1, b-2, ..., a):

```
for i in range(b, a-1, -1):
    do_something(i)
```

```
    1    to   35
____________________________________________
n   	Divisors                       Sum
1   	1 	                           1
2   	1, 2 	                       3
3 	    1, 3                           4
4    	1, 2, 4                        7
5   	1, 5                           6
6   	1, 2, 3, 6                     12
7   	1, 7                           8
8   	1, 2, 4, 8                     15
9   	1, 3, 9 	                   13
10   	1, 2, 5, 10                    18
11 	    1, 11                          12
12   	1, 2, 3, 4, 6, 12              28
13 	    1, 13                          14
14   	1, 2, 7, 14                    24
15 	    1, 3, 5, 15                    24
16  	1, 2, 4, 8, 16                 31
17  	1, 17                          18
18  	1, 2, 3, 6, 9, 18 	           39
19  	1, 19 	                       20
20  	1, 2, 4, 5, 10, 20 	           42
21  	1, 3, 7, 21                    32
22  	1, 2, 11, 22                   36
23  	1, 23                          24
24  	1, 2, 3, 4, 6, 8, 12, 24       60
25  	1, 5, 25                       31
26  	1, 2, 13, 26                   42
27  	1, 3, 9, 27                    40
28  	1, 2, 4, 7, 14, 28             56
29  	1, 29                          30
30  	1, 2, 3, 5, 6, 10, 15, 30      72
31  	1, 31                          32
32  	1, 2, 4, 8, 6, 32              63
33  	1, 3, 11, 33                   48
34  	1, 2, 17, 34                   54
35  	1, 5, 7, 35                    48
```

=====

##4. Check if integer is prime

Given an integer, implement a function, called ```is_prime(n)``` which returns True if n is a prime number. You should handle the case with negative numbers too.

A primer number is a number, that is divisible only by 1 and itself.

1 is not considered to be a prime number. [If you are curious why, find out here.](http://www.youtube.com/watch?v=IQofiPqhJ_s)

### Signature

```python
def is_prime(n):
    # implementation
```

### Test examples

```
>>> is_prime(1)
False
>>> is_prime(2)
True
>>> is_prime(8)
False
>>> is_prime(11)
True
>>> is_prime(-10)
False
```

##More information:

    Importing modules:
    
    ```
    From math import sqrt, ceil
    ```
    
    sqrt - коренуване
    ceil - закръгляне на горе
    
```
         1    to    40
    ________________________
 1 − 20          21 − 40
________        __________
1 	            21 	3·7
2 	            22 	2·11
3 	            23
4 	2^2         24 	2^3·3
5 	            25 	5^2
6 	2·3         26  2·13
7 	            27  3^3
8 	2^3         28  2^2·7
9 	3^2         29  29
10 	2·5         30  2·3·5
11 	            31
12 	2^2·3       32  2^5
13 	            33  3·11
14 	2·7         34  2·17
15 	3·5         35  5·7
16 	2^4         36  2^2·3^2
17 	            37
18 	2·3^2       38  2·19
19 	            39  3·13
20 	2^2·5       40  2^3·5
```

====

##5. Check if a number has a prime number of divisors

Given an integer, implement a function, called ```prime_number_of_divisors(n)``` which returns True if the number of divisors of n is a prime number. False otherwise.

For example, the divisors of 8 are 1,2,4 and 8, a total of 4. 4 is not a prime.
The divisors of 9 are 1,3 and 9, a total of 3, which is a prime number.

### Signature

```python
def prime_number_of_divisors(n):
    # Implementation
```

### Test examples

```
>>> prime_number_of_divisors(7)
True
>>> prime_number_of_divisors(8)
False
>>> prime_number_of_divisors(9)
True
```

## More information:

    How to add function from your .py file(module):
    
    ```
    from is_prime_4 import is_prime
    ```
    

##6. Are there n sevens in a row?

Implement a function, called ```sevens_in_a_row(arr, n)```, which takes an array of integers ```arr``` and a number ```n > 0```

The function returns True, __if there are n consecutive sevens__ in ```arr```

For example, if ```arr``` is ```[10, 8, 7, 6, 7, 7, 7, 20, -7]``` and n is 3, the function should return True. Otherwise, it returns False

### Signature

```python
def sevens_in_a_row(arr, n)
```

### Test examples

```
>>> sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
True
>>> sevens_in_a_row([1,7,1,7,7], 4)
False
>>> sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
True
>>> sevens_in_a_row([7,2,1,6,2], 1)
True
```

##7. Integer Palindromes

A palindrome is а word or a phrase or a number, that when reversed, stays the same.

For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".

But this time, we are not interested in words but numbers.
A number palindrome is a number, that taken backwards, remains the same.

For example, the numbers 1, 4224, 9999, 1221 are number palindromes.

Implement a function, called ```is_int_palindrome(n)``` which takes an integer and returns True, if this integer is a palindrome.

### Signature

```python
def is_int_palindrome(n):
    # implementation
```

### Test examples

```
>>> is_int_palindrome(1)
True
>>> is_int_palindrome(42)
False
>>> is_int_palindrome(100001)
True
>>> is_int_palindrome(999)
True
>>> is_int_palindrome(123)
False
```

##8. Number containing a single digit?

Implement a function, called ```contains_digit(number, digit)``` which checks if ```digit``` is contained by the given ```number```.

```digit``` and ```number``` are integers.

### Signature

```python
def contains_digit(number, digit):
    # Implementation
```

### Test examples

```
>>> contains_digit(123, 4)
False
>>> contains_digit(42, 2)
True
>>> contains_digit(1000, 0)
True
>>> contains_digit(12346789, 5)
False
```

##9. Number containing all digits?

Implement a function, called ```contains_digits(number, digits)``` where ```digits``` is a __list of integers__ and a ```number``` is an integer.

The function should return True if __all__ ```digits``` are contained by ```number```

### Signature

```python
def contains_digits(number, digits):
    # Implementation
```

### Test examples

```
>>> contains_digits(402123, [0, 3, 4])
True
>>> contains_digits(666, [6,4])
False
>>> contains_digits(123456789, [1,2,3,0])
False
>>> contains_digits(456, [])
True
```

##10. Is number balanced?

A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number ```1238033``` is balanced, bacause it has a left part, equal to 123, and right part, equal ot 033.

We have : ```1 + 2 + 3 = 0 + 3 + 3 = 6```

A number with only one digit is always balanced.

Implement a function, called ```is_number_balanced(n)``` which checks if the given number is balanced.

### Signature

```python
def is_number_balanced(n):
    # Implementation
```

### Test examples

```
>>> is_number_balanced(9)
True
>>> is_number_balanced(11)
True
>>> is_number_balanced(13)
False
>>> is_number_balanced(121)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True

```

##11. Counting substrings

Implement a function, called ```count_substrings(haystack, needle)``` which returns the count of occurrences of the string ```needle``` in the string ```haystack```.

__Don't count overlapped substings and take case into consideration!__
For overlapping substrings, check the "baba" example below.

### Signature

```python
def count_substrings(haystack, needle):
    # Implementation
```

### Test examples
```
>>> count_substrings("This is a test string", "is")
2
>>> count_substrings("babababa", "baba")
2
>>> count_substrings("Python is an awesome language to program in!", "o")
4
>>> count_substrings("We have nothing in common!", "really?")
0
>>> count_substrings("This is this and that is this", "this")  # "This" != "this"
2
```

##12. Vowels in a string

Implement a function, called ```count_vowels(str)``` which returns the count of all vowels in the given string ```str```. __Count uppercase vowels as well!__

The vowels are ```aeiouy```.

### Signature

```python
def count_vowels(str):
    # Implementation
```

### Test examples

```
>>> count_vowels("Python")
2
>>> count_vowels("Theistareykjarbunga") #It's a volcano name!
8
>>> count_vowels("grrrrgh!")
0
>>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
>>> count_vowels("A nice day to code!")
8
```

##13. Consonants in a string

Implement a function, called `count_consonants(str)` which returns the count of all consonants in the given string `str`. __Count uppercase consonants as well!__

The consonants are ```bcdfghjklmnpqrstvwxz```.

### Signature

```python
def count_consonants(str):
    # Implementation
```

### Test examples

```
>>> count_consonants("Python")
4
>>> count_consonants("Theistareykjarbunga") #It's a volcano name!
11
>>> count_consonants("grrrrgh!")
7
>>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
>>> count_consonants("A nice day to code!")
6
```

##14. Turn a number into a list of digits

Implement a function, called ```number_to_list(n)``` which takes an integer ```n``` and returns a list, containing the digits of ```n```

### Signature

```python
def number_to_list(n):
    # Implementation
```

### Test Examples

```
>>> number_to_list(123)
[1, 2, 3]
>>> number_to_list(99999)
[9, 9, 9, 9, 9]
>>> number_to_list(123023)
[1, 2, 3, 0, 2, 3]
```

##14. Turn a list of digits into a number

Implement a function, called ```list_to_number(digits)``` which takes a list of digits (integers) and returns the number, containing those digits.

### Signature

```python
def list_to_number(digits):
    # Implementation
```

### Test Examples

```
>>> list_to_number([1,2,3])
123
>>> list_to_number([9,9,9,9,9])
99999
>>> list_to_number([1,2,3,0,2,3])
123023
```

##15. Biggest difference between two numbers

Implement a function, called ```biggest_difference(arr)```, which takes an array of integers and returns the biggest difference between any two numbers from the array.

For every two elements from the array ```a``` and ```b```, we are looking for the minimum of ```a - b``` or ```b - a```

### Signature

```python
def biggest_difference(arr):
    # Implementation
```

### Test examples

```
>>> biggest_difference([1,2])
-1
>>> biggest_difference([1,2,3,4,5])
-4
>>> biggest_difference([-10, -9, -1])
-9
>>> biggest_difference(range(100))
-99
```

##16. Increasing sequence?

Implement a function, called ```is_increasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously increasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously increasing if for every two elements a and b, that are next to each other (a is before b), we have a < b

For example, ```[1,2,3,4,5]``` is monotonously increasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_increasing(seq):
    # Implementation
```

### Test examples

```
>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False
```

##17. Descreasing sequence?

Implement a function, called ```is_decreasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously decreasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously decreasing if for every two elements a and b, that are next to each other (a is before b), we have a > b

For example, ```[5,4,3,2,1]``` is monotonously decreasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_decreasing(seq):
    # Implementation
```

### Test examples

```
>>> is_decreasing([5,4,3,2,1])
True
>>> is_decreasing([1,2,3])
False
>>> is_decreasing([100, 50, 20])
True
>>> is_decreasing([1,1,1,1])
False
```

##18. Zero Insertion

Given an integer, implement a function, called `zero_insert(n)`, which returns a new integer, constructed by the following algorithm:

* If two neighboring digits are the same (like `55`), insert a 0 between them (`505`)
* Also, if we add two neighboring digits and take their module by 10 (`% 10`) and the result is 0 - add 0 between them.

For example, if we have the number `116457`, result will be: `10160457`:

* 1 and 1 are the same, so we insert 0 between them
* `6 + 4 % 10 = 0`, so we insert 0 between them.


### Examples

```python
zero_insert(116457)
10160457
zero_insert(55555555)
505050505050505
zero_insert(1)
1
zero_insert(6446)
6040406
```

##19. Sum Numbers in Matrix

You are given a `NxM` matrix  of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in python.

### Examples:

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55
```

##20. Matrix Bombing

You are givn a `NxM` matrix of integer numbers.

We can drop a bomb at any place in the matrix, which has the following effect:

* All of the 8 neighbours of the target are reduced by the value of the target.
* Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:

```
10 10 10
10  9  10
10 10 10
```

and we drop bomb at `9`, this will result in the following matrix:

```
1 1 1
1 9 1
1 1 1
```

Implement a function called `matrix_bombing_plan(m)`.

The function should return a dictionary where keys are positions in the matrix, represented as tuples, and values are the total sum of the elements of the matrix, after the bombing at that position.

The positions are the standard indexes, starting from `(0, 0)`

For example if we have the following matrix:

```
1 2 3
4 5 6
7 8 9
```

and run the function, we will have:

```python
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}
```

We can see that if we drop the bomb at `(1, 1)` or `(2, 1)`, we will do the most damage!

## Hack Numbers

A hack number is an integer, that matches the following criteria:

* The number, represented in binary, is a palindrom
* The number, represented in binary, has an odd number of 1's in it

Example of hack numbers:

* 1 is `1` in binary
* 7 is `111` in binary
* 7919 is `1111011101111` in binary

Implement a function, called `next_hack(n)` that takes an integer and returns the next hack number, that is bigger than `n`

### Examples

```python
>>> next_hack(0)
1
>>> next_hack(10)
21
>>> next_hack(8031)
8191
```

##21. NaN Expand

In most programming languages, `NaN` stands for `Not a Number`

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number' // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms :P) that many `times`

For example:

* If we expand `NaN` once (`times=1`), we will have `"Not a NaN"`
* If we expand `NaN` twice (`times=2`), we will have `"Not a Not a NaN"`
* If `times=3`, we have `"Not a Not a Not a NaN"`
* And so on ...

### Examples

```python
>>> nan_expand(0)
""
>>> nan_expand(1)
"Not a NaN"
>>> nan_expand(2)
"Not a Not a NaN"
>>> nan_expand(3)
"Not a Not a Not a NaN"
```

##22. Iterations of NaN Expand

Implement a function, called `iterations_of_nan_expand(expanded)` that takes a string `expanded`, which is an unkown iteration of NaN Expand (check the problem for more information)

The function should return the number of iterations that have been made, in order to get to `expanded`

For example, if we have `"Not a Not a Not a NaN"` - this is the 3rd iteration of `NaN`

**If `expanded` is not a valid NaN expand string, the function should return false! (This is the hard part)**

### Examples

```python
>>> iterations_of_nan_expand("")
0
>>> iterations_of_nan_expand("Not a NaN")
1
>>> iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
10
>>> iterations_of_nan_expand("Show these people!")
False
```



##23. Integer prime factorization

Given an integer ```n```, we can factor it in the following form:

> n = p1^a1 * p2^a2 * ... * pn^an

Where each p is a prime number and each a is an integer and p^a means p to the power of a.

[This is called prime factorization.](http://mathworld.wolfram.com/PrimeFactorization.html)

Lets see few examples

> 10 = 2^1 * 5^1
> 25 = 5^2
> 356 = 2^2 * 89 ^ 1

Implement a function, called ```prime_factorization(n)``` which takes an integer and returns a list of tuples ```(pi, ai)```, which is the result of the factorization.

The list should be sorted in increasing order of the prime numbers.

### Signature

```python
def prime_factorization(n):
    # Implementation
```

### Test examples

```
>>> prime_factorization(10)
[(2, 1), (5, 1)] # This is 2^1 * 5^1
>>> prime_factorization(14)
[(2, 1), (7, 1)]
>>> prime_factorization(356)
[(2, 2), (89, 1)]
>>> prime_factorization(89)
[(89, 1)] # 89 is a prime number
>>> prime_factorization(1000)
[(2, 3), (5, 3)]
```
##24. Calculate coins

This problem is from the [Python 2013 course in FMI](http://2013.fmi.py-bg.net/)

Implement a function, called ```calculate_coins(sum)``` where sum is a floating point number.

The function should return a dictionary, that represents a way to get the sum with minimal number of coins.

__The coins that we can use are with values 1,2,100,5,10,50,20.__

Check the examples below.

### Signature

```python
def calculate_coins(sum):
    # Implementation
```

### Test examples

```
>>> calculate_coins(0.53)
{1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0} # We pay with one coin of value 50 and two coins of value 2 and one coin of value 1 - that's the minimal number of coins to get to 0.53
>>> calculate_coins(8.94)
{1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}
```

##25. What is the sign?

This problem is from the Python 2013 course in FMI. [Link to original problem statement.](http://2013.fmi.py-bg.net/tasks/1)

Implement a function, called ```what_is_my_sign(day, month)``` which takes two integers (one for the day and one for the month) and returns the name of the zodiac for the given time period.

Consider the following zodiac table ([Or check wikipedia](http://en.wikipedia.org/wiki/Zodiac#Table_of_dates)) :

* Aries: 21 March – 20 April
* Taurus: 21 April – 21 May
* Gemini: 22 May – 21 June
* Cancer: 22 June – 22 July
* Leo: 23 July – 22 August
* Virgo: 23 August – 23 September
* Libra: 24 September – 23 October
* Scorpio: 24 October – 22 November
* Sagittarius: 23 November – 21 December
* Capricorn: 22 December – 20 January
* Aquarius: 21 January – 19 February
* Pisces: 20 February – 20 March


### Signature

```python
def what_is_my_sign(day, month):
    # Implementation
```

### Test examples

```
>>> what_is_my_sign(5, 8)
"Leo"
>>> what_is_my_sign(29, 1)
"Aquarius"
>>> what_is_my_sign(30, 6)
"Cancer"
>>> what_is_my_sign(31, 5)
"Gemini"
>>> what_is_my_sign(2, 2)
"Aquarius"
>>> what_is_my_sign(8, 5)
"Taurus"
>>> what_is_my_sign(9, 1)
"Capricorn"
```

