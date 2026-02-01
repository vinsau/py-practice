def reverse(s):
    return s[::-1]

def is_palindrome(s):
    s_clean = s.lower().replace(" ", "")
    return s_clean == s_clean[::-1]

    