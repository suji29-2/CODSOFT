history = []

while True:
    print("\n1.Calculate")
    print("2.View History")
    print("3.Exit")

    choice = input("Choice: ")

    if choice == "1":
        a = float(input("First Number: "))
        op = input("Operation (+,-,*,/,%,^): ")
        b = float(input("Second Number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        elif op == "%":
            result = (a / b) * 100
        elif op == "^":
            result = a ** b
        else:
            print("Invalid")
            continue

        print("Result:", result)
        history.append(f"{a} {op} {b} = {result}")

    elif choice == "2":
        for item in history:
            print(item)

    elif choice == "3":
        break