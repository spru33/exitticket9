import matplotlib.pyplot as plt

# 1
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")

# 2
group = int(input("How many people are in your dinner group? "))
if group > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# 3
num = int(input("Enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")

# 4
while True:
    topping = input("Enter a pizza topping (or 'quit'): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")

# 5
topping = ""
while topping != 'quit':
    topping = input("(5a) Enter a topping (or 'quit'): ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

active = True
while active:
    topping = input("(5b) Enter a topping (or 'quit'): ")
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

while True:
    topping = input("(5c) Enter a topping (or 'quit'): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")

# 6
# while True:
#     print("This never ends...")

# 7
sandwich_orders = ['tuna', 'turkey', 'ham', 'veggie']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("All finished sandwiches:")
for s in finished_sandwiches:
    print(s)

# 8
responses = {}
polling = True
while polling:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place
    again = input("Would someone else like to take the poll? (yes/no) ")
    if again == 'no':
        polling = False
print("--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")

# 9
expenses = {}
expenses['Food'] = float(input("Weekly spending on Food: "))
expenses['Transportation'] = float(input("Weekly spending on Transportation: "))
expenses['Entertainment'] = float(input("Weekly spending on Entertainment: "))
plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
plt.title("Weekly Expenses")
plt.show()

# 10
study_hours = {}
study_hours['Python'] = int(input("Hours studied for Python: "))
study_hours['Math'] = int(input("Hours studied for Math: "))
study_hours['Science'] = int(input("Hours studied for Science: "))
plt.bar(study_hours.keys(), study_hours.values())
plt.title("Study Hours by Subject")
plt.xlabel("Subject")
plt.ylabel("Hours Studied")
plt.show()

# 11
temperatures = []
while True:
    temp = float(input("Enter a temperature: "))
    temperatures.append(temp)
    another = input("Enter another temperature? (yes/no) ")
    if another != 'yes':
        break
print("All temperatures:", temperatures)
print("Highest:", max(temperatures))
print("Lowest:", min(temperatures))

# 12
grades = {}
while True:
    name = input("Enter a student's name: ")
    grade = float(input(f"Enter {name}'s grade: "))
    grades[name] = grade
    more = input("Add another student? (yes/no) ")
    if more != 'yes':
        break
for name, grade in grades.items():
    print(f"{name}: {grade}")
print("Average grade:", sum(grades.values()) / len(grades))

# 13
foods = []
while True:
    food = input("Enter a favorite food: ")
    foods.append(food)
    more = input("Add another food? (yes/no) ")
    if more != 'yes':
        break
print("Your foods:", foods)
search = input("Enter a food to search for: ")
if search in foods:
    print(f"{search} is in the list.")
else:
    print(f"{search} is not in the list.")

# 14
inventory = {}
while True:
    product = input("Enter a product name: ")
    qty = int(input(f"How many units of {product}? "))
    inventory[product] = qty
    more = input("Add another product? (yes/no) ")
    if more != 'yes':
        break
for product, qty in inventory.items():
    print(f"{product}: {qty}")
print("Total units:", sum(inventory.values()))

# 15
items = []
prices = []
while True:
    item = input("Enter an item to purchase: ")
    price = float(input(f"Enter the price of {item}: "))
    items.append(item)
    prices.append(price)
    more = input("Add another item? (yes/no) ")
    if more != 'yes':
        break
for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]}")
total = sum(prices)
print(f"Total cost: ${total}")
budget = float(input("Enter your budget: "))
if total <= budget:
    print(f"Money remaining: ${budget - total}")
else:
    print(f"You are over budget by ${total - budget}")

# 16
movies = []
ratings = []
while True:
    title = input("Enter a movie title: ")
    rating = int(input("Rate it from 1 to 5: "))
    movies.append(title)
    ratings.append(rating)
    more = input("Enter another movie? (yes/no) ")
    if more != 'yes':
        break
for i in range(len(movies)):
    print(f"{movies[i]}: {ratings[i]}")
print("Highest rating:", max(ratings))