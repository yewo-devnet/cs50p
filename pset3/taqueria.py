def main():
    d = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    try:
        val = 0
        while True:
            item = input("Item: ").title()
            if item in d:
                val = val + d[item]

    except (EOFError, KeyError):
        print(f"Total: {val}")
        
if __name__ == "__main__":
    main()