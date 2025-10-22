from plates import is_valid


def main():
    test_max_length()
    test_middle()
    test_min_length()
    test_punctuation()
    test_zero()


def test_min_length():
    assert is_valid("12") == False
    assert is_valid("1") == False
    assert is_valid("") == False

def test_max_length():
    assert is_valid("qwertyu") == False
 
def test_zero():
    assert is_valid("cs05") == False

def test_middle():
    assert is_valid("cs50p") == False

def test_punctuation():
    assert is_valid("cs50.") == False
    assert is_valid("cs50 ") == False
    assert is_valid("cs50!") == False

if __name__ == "_main__":
    main()