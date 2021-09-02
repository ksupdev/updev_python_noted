# Data Types
## Exceisie

```python
# Input 123 ,output 1+2+3 = 6
input_val = input("Please input value : \n")
# print(type(input_val))
output_val = 0
is_err = False
for _char in input_val:
  try:
    print("input: " + _char)
    output_val = output_val+int(_char)
  except ValueError:
    is_err = True
    print('Error,please enter an integer only : '+ _char)
if is_err != True :
  print("Result : "+str(output_val))

```

## Order of process

```python

# PEMDAS
# Parentheses "()"
# Exponents "**"
# Multiplication "*"
# Division "/"
# Addition "+"
# Subtraction "-"

# PEMDASLR order of calculate
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)
# 3*3 = 9
# 3/3 = 1
# 9 + 1 = 10
# 10 - 3 = 7

print(3 * (3 + 3) / 3 - 3)
# (3 + 3) = 6
# 3 * 6 = 18
# 18 / 3 = 6
# 6 - 3 = 3
```

## BMI
```python
# BMI Calculater
input_weight = float(input("Your weight (kg) : "))
input_height = float(input("Your height (m) : "))

bmi_val = input_weight/input_height**2

print("BMI : "+str(bmi_val))
```

## F-String
```python
# f-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, your are wining is {isWinning}")
```

## Exercies Your Life in Week (90 year olds)
```python
# Create a program using maths and f-Strings that tells us how many days,weeks,months we have left if we live until 90 years old
current_age = input("Your current age : \n")
target_age = 90
remaining_age = target_age - float(current_age)

day_remaining = remaining_age * 365
weeky_remaining = remaining_age * 52
monthy_remaining = remaining_age * 12

# There are 365 days in a year, 52 weeks in a year and 12 months in year
print(f"You have {day_remaining} days, {weeky_remaining} weeks and {monthy_remaining} months left.")
```
## Project Tip Calculator

```python
print("Welcome to the tip calculator .")
bill_val = float(input("What was the total bill? : $ "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))
people = int(input("How many people to split the bil? : "))

total_bill_as_tip = (bill_val + ((bill_val*tip)/100))
bill_per_person = total_bill_as_tip/people
final_amount = round(bill_per_person,2)

print(f"Each person should pay : $ {final_amount}")
```
