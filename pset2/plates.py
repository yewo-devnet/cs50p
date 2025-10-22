def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    other = ['.', ' ' , '!']
    length = len(s)

    if length > 6:
        return False
    for i in s:
        if i in other or s[0] == 0 or (s[0].isalpha() and s[length - 1].isalpha()):
            return False
        
    return True
        
    

main()