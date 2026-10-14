import os
from datetime import datetime
from pathlib import Path

# with open("class.json" "w") as file:
#     json.dump("Today's Class is on API")


num = [1, 2, 3, 5, 7, 4]
total = sum(num)
print(total)

# datetime
time = datetime.now()
print(time)

# pathlib
file = Path("text.txt")
print(file.exists())

try:
  age = int(input("Enter your age: "))
  print(age)
except ValueError:
  print("This is not a valid age")



user_name = os.getenv("USERNAME")
print(user_name)

# print(os.getenv("HOME"))       # Linux/Mac home folder
# print(os.getenv("USERNAME"))   # Windows username
# print(os.getenv("USER"))       # Linux/Mac username
# print(os.getenv("PATH"))       # system PATH