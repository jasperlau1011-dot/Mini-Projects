school = ['12', 'you', 'ase']
school_1 = {'profile' : 12, 'user' : 14}
for key, value in school_1.items():
    print(key)
    print(value)
import random
import string
random.choice(string.ascii_lowercase)
import random
weathers = {"raining" : '1', "clear": "2", "sunny": "3"}
weathers[0] = '8'
print(weathers[0])
print(weathers)
for key, value in weathers.items():
    if key == "raining":
        print(key + value)
    else:
        pass
weather_roll = random.randint(1, 6)
my_dict = {'a': 10, 'b': 20, 'c': 30}
my_var = 20
if my_var in my_dict.values():
    print(f"Yes, {my_var} is a value in the dictionary!")
def greet():
    print("hello")
def pers_name(name):
    print(f"hello {name}.")
pers_name("alice")
def numbers(a, b):
    return a + b
result = numbers(3, 9)
print(result)
name = input("what is your name?")
count = 0
while name == "" and count == 0 or "-" in name and count == 0:
    print("incomplete statement.")
    count = count + 1
print("statement complete")

list_1 = {"pe": 1, "tung" : 2, "SE" : 3}
list_2 = {"see" : 4, "pes" : 5, "po" : 6}
list_total = [list_1, list_2]
print(list_total)
for lists in list_total:
    print(lists)
    
flav = {"chocolate" : 1, "vanilla" : 2, "mango" : 3}
for keysss in flav.keys():
    print(keysss)
index = 0
item = "apples"

print(index, item)
# Output: 0 apples
#          ^ Python automatically added this space
list_67 = {"te" : ["pee", "siu"], "pos" : [12, 13]}
for value in list_67.values():
    print(value)
    print(value[:1])
    print(value[1:])
    print(value[1:2])
dictionary = {"ealbert" : {"first" : "albert", "last" : "einstein"}, "jepstein" : {"first" : "jefferey", "last" : "epstein"}}
for name, dictionaries in dictionary.items():
    print(f"hello {name}")
    print("full-name:\nfirst name: " + dictionaries["first"] + "\nlast name: " + dictionaries["last"])
prompt = "hello"
prompt += "whats your name?"
name_1212 = input(prompt)
print(f'hello {name_1212}')
print(4%3) # enters remainder
number = [12, 13]
for numbers in number:
    if numbers % 2 == 0:
        print("even")
    else:
        print("odd")
prompt = "enter something and i will repeat. enter 'quit' to proceed to next program"
message = ""
while message != "quit":
    message = input(prompt)
    
    if message != "quit":
        print(message)
active = True
while active:
    message = input("i will repeat what you say")
    
    if message == 'quit':
        active = False
    else:
        print(message)
while True:
    message = input("i will repeat your response")
    if message == "quit":
        break
    else:
        print(message)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 4:
        break  # Stops the loop completely when num is 4
    print(num)

print("Loop finished!")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue  # Skips printing 3 and moves to 4
    print(num)

print("Loop finished!")
text = "   \n Hello World!   \t "
cleaned = text.strip()

print(f"Original: '{text}'")
print(f"Cleaned:  '{cleaned}'")#removes white space
text = "...,,xz..Hello World!..zx,,"
cleaned = text.strip(".,xz")#removes specific characters (individual characters)

print(cleaned)
text = "   Hello World!   "

print(f"'{text.lstrip()}'")  # Output: 'Hello World!   ' removes left side
print(f"'{text.rstrip()}'")  # Output: '   Hello World!' removes other side
# 1. Define the blueprint using the class keyword
class Dog:
    # The constructor to initialize each dog's unique traits
    def __init__(self, name, breed):
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute

    # A method defining a behavior
    def bark(self):
        return f"{self.name} says Woof!"

# 2. Create concrete "objects" (instances) from the blueprint
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "French Bulldog")

# 3. Access data and behaviors
print(dog1.name)  # Output: Buddy
print(dog2.bark()) # Output: Luna says Woof!
# 1. Define the blueprint
class Character:
    # Set up the initial stats for any new character
    def __init__(self, name, role):
        self.name = name      # Character's name
        self.role = role      # e.g., Warrior, Mage, Rogue
        self.health = 100     # Every character starts with 100 health

    # Action: Take damage from an enemy
    def take_damage(self, amount):
        self.health -= amount
        return f"{self.name} took {amount} damage! Health is now {self.health}."

    # Action: Heal back some life
    def drink_potion(self):
        self.health += 20
        return f"{self.name} drank a potion. Health is now {self.health}."

# 2. Create two separate character variables
hero1 = Character("Arthur", "Warrior")
hero2 = Character("Zelda", "Mage")

# 3. Play the game (run actions)
print(hero1.take_damage(30))  # Output: Arthur took 30 damage! Health is now 70.
print(hero2.take_damage(15))  # Output: Zelda took 15 damage! Health is now 85.
print(hero1.drink_potion())   # Output: Arthur drank a potion. Health is now 90.
class Car:
    def __init__(self, brand):
        self.brand = brand  # self saves the brand to this specific car instance

    def drive(self):
        print(f"The {self.brand} is driving!")

# 1. Create an instance of the class
my_car = Car(input("enter car brand"))

# 2. Call a method
my_car.drive()
foods = {"bread" : 2, "sea" : 3}
foods["bread"] = 3
for food, amount in foods.items():
    print(food + " " + str(amount))

def foods(type_bread, amount):
    for breads in type_bread:
        print("i eat " + str(amount) + " " + breads)
foods("ty", 12)

def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton', feild = 's')
print(user_profile)

def print_scores(name, *scores):
    print(name)
    print(scores)  # Tuple of extra positional arguments

print_scores("Alice", 90, 85, 95)
# Output: Alice, (90, 85, 95)
    

def configure_server(**settings):
    print(settings)  # Dictionary of extra keyword arguments

configure_server(host="localhost", port=8080)
# Output: {'host': 'localhost', 'port': 8080}


    
    


        


