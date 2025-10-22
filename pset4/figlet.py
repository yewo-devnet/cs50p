import sys
import pyfiglet

def main():
    num_of_args = len(sys.argv)
    text = input("Input: ")
    if num_of_args == 1:
        f =pyfiglet.figlet_format(text)
        print("Output")
        print(f)
        with open("eric.txt", "w") as file:
            file.write(f)
    elif sys.argv[1] == '-f' or sys.argv[1] == '--font':
        f =pyfiglet.figlet_format(text, font=sys.argv[2])
        print("Output")
        print(f)

if __name__ == "__main__":
    main()