product = str(input())
fruit_or_vegetable = ""

if ((product == "banana")
    or (product == "apple")
    or (product == "kiwi")
    or (product == "cherry")
    or (product == "lemon")
    or product == "grapes"):
    fruit_or_vegetable = "fruit"
elif ((product == "tomato")
      or (product == "cucumber")
      or (product == "pepper")
      or (product == "carrot")):
    fruit_or_vegetable = "vegetable"
else:
    fruit_or_vegetable = "unknown"

print(fruit_or_vegetable)