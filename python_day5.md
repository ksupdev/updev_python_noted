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
