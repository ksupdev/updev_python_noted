
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

### Day 3.4 Pizza Order Exercise

```python

print("Welcome to Python Pizza Deliveries!")
size = str(input("What size pizza do you want? S,M or L :")).upper()
add_pepperoni = str(input("Do you want pepperoni? Y or N :")).upper()
extra_cheese = str(input("Do you want extra cheese? Y or N :")).upper()

# S = $15
# M = $20
# L = $25

# Pepperoni for Small pizza : +$2
# Pepperoni for Medium and Large pizza : +$3

# Extra cheese for any size pizza : + $1

ballance = 0

# Calculate bill for pizza size
if size == 'S':
  ballance = 15
elif size == 'M':
  ballance = 20
else:
  ballance = 25

# Calculate bill for add pepperoni
if add_pepperoni == "Y":
  if size == 'M' or size == 'L':
    ballance += 3
  else:
    ballance += 2

if extra_cheese == "Y":
  ballance += 1

print(f"Your final bill is : {ballance}")
```

## Day 3.5 Love Calculator

```python
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

love_score = ""
keywords = ["true", "love"]
names = (name1 + name2).lower()
keywords_score = {  "true" : 0 ,"love" : 0}

for key in keywords_score:
  score = 0
  for i, v in enumerate(key):
    _count = names.count(v)
    score += _count
  keywords_score[key] = score
  love_score += str(keywords_score[key])
  print(f"key : {key} ,value = {keywords_score[key]} , {love_score}")


if love_score != "":
  love_score_int = int(love_score)
  if love_score_int < 10 or love_score_int > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos. ")
  elif love_score_int >= 40 and love_score_int <= 50:
      print(f"Your score is {love_score}, you are alright together. ")
  else:
    print(f"Your score is {love_score}")

```
