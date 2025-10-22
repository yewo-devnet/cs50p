import inflect

def main():
    p = inflect.engine()
    list = []
    while True:
        try:
            list.append(input("Input: "))

        except EOFError:
            print(list)
            print(p.join(list))
            break

if __name__ == "__main__":
    main()