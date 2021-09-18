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


