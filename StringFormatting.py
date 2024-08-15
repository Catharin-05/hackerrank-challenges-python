def print_formatted(number):
    
    for i in range(1,number+1):
        width = len(bin(number)[2:])
        string = str(i).rjust(width)
        Octal = oct(i)[2:].rjust(width)
        Hexadecimal =  hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(string,Octal,Hexadecimal,binary)
    


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
