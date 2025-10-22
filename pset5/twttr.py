def main():

    print(shorten(input("Input: ")))

def shorten(word):
    vowels = "AEIOU"
    for i in word:
        for j in vowels:
            if i == j:
                word = word.replace(i, "")
            else
                return ValueError()
    return word

if __name__ == "__main__":
    main()

