bank = input("Greeting? ")

match bank:
    case "Hello" | "Hello there" | "Hello, Newman":
        print("$0")
    case _ if bank.startswith("H") or bank.startswith("h"):
        print("$20")
    case _:
        print("$100")