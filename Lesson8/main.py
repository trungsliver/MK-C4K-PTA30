# Import thư viện
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# Tạo app (python)
app = QApplication(sys.argv)

# Mỗi trang gia diện là 1 class riêng biệt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Lấy file giao diện đã tạo (cùng folder)
        uic.loadUi('lesson8.ui', self)
        # Sự kiện thay đổi số lượng vé
        self.spinBox_film1.valueChanged.connect(self.update_price)
        self.spinBox_film2.valueChanged.connect(self.update_price)
        self.spinBox_popcorn.valueChanged.connect(self.update_price)
        self.spinBox_luckyBox.valueChanged.connect(self.update_price)
        # Sự kiện ấn nút checkout
        self.pushButton_checkout.clicked.connect(self.checkout)

    # Phương thức cập nhật số tiền khi thay đổi số lượng vé
    def update_price(self):
        # Khởi tạo giá vé
        price = {
            'film1': 120000,
            'film2': 110000,
            'popcorn': 150000,
            'luckyBox': 100000
        }
        # Biến lưu trữ tổng tiền
        total = 0
        # Tính số lượng theo từng sản phẩm
        total += self.spinBox_film1.value() * price['film1']
        total += self.spinBox_film2.value() * price['film2'] 
        total += self.spinBox_popcorn.value() * price['popcorn']
        total += self.spinBox_luckyBox.value() * price['luckyBox']
        # Hiển thị total lên lineEdit
        self.lineEdit_total.setText(str(total) + " VNĐ")

    # Phương thức xử lý checkout
    def checkout(self):
        # hiện thông báo
        msg_box('Thanh toán thành công', f'Số tiền: {self.lineEdit_total.text()}')

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
window = MainWindow()
window.show()
sys.exit(app.exec())

# Cách chạy file:
    # Bước 1: Chuột phải vào folder muốn chạy
    # Bước 2: Chọn "Open in integrated Terminal"
    # Bước 3: Nhập lệnh "python main.py"