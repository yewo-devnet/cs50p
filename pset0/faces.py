def main():

    prompt = input("enter a message: ")
   
    print(convert(prompt))

def convert(p):
   
    mp = p.replace(":(", "🙁")
    mp = p.replace(":)", "🙂")
    #why is the second replace not working

    return mp

if __name__ == "__main__":
    main()