# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == '__main__':
    tot_shoes = int(input())
    shoe_sizes = map(int,input().split())
    shoe_sizes = dict(Counter(shoe_sizes).items())
    income = 0
    no_of_customers = int(input())
    for i in range(no_of_customers):
        shoe_size_customer, shoe_price_customer = map(int,input().split())
        if shoe_size_customer in shoe_sizes and shoe_sizes[shoe_size_customer] > 0: 
            income += shoe_price_customer
            shoe_sizes[shoe_size_customer] -= 1
        else:
            income+=0
    print(income)  
