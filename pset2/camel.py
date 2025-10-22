def main():
    camel = input("camelCase: ").strip()

    for i in camel:
        if i.isupper():
            camel = camel.replace(i, f"_{i.lower()}")
    
    print(f"snake_case: {camel}")

if __name__ == "__main__":
    main()