# Scope & Number Guessing Game

**keyconcept** : scope ใน python จะมีความต่างจากภาษาอื่นๆ จาก code

```python
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

สิ่งที่เราคิดกันทั่วๆไป ผลลัพท์ที่ได้มันน่าาจะแสดง 2 ทั้งคู่ แต่เหมือนในส่วนของ python จะมีการ scope การทำงานภายใน *function หรือก็คือจะไม่สามารถ assign value ไปที่ตัวแปลที่อยู่นอก function ได้* 

```powershell
enemies inside function : 2
enemies Outside function : 1

```

และถ้าเราพยายามจะแก้ไข หรือก็คือการอัพเดต value โดยการ ref ไปที่ global variable เช่น ``enemies += 2`` program ก็เจอ error ทันที

```powershell
UnboundLocalError: local variable 'enemies' referenced before assignment
```

