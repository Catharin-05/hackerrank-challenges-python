def split_and_join(line):
    # Splitting the line and storing it in a list
    line_list = line.split(" ")
    # Defining the seperator and joining the list into sentences 
    seperator = '-'
    return seperator.join(line_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
