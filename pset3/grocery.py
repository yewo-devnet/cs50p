def main():
    try:
        groceries = {}
        val = 0
        while True:
            item = input().upper()
            if item in groceries:
                val = groceries.get(item)
                groceries[item] = val + 1
            else:
                val = 0
                groceries[item] = val + 1
            
    except (EOFError):
        for item in groceries:
            print(f"{groceries[item]} {item}")
        
if __name__ == "__main__":
    main()
