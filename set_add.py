if __name__ == '__main__':
    unique_countries = set()
    N = int(input())
    for i in range(N):
        country = input()
        unique_countries.add(country)
    print(len(unique_countries))
