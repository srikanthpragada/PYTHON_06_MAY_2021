try:
    num = int(input("Enter a number :"))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except Exception as ex:
    print('Error :', ex)

print("The End!")