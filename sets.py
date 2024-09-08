def average(array):
    # your code goes here
    disctinct_plant_heights = set(array)
    return sum(disctinct_plant_heights)/len(disctinct_plant_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
