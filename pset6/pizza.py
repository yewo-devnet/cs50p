import sys
import csv
import tabulate

def main():
    n = len(sys.argv)
    table = []


    if n > 2:
        print("Too many command arguments")
        sys.exit()
    elif n <= 1:
        print("Too few command-line arguments")
        sys.exit()
    else:
        _ , x = sys.argv[1].rsplit('.') 
        if x != "csv":
            print("Not a csv file")
            sys.exit()

    try:
        with open("x" , "r") as file:
            reader = csv.reader(file)
            print(reader)

            # for row in reader:
            #     list1.append(row[0])
            #     list2.append(row[1])
            #     list3.append(row[2])


        #open the csv file 
        #format the table using grid format 
    except Exception as e:
        print(e)
    
    

if __name__ == "__main__":
    main()