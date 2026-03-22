class Student:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender, school):
        # name, age, gender, school là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender
        self.school = school

    # Phương thức để hiển thị thông tin
    def __str__(self): # để sử dụng print()
        return f'{self.name} - {self.age} tuổi - {self.gender} - {self.school}'
    
    def display_info(self):
        print('========== THÔNG TIN ==========')
        print(f'Tên: {self.name}')
        print(f'Tuổi: {self.age}')
        print(f'Giới tính: {self.gender}')
        print(f'Trường: {self.school}') 
        print('==============================')

    # Phương thức cập nhật thông tin
        # Cập nhật tuổi (tự nhập thông tin)
    def edit_age(self):
        new_age = int(input('Nhập tuổi mới: '))
        if new_age > 0:
            # Cập nhật tuổi vào thuộc tính age
            self.age = new_age
            print('Cập nhật tuổi thành công!')
        else:
            print('Tuổi không hợp lệ. Vui lòng nhập lại.')

        # Cập nhật trường học (truyền tham số)
    def edit_school(self, new_school):
        # strip(): loại bỏ khoảng trắng thừa ở đầu và cuối 
        if new_school.strip() == '':
            print('Tên trường không hợp lệ!')
        else:
            # Cập nhật tên trường vào thuộc tính school
            self.school = new_school
            print('Cập nhật trường học thành công!')

# Tạo đối tượng Student
stu1 = Student('Trí Thành', 12, 'male', 'Vinschool')

# Hiển thị thông tin
print(stu1) # sử dụng phương thức __str__()
stu1.display_info()

# Cập nhật tuổi
stu1.edit_age()

# Cập nhật trường học
stu1.edit_school('TH School')

stu1.display_info()