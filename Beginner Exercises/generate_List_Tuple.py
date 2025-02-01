#Generate a list and tuple with comma-separated numbers
value = input ("Enter some values seperated by comma , ")
list = value.split(",")
tuple = tuple(list)
print("List:", list)
print("Tuple:", tuple)
