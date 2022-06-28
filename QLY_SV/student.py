class Student:
    count=0

    def __init__(self,id,name, sex, age, diemToan, diemLy, diemHoa):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.diemToan = diemToan
        self.diemLy = diemLy
        self.diemHoa = diemHoa
        self.diemTB = 0
        self.hocLuc = ""
        Student.count +=1
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_Name(self,name):
        self.name = name
    def get_Name(self):
        return self.name
    def show_info(self):
        # print(f"\n Thông tin Sinh Viên: ")
        print(f"\nId: {self.get_id()}")
        print(f"Tên SV: {self.name}")
    def showSinhVien(self, listSV):
        # hien thi tieu de cot
        print("{:<8} {:<18}".format("ID", "Name"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18}".format(sv._id, sv._name))
        print("\n")
    def getListSinhVien(self):
        return self.listSinhVien
sv=Student("sv01", "Sinh Vien 1")
sv1=Student("sv02", "Sinh Vien 2")
sv.show_info()
print(sv.count)
sv.get_Name()