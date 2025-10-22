def main():

    try:
        print(f"{get_percent()}%")

    except (ValueError, ZeroDivisionError):
        get_percent()
        print(f"{get_percent()}%")

def get_percent():
        variables = input("enter a fraction: ")
        x, y = variables.split('/')
        x = int(x)
        y = int(y)
        val = round((x/y) * 100)
        if val <= 1:
            val = 'E'
        elif val >= 99:
            val = 'F'
        return f"{val}"


if __name__ == "__main__":
    main()