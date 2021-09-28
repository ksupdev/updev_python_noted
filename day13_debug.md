# Day 13 Debugging

```python
### --- error
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# -------- Fix error
from random import randint
import random
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(random.choice(dice_imgs))
print(dice_imgs[dice_num-1])
```

```python
### --- error
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# -------- Fix error
from random import randint
import random
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(random.choice(dice_imgs))
print(dice_imgs[dice_num-1])
```
