# Getting Started
## Using python shell
  - Open terminal (ctrl+alt+t). 
  - Type:
```sh 
$ python
``` 
- If you have python 3 then type:
```sh
$ python3
``` 
 This will open python shell in your terminal.  
 
```sh
>>>
```

Lets tryout a simple python code to print  "Unlock the world of security",  all you need is to use print function.

- open terminal and type: 

```sh 
$ python3
>>> print("Unlock the world of security")
``` 
- In case of python 2 the above syntax will also work along with the following syntax :
```sh
$ python
>>> print "Unlock the world of security" 
``` 
The output will be displayed in the python shell as: 
```sh
>>> Unlock the world of security
``` 

## Basic Data Types
- Integer       eg: -4, 0, 32 
- Float         eg: -44.3, 0.55, 7.0
- Complex       eg: 3+2i, 4-i, -2-3i
- Boolean       true or false
- String        eg: 'Smile', '44', 'disc0ver'

> To check the datatype, python has built in function type().

```sh
>>> n=1729
>>>type(n)
<class 'int'>
>>>s="H4cker"
>>>type(s)
<class 'str'>
>>>f=17.29
>>>type(f)
<class 'float'>
```
Convertion to a valid datatype is possible with the help of typecasting.

```sh
>>>f=212.34
>>>int(f)
212
>>>num=33
>>>float(num)
33.0
```

## Strings

These are set of characters closed with double or single quotes.  

string="security"

Here security is written in double quotes, hence is taken as a string.

With length as 8.

To check length, python has built-in funtion, ```len(string name)```.

```sh 
>>> string="security"
>>>len(string)
```

Press enter.
#### Output
```sh 
8
```
Index value starts from 0.

![home](string.png)

**Things to know:**

Syntax for extracting a part of the string : 

#### string_name[starting:ending:incrementation]


```sh 
>>>a='I can crack your password'
>>>len(a)
```

#### Output
```sh 
25
```
It starts from 0 to 24, thus in total 25 characters. 

```sh 
>>>a[0:24]
```
#### Output
```sh 
'I can crack your password'
```
For only the fisrt 5 characters.
```sh 
>>>a[0:5]
```
#### Output
```sh 
'I can'
```
For the 10th character.
```sh 
>>>a[10]
```
#### Output
```sh 
'k'
```
To Extract the characters at even indices.

To include the last character, we need to specify the ending point as 25.

```sh 
>>>a[0:25:2]
```

#### Output
```sh 
'Icncakyu asod'
```
Python has built-in funtion ```string_name.split("")```.

It will split the string into substrings when it encounters the character in quotations.
If nothing is specifed in the quotes, then it will dispaly error.

Example 1 

If we want to separate the string into subtrings, when there is a space:

```sh 
>>>a.split(" ")
```
It will give us a list with the substrings which are separated by what is specified in quotations (here split(" ") i.e. space).
#### Output
```sh 
['I', 'can', 'crack', 'your', 'password']
```
Example 2

```sh 
>>>new='safe, secure, security'
>>>new.split(",")
```
#### Output

```sh 
['safe', ' secure', ' security']
```
