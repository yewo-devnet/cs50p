import random 

def main():
    pass

def get_level():
    level = input("Enter level: ")
    while level not in [1,2,3]:
        level = input("Enter level: ")
    return level

def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    if level == 1:
        integer =random.random(1, 10)
    elif level ==2:
        random.random(1, 100)
    else:
        random,random(1, 1000)
    pass

if __name__ == "__main__":
    main()