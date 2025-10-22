import sys

def main():

    n = len(sys.argv)

    if n > 2:
        print("Too many command arguments")
        sys.exit()
    elif n <= 1:
        print("Too few command-line arguments")
        sys.exit()
    elif sys.argv[1].rsplit('.') == "py":
        print("Not a python file")
        sys.exit()

    #get the path of the file 
    count = 0
    try:
        with open(f"{sys.argv[1]}", "r") as file:
            for line in file:
                count = count + 1
                if line.startswith('#') or line.strip() == "":
                    count = count - 1
                
            print(f"Lines of Code = {count}")
    except Exception as e:
        print(e)
        print("File does not exist")

if __name__ == "__main__" :
    main()