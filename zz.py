"""
2. Lists 
Ordered, flexible (can mix types). 
python 
# CopyEdit 
"""
fruits = ["apple", "banana", "cherry"] 
fruits[1]="Mango"
print(fruits[1])  # banana 
print(fruits[1])  # banana 
"""
3. Tuples 
Like lists but immutable (can't change). 
python 
CopyEdit
""" 


# colors[0] = "yellow" 
#fruits[1]="Mango"
 
is_raining = False 
print(is_raining) # <class 'bool'>

a = 10 
b = 3 
print(a + b)  # 13 
print(a - b)  # 7 
print(a * b)  # 30 
print(a / b)  # 3.333... 
print(a // b) # 3 (floor division) 
print(a % b)  # 1 (remainder) 
print(a ** b) # 1000 (exponentiation)
person = { 
"name": "Lily", 
"age": 30 
} 
print(person["name"])  # Lily 
print(person.get("age"))  # 30
print(person.get("name"))  # Lily 
print(person["age"])  # 30