my_word = input('Check if word is palindrome: ')


def palindrome(word):
    return list(word) == list(word)[::-1]


if palindrome(my_word):
    print(f'Word "{my_word}" is a palindrome!')
else:
    print(f'Word "{my_word}" is not a palindrome!')
