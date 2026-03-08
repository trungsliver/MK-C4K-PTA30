import oop

# Khởi tạo đối tượng
a1 = oop.Animal("Lucky", "Dog", 5, "gray")
a2 = oop.Animal("Doraemon", "Cat", 10, "blue")
a3 = oop.Animal(species = "Mouse",
                name = "Jerry", 
                age = 2, 
                color = "brown")

# Hiển thị thông tin
    # Hiển thị từng thuộc tính
print(a1.species, a1.name, a1.age, a1.color)
    # Hiển thị thông tin bằng phương thức __str__
print(a2)
    # Hiển thị thông tin bằng phương thức show_info
a3.show_info()

# Gọi phương thức ăn
a1.eat("bone")
a2.eat("red bean pan-cake")
a3.eat("cheese")

# Bài 2: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
# Test ở file main.py: tạo đối tượng, tính chu vi, diện tích.
hcn1 = oop.Rectangle(5, 3)
print(f"Chu vi hình chữ nhật 1: {hcn1.perimeter()}")
print(f"Diện tích hình chữ nhật 1: {hcn1.area()}")

hc2 = oop.Rectangle(10, 4)
print(f"Chu vi hình chữ nhật 2: {hc2.perimeter()}")
print(f"Diện tích hình chữ nhật 2: {hc2.area()}")

# Bài 3: Tạo lớp BankAccount với các thuộc tính: 
            # account_number: số tài khoản 
            # owner: tên chủ tài khoản
            # balance: số dư tài khoản
# Tạo phương thức:
            # deposit(amount): nạp tiền vào tài khoản
            # withdraw(amount): rút tiền từ tài khoản
            # display_balance(): hiển thị số dư tài khoản
            # (amount: số tiền nạp/rút theo đơn vị $)
account1 = oop.BankAccount("123456789", "Nhật Minh", 1000)
account1.display_balance()
account1.deposit(500)           # Số dư: $1500
account1.deposit(-200)          # Số dư: $1500 (nạp thất bại)
account1.withdraw(1200)         # Số dư: $300
account1.withdraw(500)          # Số dư: $300 (rút thất bại)
