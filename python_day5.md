# Average Height

```python
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
count_num_of_student = 0
sum_number = 0

for student in student_heights:
  count_num_of_student += 1
  sum_number += student
  
avg = sum_number/count_num_of_student
print(f' {sum_number} / {count_num_of_student} = {avg}')
```

# Day 5.2 Highest Score

```python

# 🚨 Don't change the code below 👇
#student_scores = input("Input a list of student scores ").split()
student_scores = "78 65 89 86 55 91 64 89".split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_value = 0
for student in student_scores:
  if max_value < student:
    max_value = student

print(f"The highest score in the class is: {max_value}")
```

# Day 5.3 Repit

```python
#Write your code below this row 👇
sum = 0
for number in range(2,101,2):
  sum += number

print(f"{sum}")
```

# Day 5.4 FizzBuzz

```python
for number in range(1,101):
  if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(f'{number}')
```

# Day 5.5 Create a Password Generator

```python
#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_letters = 4
# nr_symbols = 2
# nr_numbers = 2


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for num in range(0,nr_letters):
  password += str(letters[random.randint(0,nr_letters-1)])

for num in range(0,nr_symbols):
  # password += str(symbols[random.randint(0,nr_symbols-1)])
  password += str(random.choice(symbols))

for num in range(0,nr_numbers):
  password += str(numbers[random.randint(0,nr_numbers-1)] )

print(f"Your basic pass : {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Manual ways

adv_pass = ""
password_list = list(password)
for value in range(0, len(password_list)):
  random_val = random.randint(0,len(password_list)-1)
  adv_pass += str(password_list.pop(random_val))

print(f"Your advance pass : {adv_pass}")


# Esy ways
password_list_v2= list(password)
random.shuffle(password_list_v2)

password_v2 = ""
for char in password_list_v2:
  password_v2 += char

print(f"Your advance pass v2 : { password_v2 }")



```


