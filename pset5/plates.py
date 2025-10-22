def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    other = ['.', ' ' , '!']
    length = len(s)
    first_digit_index = 7

    if length > 6 or length <= 2:
        return False
    
    #check if the first digit is zero
    for index, char in enumerate(s):
        if char.isdigit() :
            first_digit_index = index
            if s[first_digit_index] == '0':
                return False
            else:
                break
    #check if a number is on the middle of the string
    for index, char in enumerate(s):
        if (char.isalpha() and index > first_digit_index) or  char in other:
            return False

        
    return True

if __name__ == "__main__":
    main()