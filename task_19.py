def calc():
    try:
        x = float(input("Number 1: "))
        y = float(input("Number 2: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    try:
        print("Answer:", x / y)
    except ZeroDivisionError:
        print("Second number cannot be zero.")


def item():
    values = [5, 15, 25]

    try:
        pos = int(input("Position: "))
        print(values[pos])
    except ValueError:
        print("Enter a valid number.")
    except IndexError:
        print("Position not available.")


def info():
    user = {"id": 101, "name": "Sam"}

    try:
        k = input("Field: ")
        print(user[k])
    except KeyError:
        print("Field does not exist.")


def text():
    try:
        with open("data.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File was not found.")
    else:
        print("Reading completed.")
    finally:
        print("Done.")


def whole():
    try:
        n = int(input("Enter an integer: "))
        print("Value:", n)
    except ValueError:
        print("Invalid integer.")


while True:
    print("\n1. Division")
    print("2. List")
    print("3. Dictionary")
    print("4. File")
    print("5. Integer")
    print("6. Exit")

    c = input("Choice: ")

    if c == "1":
        calc()
    elif c == "2":
        item()
    elif c == "3":
        info()
    elif c == "4":
        text()
    elif c == "5":
        whole()
    elif c == "6":
        break
    else:
        print("Wrong choice.")
