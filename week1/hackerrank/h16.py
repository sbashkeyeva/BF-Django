if __name__ == '__main__':
    s = raw_input()
    if any(word.isalnum() for word in s ):
        print('True')
    else:
        print('False')
    if any(word.isalpha() for word in s):
        print('True')
    else:
        print('False')
    if any(word.isdigit() for word in s):
        print('True')
    else:
        print('False')
    if any(word.islower() for word in s):
        print('True')
    else:
        print('False')
    if any(word.isupper() for word in s):
        print('True')
    else:
        print('False')