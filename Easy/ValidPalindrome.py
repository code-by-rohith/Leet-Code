
def isPalindrome(s: str) -> bool:
        c = ""

        for word in s:
            if word.isalnum():
                c += word

        if c.lower() == c[::-1].lower():
            return True

        return False

print(isPalindrome("malayalam"))