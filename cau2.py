n1=120
while True:
    n = int(input("Nhập số lượng cần mua vé : (0 < n <= 120): "))
    if 0 < n <= 120:
        print("đặt vé thành công")
        break
    else:
        print(" n phải lớn hơn 0 và nhỏ hơn 120. Nhập lại")

if True:
    conlai=n1-n
    print("số vé còn lại là:",conlai)
    print("số vé đã bán được là:",n)