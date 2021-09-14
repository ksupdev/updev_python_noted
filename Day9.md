# Dictionaries & Nesting

## Concept
- It like table (key,value)
- syntax ''{key: Value}'' 

```python
programming_language = {
  "web":"php,jvascript",
  "api":"java,golang",
  "database":"Mysql,sqlserver"
  }

# access data in dictionary
print(programming_language)
print(programming_language["web"])

#empty dictionary
empty_dictionary = {}

#Edit an item in a dictionary
programming_language["database"] = "progress"
print(programming_language)

#Loop through a dictionary
for key in programming_language:
  # print keys
  print(key)
  # access value with Key
  print(programming_language[key])
```

## Grading Program Exercise

```python
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
```

## Nesting Lists 

### Concept
```python
{ 
  Key: [List],
  Key2: {Dict},
```
