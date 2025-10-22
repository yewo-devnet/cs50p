import random 

def main():
    while True:
        try:
            level = int(input("level: "))
            while not level or level < 0:
                level = input("level: ")

            rnd = random.randint(1, level)
            guess = int(input("Guess: "))
            while guess != rnd:
                if guess < rnd:
                    print("Too small")
                    guess = int(input("Guess: "))
                elif guess > rnd:
                    print("Too large")
                    guess = int(input("Guess: "))

            print("Just Right!")
            break
        except Exception:
            print("Invalid Input, Try Again")
            

if __name__ == "__main__":
    main()
   
            