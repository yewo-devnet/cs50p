def main():
    print(gauge(convert(input("Enter fraction: "))))

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        return round((x/y) * 100)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except ValueError:
        print("Enter a percentageid number")

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    return f"{percentage}"

if __name__ == "__main__":
    main()