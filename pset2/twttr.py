def main():
    print(shorten(input("Enter a string: "))

def shorten(input_string)
    input_string = input("Input: ")
    vowels = "AEIOU"

    for i in input_string:
        for j in vowels:
            if i == j:
                input_string = input_string.replace(i, "")

    return input_string

if __name__ == "__main__":
    main()
