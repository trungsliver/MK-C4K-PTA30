# Data Types - Kiểu dữ liệu
    # String (str): Chuỗi ký tự / Xâu ký tự
name = "Minh Tùng"
    # Integer (int): Số nguyên
age = 13
    # Float (float): Số thực
score = 8.5
    # Boolean (bool): Giá trị đúng hoặc sai
male = True

# Các cách print
    # Dùng dấu + (yêu cầu phải chuyển sang string)
print("Tên: " + name)
print("Tuổi: " + str(age))
    # Dùng dấu , 
print("Điểm:", score)
    # Dùng f-string
print(f"Tên: {name}, Tuổi: {age}, Điểm: {score}")

# Nhập dữ liệu - input()
age = input('Nhập tuổi: ')          # string
age = int(input('Nhập tuổi: '))     # int
score = float(input('Nhập điểm: ')) # float

# Các phép toán
    # Thông thường:                 + - * /
    # Chia lấy nguyên:              //
    # Chia lấy dư:                  %
    # Lũy thừa:                     **
    # Phép toán logic:              and or not

# Câu điều kiện
    # Các phép so sánh:         == != <= >= > <
    # Các phép logic:           and or not
    # Cấu trúc: 3 dạng
        # Dạng thiếu:           if ...
        # Dạng đủ:              if ... else ...
        # Dạng đa nhánh:        if ... elif ... elif ... else ...

# Vòng lặp hữu hạn - Vòng lặp for
    # range (start, end, step):         chạy từ start => end-1
    # range (start, end):
    # range (end):                       chạy từ 0 => end-1

# Vòng lặp vô hạn - Vòng lặp while
    # while <điều kiện>: lặp đến khi điều kiện sai

    # Danh sách: array/list: CRUD
    # C - Create: Tạo PTA30 = []
    # R - Read: Duyệt, in danh sách
        # cách 1: for i in range(len(arr)):
        # cách 2: for item in arr:
        # cách 3: for index, value in enumerate(arr):
        # cách 4: print(arr)
    # U - Update: chỉnh sửa 
        # append(item): thêm phần tử vào cuối danh sách
        # insert(index, item): thêm phần tử vào vị trí index
        # arr[i] = new_value
    # D - Delete: xóa
        # remove(item): xóa bằng giá trị
        # pop(index): xóa bằng chỉ số index
        # clear(): xóa tất cả phần tử
    # Sắp xếp:
        # sort(): sắp xếp tăng dần
        # sort(reversed=True): sắp xếp giảm dần
    # Khác:
        # len(): trả về độ dài (số lượng phần tử)
        # min(): trả về item nhỏ nhất
        # max(): trả về item lớn nhất

# Chuỗi / xâu ký tự
    # len(): độ dài chuỗi
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): tách chuỗi
    # replace(): thay thế
    # upper(): chuyển thành chữ hoa
    # lower(): chuyển thành chữ thường
    # capwords(): chuyển chữ cái đầu thành hoa

# Hàm/Chương trình con
    # Hàm không có giá trị trả về
    # Hàm có giá trị trả về (return)
    # Hàm có tham số truyền vào: chuvi(cdai, crong)