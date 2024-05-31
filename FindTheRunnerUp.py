if __name__ == '__main__':
    #input
    n = int(input())
    arr = map(int, input().split())
    unique = list(set(arr))
    #sorting
    unique.sort()
    #printing the runner-up score
    print(unique[-2])
