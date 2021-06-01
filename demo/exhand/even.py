data = input("Enter a number :")
if not data.isdigit():
    print("Sorry! Invalid number!")
    exit()

num = int(data)
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
