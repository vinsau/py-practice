# test_string_utils.py
from string_utils import reverse, is_palindrome

# Test 1: Test the reverse function
def test_reverse():
    assert reverse("hello") == "ollh"
    assert reverse("abc") == "cba"
    assert reverse("") == "" # Test an edge case

# Test 2: Test the is_palindrome function
def test_is_palindrome_true():
    assert is_palindrome("radar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

# Test 3: Test the "false" case for is_palindrome
def test_is_palindrome_false():
    assert is_palindrome("hello") == False
    assert is_palindrome("pytest") == False

# Test 4: A more "Pythonic" way to test booleans
def test_is_palindrome_pythonic():
    assert is_palindrome("level") is True
    assert is_palindrome("world") is False