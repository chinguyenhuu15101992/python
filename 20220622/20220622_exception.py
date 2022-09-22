# num = 0
#
# while True:
#     if num==5:
#         break
#     print(num,'Hello world')
#     num=num+1



while True:
    try:
        x=int(input("Nhập số X: "))
        print("Số bạn đã nhập là: ",x)
        break
    except ValueError:
        print("Lỗi, hãy nhập lại số")