
def tongbinhphuong(n):
    if n<2:
        return n
    else:
        return n*(n*n+1)/2
n=int(input("nhập vào số n"))
print(f"tổnrg bình phương",tongbinhphuong(n))