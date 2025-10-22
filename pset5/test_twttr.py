from twttr import shorten

def main():
    test_vowels()

def test_upper():
    assert shorten('AEIOU') == ''

def test_lower():
    assert shorten('aeiou') == ''

def test_number():
    assert shorten('1234567890') == '1234567890'

def test_():
    assert shorten('off') == 'ff'

def test_():
    assert shorten('up') == 'p'

if __name__ == "__main__":
    main()
