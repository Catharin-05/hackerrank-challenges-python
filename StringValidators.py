if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s)) # checks if s has any alphanumeric characters
    print(any(i.isalpha() for i in s)) # checks if s has any alphabetical characters
    print(any(i.isdigit() for i in s)) # checks if s has any numbers
    print(any(i.islower() for i in s)) # checks if s has any lower case character
    print(any(i.isupper() for i in s)) # checks if s has any upper case character
