def main():
    print(value(input("Greeting: ").lower()))


def value(greeting):
    if greeting.find("hello") == 0 :
        return 0
    elif greeting.find("h") == 0:
        return 20 
    else:
        return 100
    
if __name__ == "__main__":
    main()