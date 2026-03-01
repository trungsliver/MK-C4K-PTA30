# Lập trình hướng đối tượng (OOP)
# Object Oriented Programming

# Khái niệm: là cách mô tả thế giới thực vào chương trình máy tính

# Class (lớp): Đối tượng tổng quát
# Object (đối tượng): Đối tượng cụ thể

# Ví dụ: mô phỏng Human (con người)
    # Thuộc tính (đặc điểm): tên, tuổi, giới tính, ...
    # Phương thức (hành động): ăn, ngủ, nói chuyện, ...

# Khai báo lớp đối tượng
class Human:
    # Khởi tạo giá trị (thuộc tính), đây là hàm có sẵn:
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (hành động)
    # Phương thức giới thiệu
    def introduce(self):
        print(f"Xin chào, tôi tên là {self.name}, tôi {self.age} tuổi")

    # Phương thức hiển thị thông tin (có sẵn, dùng được print)
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
    # Phương thức hát
    def sing(self, song):
        print(f"{self.name} đang hát bài {song}")

# Khởi tạo đối tượng cụ thể
human1 = Human('Hoàng Anh', 13, 'Male')
human2 = Human("Nguyên Vũ", 14, 'Unknown')

# Hiển thị thông tin
print(human1)       # chỉ hiện nơi lưu
print(human1.name)  # hiện tên

# Sử dụng phương thức
human1.introduce()
human2.introduce()
human2.sing("Baby Shark")