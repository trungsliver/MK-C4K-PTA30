# Tính chất kế thừa
class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức giới thiệu bản thân
    def introduce (self):
        print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi.')

# Lớp Student kế thừa từ lớp Human
class Student(Human):
    # Hàm khởi tọa giá trị
    def __init__(self, name, age, gender, school):
        # Gọi hàm khởi tạo từ lớp cha (Human)
        super().__init__(name, age, gender)
        # Thuộc tính riêng của lớp Student
        self.school = school

    # Ghi đè (override) phương thức của lớp cha
    def introduce(self):
        print(f'Tôi tên là {self.name}, học tại {self.school}.')

    # Phương thức có sẵn (để dùng print)
    def __str__ (self):
        return f'{self.name} - {self.age} tuổi - {self.gender} - {self.school}'
    
    # Phương thức hiển thị thông tin
    def show_info(self):
        print(f'''
========== THÔNG TIN ==========
Họ tên:         {self.name}
Tuổi:           {self.age}
Giới tính:      {self.gender}
Trường học:     {self.school}
===============================''')
        
    # Phương thức chỉnh sửa thông tin
        # Chỉnh sửa tuổi (tự nhập)
    def edit_age(self):
        new_age = int(input('Nhập tuổi mới: '))
        if new_age <= 0:
            print('Tuổi không hợp lệ!')
        else:
            # cập nhật tuổi mới vào thuộc tính age
            self.age = new_age
            print(f'Tuổi của {self.name} đã được cập nhật.')

        # Chỉnh sửa trường học (truyền tham số)
    def edit_school(self, new_school):
        if new_school.strip() == '':
            print('Tên trường không hợp lệ!')
        else:
            # Viết hoa chữ cái đầu của mỗi từ trong tên trường
            new_school = new_school.strip().title()
            # cập nhật trường học mới vào thuộc tính school
            self.school = new_school
            print(f'Trường học của {self.name} đã được cập nhật.')