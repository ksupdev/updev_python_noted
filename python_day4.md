## Who wil pay the bill?

```python
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
randome_who_pay = random.randint(0,len(names)-1)
print(f"{names[randome_who_pay]} is going to buy the meal today!")
```
