
### find Odd or Even

```python
number = input("Which number do youwant to check ? \n")
if (int(number) % 2) != 0:
  print(f" {number} is Odd")
else:
  print(f" {number} is Even")
```

### Day 3.2 BMI 2.0 Exercise

```python
height = float(input("enter your height in m :"))
weight = float(input("enter your weight in kg: "))

# Under 18 thet are underweight
# Over 18.5 but below 25 they have a normal weight 18.5 - 24.9
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obses

# BMI = weight/height**2

bmi = height/(weight ** 2)
message = ""

if bmi < 18.5:
  message = "underweight"
elif bmi >= 18.5 and bmi < 25:
  message = "normal weight"
elif bmi >= 25 and bmi < 30:
  message = "overweight"
elif bmi >= 30 and bmi < 35:
  message = "obese"
else:
  # Above 35
  message = "clinically obses"


print(f"Your BMI is {round(bmi,2)}, you are {message}")
```

### Day 3.3 Leap Year Exercise

```python
year = int(input("Which year do you want to check? :"))
rule1_val = year % 4
rule2_val = year % 100
rule3_val = year % 400

if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print(f"the year {year} is a leap year")
    else:
      print(f"the year {year} is not a leap year")    
  else:
    print(f"the year {year} is a leap year")
else:
  print(f"the year {year} is not a leap year")
```
