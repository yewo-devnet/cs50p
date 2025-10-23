import sys

def main():
    n = len(sys.argv)

    if n > 2:
        print("Too many command arguments")
        sys.exit()
    elif n <= 1:
        print("Too few command-line arguments")
        sys.exit()
    elif sys.argv[1].rsplit('.') == "csv":
        print("Not a csv file")
        sys.exit()

    


    try:
        pass
        #open the csv file 
        #format the table using grid format 
    except Exception as e:
        print(e)
    
    

if __name__ == "__main__":
    main()