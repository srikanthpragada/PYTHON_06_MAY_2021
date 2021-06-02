a = 10
b = 0
try:
    c = a / b
    print(c)
except Exception as ex:
    print('Error :', ex)
else:
    print("Success")
finally:
    print("Over")

print("The End!")
