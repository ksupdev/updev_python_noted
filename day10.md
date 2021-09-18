# Beginner Functions with Outputs

## Basic function and parameter and return single value

```python
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  # print(f"{formated_f_name} {formated_l_name}")
  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("kaRoon","Sillapapan")
print(formated_string)
```

## Return multiple values

```python
#Functioln with Outputs

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."

  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  # print(f"{formated_f_name} {formated_l_name}")
  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name(
  input("What is your first name? :"),
  input("What is your last name? :"))
 
print(formated_string)  

```

## Days in Month Exercies

### UPDEV solution
```python
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if isinstance(year, int) and isinstance(month, int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
      return "29"
    return f"{month_days[month-1]}"
  else:
    return "Please check your argument, support int only"
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```
### Udemy

```python
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "Invarid month"

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return "29"
  return f"{month_days[month-1]}"
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

## Docstrings

- ``""" Function info """``

```python
def format_name(f_name, l_name):
  """Take a first and last name and format it to return the title case version of the name."""
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  # print(f"{formated_f_name} {formated_l_name}")
  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("kaRoon","Sillapapan")
print(formated_string)
```

## Calculator

```python
# from art import logo
# print(logo)
# Calculator

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Devide
def devide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : devide }

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operation in operations:
  print(operation)
  # print(f"{operations[operation](num1,num2)}")
operation_symbo = input("Pick an operation from the line above: ")

answer = operations[operation_symbo](num1,num2)
print(f"{num1} {operation_symbo} {num2} = {answer}")

```

## Calculatir

```python
from art import logo

# Calculator

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Devide
def devide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : devide }

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)

  should_continue = True

  while should_continue:
    operation_symbo = input("Pick an operation : ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbo]
    
    anwser = calculation_function(num1,num2)
    print(f"{num1} {operation_symbo} {num2} = {anwser}")
    
    if input(f"Type 'y' to continue calculating with {anwser} or type 'n' to exit: ") == 'n':
      should_continue = False
      calculator()
    else:
      num1 = anwser
      

calculator()

```

