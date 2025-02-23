deep = input("? ")

match deep:
    case "42" | "Forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")