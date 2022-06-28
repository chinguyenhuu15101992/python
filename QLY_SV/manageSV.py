from student import Student

ds=[]
while True:
    print(f'''
    0. Thoát chương trình
    1. Thêm Sinh viên
    2. Cập nhật thông tin sinh viên
    3. Xoá sinh viên
    4. Xem thông tin tất cả sinh viên
    5. Xem thông tin sinh viên
    6. Tìm sinh viên theo Tên
    7. Số lượng Sinh Viên
    ''')
    select = input(" Mời bạn chọn chức năng:  ")
    if str(select).isdigit():
        select = int(select)
        if select ==0:
            break
        elif select ==1:
            id = input("Nhập id Sinh Viên: ")
            name = input("Nhập tên Sinh viên: ")
            sv = Student(id , name)
            ds.append(sv)
            ds.sort(key=lambda ds: ds.name)
        elif select ==2:
            id = input("Nhập Id sinh viên bạn cần sửa: ")
            for i in ds:
                if i.get_id() == id:
                    print("Thông tin SV bạn chọn là:")
                    i.show_info()
                    i.set_Name(input("Mời bạn nhập tên mới: "))
                    print("Thông tin SV sau khi sửa là:")
                    i.show_info()
        elif select ==3:
            id = input("Nhập Id Sinh viên cần xoá: ")
            # if ban nhập sai ID rồi
            for i in ds:
                if i.get_id()==id:
                    ds.remove(i)
                    print("Bạn đã xoá SV thành công!!")
                    continue
                else:
                    print("Bạn nhập sau Id SV rồi, mời bạn nhập lại")
                    break
        elif select==4:
            if len(ds) ==0:
                print("\n Hiện tại, không có SV. Bạn hãy thêm sinh viên mới vào danh sách!")
            else:
                print(f"Thông tin toàn bộ các SV: Hiện có {len(ds)}")
                # #fail to show cot tieu de
                # Student.showSinhVien(ds)
                print("{:<8} {:<18}".format("ID", "Name"))
            for i in ds:
                    # i.show_info()
                print("{:<8} {:<18}".format(i.get_id(), i.get_Name()))
        elif select == 5:
            id = input("Nhập ID Sinh viên cần xem thông tin: ")
            for i in ds:
                if i.get_id() == id:
                    print(f"Thông tin SV bạn tìm là:")
                    i.show_info()
        elif select == 6:
            ten = input("\n Nhập tên Sinh viên cần xem thông tin: ")
            for i in ds:
                #chua ro tai sai fail buoc nay khi bat else len
                print("gia tri vong lap",i)
                if i.get_Name() == ten:
                    print(f"Thông tin SV bạn tìm là:")
                    i.show_info()
                    continue
                # else:
                #     print(f"\n Không có sinh viên có tên như bạn nhập: {ten}, mời bạn kiểm tra lại!!!")
                #     break
        elif select == 7:
            print(f"\nHiện có { len(ds) } Sinh Viên\n")
    else:
        print("Bạn phải nhập số. Vui lòng nhập lại")