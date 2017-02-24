def sum_to(n):
    if (n == 1):
        return(1)
    return(sum_to(n-1)+n)

n = 10
print('Tong',n,'so =',sum_to(n))
