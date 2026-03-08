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
        
# Bài 2:
class Rectangle:
    # Hàm khởi tạo
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Phương thức tính chu vi
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    # Phương thức tính diện tích
    def area(self):
        return self.length * self.width
    
# Bài 3:
class BankAccount:
    # Hàm khởi tạo
    def __init__(self, account_number, owner, balance):
        # Số tài khoản
        self.account_number = account_number
        # Tên chủ tài khoản
        self.owner = owner
        # Số dư tài khoản
        self.balance = balance

    # Phương thức hiển thị số dư tài khoản
    def display_balance(self):
        print(f'''
========== SỐ DƯ TÀI KHOẢN ==========
Số tài khoản: {self.account_number}
Chủ tài khoản: {self.owner}
Số dư: ${self.balance}
=====================================
''')
        
    # Phương thức nạp tiền
    def deposit(self, amount):
        # amount: số tiền nạp vào tài khoản
        if amount > 0:
            # Cộng tiền vào số dư tài khoản
            self.balance += amount
            # Thông báo nạp tiền thành công
            print(f"Nạp thành công ${amount}!")
        else:
            # Thông báo nạp tiền thất bại
            print("Số tiền nạp vào phải lớn hơn 0.")
        # Hiển thị số dư tài khoản sau khi nạp tiền
        self.display_balance()  

    # Phương thức rút tiền
    def withdraw(self, amount):
        # amount: số tiền rút từ tài khoản
        if amount > 0 and amount <= self.balance:
            # Trừ tiền từ số dư tài khoản
            self.balance -= amount
            # Thông báo rút tiền thành công
            print(f"Rút thành công ${amount}!")
        else:
            # Thông báo rút tiền thất bại
            print("Số tiền rút không hợp lệ!")
        # Hiển thị số dư tài khoản sau khi rút tiền
        self.display_balance()