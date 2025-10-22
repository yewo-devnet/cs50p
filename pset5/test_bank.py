from bank import value 


def main():
    test_upper()
    test_lower()
    test_numbers()

def test_upper():
    assert value("HELLO") == 0
    assert value("H") == 20
    assert value(" ") == 100
    assert value("ABC") == 100

def test_lower():
    assert value("")
    assert value("hello") == 0
    assert value("h") == 20
    assert value(" ") == 100
    assert value("abc") == 100

def test_numbers():
    assert value("1234567890") == "1234567890"

if __name__ == "__main__":
    main()