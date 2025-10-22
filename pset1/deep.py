def main():
    answer = input("What is the answer to great question of Life, the Universe, and Everything?").strip()

    if answer.lower() == "forty-two" or answer.lower() == "forty two" or answer == "42":
        print("Yes")

    else:
        print("No")

if __name__ == "__main__":
    main()