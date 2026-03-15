import oop

human1 = oop.Human('Nhật Minh', 12, 'male')
stu1 = oop.Student('Đức Anh', 11, 'male', 'TH Minh Khai')
stu2 = oop.Student('Hoàng Anh', 13, 'female', 'MindX')

# Sử dụng phương thức của lớp cha (Human)
human1.introduce()
stu1.introduce()
# Sử dụng phương thức __str__
print(stu2)
# Sử dụng phương thức show_info
stu2.show_info()

# Sử dụng phương thức chỉnh sửa thông tin
stu2.edit_age()
stu2.edit_school('mindx technology school')
# Hiển thị lại thông tin sau khi chỉnh sửa
stu2.show_info()

# Đề bài luyện tập:
# Tạo class Animal gồm các thuộc tính: tên, loài
# Viết 2 phương thức cho class Animal

# Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
# Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
# Viết 1 phương thức mới cho class Dog

# Yêu cầu:
# - Tạo class ở file oop.py
# - Viết chương trình test tại file main.py