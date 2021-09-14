# Day 8 - Beginner - Function Parameters & Caesar Cipher

## Simple caesar

```python
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# alphabet.append(alphabet.pop(0))
# print(alphabet)

def encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
      cipher_text += alphabet[alphabet.index(char) + shift]
    return cipher_text

def decode(plain_text, shift_amount):
    alphabet_shift = alphabet[shift_amount:]+alphabet[:shift_amount]
    result = ""
    for char in plain_text:
      result += alphabet[alphabet_shift.index(char)]
    return result

def encrypt_updev(plain_text, shift):
    alphabet_shift = alphabet[shift:]+alphabet[:shift]
    result = ""
    for char in plain_text:
      result += alphabet_shift[alphabet.index(char)]
    return result

def ceasar(plain_text,shift, direction):
  alphabet_key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  alphabet_source = []
  alphabet_target = []
  if direction == "encode":
    alphabet_source = alphabet_key
    alphabet_target = alphabet_key[shift:]+alphabet_key[:shift]
  else:
    alphabet_target = alphabet_key
    alphabet_source = alphabet_key[shift:]+alphabet_key[:shift]
  
  print(alphabet_source)
  print(alphabet_target)
  
  result = ""
  for char in plain_text:
    result += alphabet_target[alphabet_source.index(char)]
  
  return result
  

run_again = "yes"

print(logo)

while run_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  print(f"The {direction} text is {ceasar(text,shift,direction)}")
  run_again = str(input("Type 'yes' if you want to go again. Otherwise type 'no':\n"))


# result = encrypt("hello", 5)
# result_updev = encrypt_updev("zulu", 5)
# print(f"The encoded text is {result}")
# print(f"The encoded text is {result_updev}")
```

## Udemy way

```python
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# alphabet.append(alphabet.pop(0))
# print(alphabet)

def encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
      cipher_text += alphabet[alphabet.index(char) + shift]
    return cipher_text

def decode(plain_text, shift_amount):
    alphabet_shift = alphabet[shift_amount:]+alphabet[:shift_amount]
    result = ""
    for char in plain_text:
      result += alphabet[alphabet_shift.index(char)]
    return result

def encrypt_updev(plain_text, shift):
    alphabet_shift = alphabet[shift:]+alphabet[:shift]
    result = ""
    for char in plain_text:
      result += alphabet_shift[alphabet.index(char)]
    return result

def ceasar(plain_text,shift, direction):
  alphabet_key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  shift = shift % len(alphabet_key)
  print(shift)
  # if direction == "encode":
  #   alphabet_source = alphabet_key
  #   alphabet_target = alphabet_key[shift:]+alphabet_key[:shift]
  # else:
  #   alphabet_target = alphabet_key
  #   alphabet_source = alphabet_key[shift:]+alphabet_key[:shift]
  
  # print(alphabet_source)
  # print(alphabet_target)

  if direction == "decode":
    shift *= -1
  
  result = ""
  for char in plain_text:
    if char in alphabet_key:
      # result += alphabet_target[alphabet_source.index(char)]
      result += alphabet_key[alphabet_key.index(char) + shift]
    else:
      result += char
  
  return result
  

run_again = "yes"

print(logo)

while run_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  print(f"The {direction} text is {ceasar(text,shift,direction)}")
  run_again = str(input("Type 'yes' if you want to go again. Otherwise type 'no':\n"))






# result = encrypt("hello", 5)
# result_updev = encrypt_updev("zulu", 5)
# print(f"The encoded text is {result}")
# print(f"The encoded text is {result_updev}")
```
