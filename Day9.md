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
 }
 
 ##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# travel_log['France'][0] = "Thai"
# print(f"{travel_log['France'][0]}")
# print(f"{travel_log}")

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}



# #Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
```

## Exercise Dictionary in List

```python
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, time_visited, cities_visited):
  # create dictionaries temp
  country_dict = {}
  country_dict["country"] = country_visited
  country_dict["visits"] = time_visited
  country_dict["cities"] = cities_visited
  travel_log.append(country_dict)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

```

## Bid auction-start (updev)

```python
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bid_list = [ ]

have_other_bidder = "yes"
while(have_other_bidder == "yes"):
  bid_dict = {}
  bidder_name = str(input("What is your name?: "))
  bid = float(input("What's your bid?: "))
  bid_dict[bidder_name] = bid
  bid_list.append(bid_dict)

  have_other_bidder = str(input("Are there any other bidder? Type 'yes' or 'no'"))
  clear()


temp_high_bid = {}
for bid in bid_list:
  if temp_high_bid == {}:
    temp_high_bid = bid
  else:
    current_score = list(temp_high_bid.values())[0]
    new_score = list(bid.values())[0]
    if new_score > current_score:
      temp_high_bid = bid

print(temp_high_bid)

```

## Bid auction-start (udemy)

```python
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, time_visited, cities_visited):
  # create dictionaries temp
  country_dict = {}
  country_dict["country"] = country_visited
  country_dict["visits"] = time_visited
  country_dict["cities"] = cities_visited
  travel_log.append(country_dict)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
```


