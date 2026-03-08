# Khai báo đối tượng tổng quát
class Animal:
    # Hàm khởi tạo
    def __init__ (self, name, species, age, color):
        # name, species, age, color là thuộc tính
        self.name = name
        self.species = species
        self.age = age
        self.color = color

    # Phương thức - hành động
    # Phương thức ăn
    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    # Phương thức hiển thị thông tin
        # Phương thức có sẵn (dùng được print)
    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.color} {self.species}."
    
        # Phương thức không có sẵn
    def show_info (self):
        print(f'''
========== THÔNG TIN ==========
Species: {self.species}
Name: {self.name}
Age: {self.age}
Color: {self.color}
================================''')