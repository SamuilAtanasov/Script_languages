import re  #it used for cleaning text, validation, extraction and replacement
def is_palindrome(text):
    cleaned = re.sub(r'[^a-zA-Z0-9]','', text.lower())
    return cleaned == cleaned[::-1]
user_input = input("Enter a word or phrase:")
if is_palindrome(user_input):
    print("Yes")
else:
    print("No")