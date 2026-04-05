# Import thư viện
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# Tạo app (python)
app = QApplication(sys.argv)

# Khai báo danh sách người dùng dạng: "email:password"
users = ['admin:123456']

# Mỗi trang gia diện là 1 class riêng biệt
class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        # Lấy file giao diện đã tạo (cùng folder)
        uic.loadUi('signup.ui', self)
        # Khai báo sự kiện ấn nút Signup
        self.pushButton_signup.clicked.connect(self.signup_check)

    # Phương thức kiểm tra đăng ký
    def signup_check(self):
        # Lấy thông tin từ giao diện
        username = self.lineEdit_username.text().strip()
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        confirm = self.lineEdit_confirm.text().strip()
        checkB = self.checkBox.isChecked()

        # Biến kiểm tra đăng ký
        check = True

        # Thiếu thông tin
        if username == '' or email == '' or password == '' or confirm == '' or checkB != True:
            check = False
            msg_box('Signup fail', 'Missing information!')
        # Password và confirm không khớp
        elif password != confirm:
            check = False
            msg_box('Signup fail', 'Password not match!')
        # Độ dài password >= 6
        elif len(password) < 6:
            check = False
            msg_box('Signup fail', 'Password at least 6 characters!')
        # Đã tồn tại email trong danh sách users
        else:
            # Duyệt danh sách users (cách 2 - chỉ duyệt value)
            for user in users:
                # Tách email, password và lưu vào 2 biến
                stored_email, stored_password = user.split(':')
                if stored_email == email:
                    check = False
                    msg_box('Signup fail', 'Email already exists!')
                    break

        # kiểm tra xem có đăng ký thành công không
        if check == True:
            # Thêm tài khoản vào danh sách users
            new_acc = f'{email}:{password}'
            users.append(new_acc)
            msg_box('Signup success', 'Signup success!')
            # Chuyển sang trang Login
            switch_window(Login())

# Mỗi trang gia diện là 1 class riêng biệt
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # Lấy file giao diện đã tạo (cùng folder)
        uic.loadUi('login.ui', self)
        # Sự kiện ấn nút login
        self.pushButton_login.clicked.connect(self.login_check)

    # Kiểm tra đăng nhập
    def login_check(self):
        # Lấy thông tin từ giao diện
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        # Biến kiểm tra đăng nhập
        check = False

        # Kiểm tra đăng nhập
        for user in users:
            stored_email, stored_password = user.split(':')
            if email == stored_email and password == stored_password:
                check = True
                break
        
        # Kiểm tra đăng nhập
        if check == True:
            msg_box('Login success', 'Welcome to my app !!!')
            switch_window(Signup())
        else:
            msg_box('Login fail', 'Email or password is incorrect!')

# Hàm hiển thị thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Chạy app
# Run app
window = Signup()
window.show()
sys.exit(app.exec())

# Cách chạy file:
    # Bước 1: Chuột phải vào folder muốn chạy
    # Bước 2: Chọn "Open in integrated Terminal"
    # Bước 3: Nhập lệnh "python main.py"