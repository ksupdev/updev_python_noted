# Robot walk

> you can test with https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

```python

 
# Found free space if current locate = 2
def turn_aroud_3():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_aroud_3()
    move()
    turn_aroud_3()
    move()
    turn_left()
# def go_ahead():
    
def move_to() :
    while at_goal() == False:
        if wall_in_front():
            jump()
        else:
            move()
    
move_to()
```

## Hurdle 4
> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

```python

 
# Found free space if current locate = 2
def turn_aroud_3():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    
    while wall_on_right():
        move()
    
    turn_aroud_3()
    move()
    turn_aroud_3()
    #turn_left()
    move()
    while wall_in_front() == False:
        move()
    turn_left()
    
# def go_ahead():
    
def move_to() :
    while at_goal() == False:
        if wall_in_front():
            jump()
        else:
            move()
    
move_to()
```
