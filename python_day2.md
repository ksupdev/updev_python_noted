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
