import sys
import json
import re

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)


USERS_FILE = "users.json"


class MainApp:
    def __init__(self):

        self.signup_window = uic.loadUi("signup.ui")
        self.login_window = uic.loadUi("login.ui")
        self.calculator_window = uic.loadUi("calculator.ui")

        self.last_answer = ""

        self.setup_navigation()
        self.setup_signup()
        self.setup_login()
        self.setup_calculator()

        self.signup_window.show()

    # =========================
    # NAVIGATION
    # =========================

    def setup_navigation(self):

        windows = [
            self.signup_window,
            self.login_window,
            self.calculator_window
        ]

        for window in windows:

            window.btnSignupNav.clicked.connect(
                self.show_signup
            )

            window.btnLoginNav.clicked.connect(
                self.show_login
            )

            window.btnCalculatorNav.clicked.connect(
                self.show_calculator
            )

    def show_signup(self):
        self.hide_all()
        self.signup_window.show()

    def show_login(self):
        self.hide_all()
        self.login_window.show()

    def show_calculator(self):
        self.hide_all()
        self.calculator_window.show()

    def hide_all(self):
        self.signup_window.hide()
        self.login_window.hide()
        self.calculator_window.hide()

    # =========================
    # SIGNUP
    # =========================

    def setup_signup(self):

        self.signup_window.signupButton.clicked.connect(
            self.signup
        )

    def signup(self):

        username = self.signup_window.usernameInput.text()
        email = self.signup_window.emailInput.text()
        gender = self.signup_window.genderCombo.currentText()
        password = self.signup_window.passwordInput.text()
        confirm_password = self.signup_window.confirmPasswordInput.text()

        if not username or not email or not password or not confirm_password:
            self.show_error("Please fill all fields")
            return

        if len(username) < 3:
            self.show_error("Username must be at least 3 characters")
            return

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_regex, email):
            self.show_error("Invalid email format")
            return

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$'

        if not re.match(password_regex, password):
            self.show_error(
                "Password must contain uppercase, lowercase and number"
            )
            return

        if password != confirm_password:
            self.show_error("Confirm password does not match")
            return

        users = self.load_users()

        for user in users:
            if user["email"] == email:
                self.show_error("Email already exists")
                return

        new_user = {
            "username": username,
            "email": email,
            "gender": gender,
            "password": password
        }

        users.append(new_user)

        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4)

        QMessageBox.information(
            self.signup_window,
            "Success",
            "Signup successful"
        )

        self.show_login()

    # =========================
    # LOGIN
    # =========================

    def setup_login(self):

        self.login_window.loginButton.clicked.connect(
            self.login
        )

    def login(self):

        email = self.login_window.emailInput.text()
        password = self.login_window.passwordInput.text()

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$'

        if not re.match(email_regex, email):
            self.show_error("Invalid email format")
            return

        if not re.match(password_regex, password):
            self.show_error("Invalid password format")
            return

        users = self.load_users()

        for user in users:

            if user["email"] == email and user["password"] == password:

                QMessageBox.information(
                    self.login_window,
                    "Success",
                    "Login successful"
                )

                self.show_calculator()
                return

        self.show_error("Incorrect email or password")

    # =========================
    # CALCULATOR
    # =========================

    def setup_calculator(self):

        # Number buttons
        self.calculator_window.btn0.clicked.connect(
            lambda: self.add_to_expression("0")
        )

        self.calculator_window.btn1.clicked.connect(
            lambda: self.add_to_expression("1")
        )

        self.calculator_window.btn2.clicked.connect(
            lambda: self.add_to_expression("2")
        )

        self.calculator_window.btn3.clicked.connect(
            lambda: self.add_to_expression("3")
        )

        self.calculator_window.btn4.clicked.connect(
            lambda: self.add_to_expression("4")
        )

        self.calculator_window.btn5.clicked.connect(
            lambda: self.add_to_expression("5")
        )

        self.calculator_window.btn6.clicked.connect(
            lambda: self.add_to_expression("6")
        )

        self.calculator_window.btn7.clicked.connect(
            lambda: self.add_to_expression("7")
        )

        self.calculator_window.btn8.clicked.connect(
            lambda: self.add_to_expression("8")
        )

        self.calculator_window.btn9.clicked.connect(
            lambda: self.add_to_expression("9")
        )

        # Operators
        self.calculator_window.btnPlus.clicked.connect(
            lambda: self.add_to_expression("+")
        )

        self.calculator_window.btnMinus.clicked.connect(
            lambda: self.add_to_expression("-")
        )

        self.calculator_window.btnMultiply.clicked.connect(
            lambda: self.add_to_expression("*")
        )

        self.calculator_window.btnDivide.clicked.connect(
            lambda: self.add_to_expression("/")
        )

        self.calculator_window.btnDot.clicked.connect(
            lambda: self.add_to_expression(".")
        )

        # Special buttons
        self.calculator_window.btnAC.clicked.connect(
            self.clear_expression
        )

        self.calculator_window.btnDEL.clicked.connect(
            self.delete_last
        )

        self.calculator_window.btnAns.clicked.connect(
            self.insert_answer
        )

        self.calculator_window.btnEqual.clicked.connect(
            self.calculate
        )

    def add_to_expression(self, value):

        current = self.calculator_window.expressionDisplay.text()

        self.calculator_window.expressionDisplay.setText(
            current + value
        )

    def clear_expression(self):

        self.calculator_window.expressionDisplay.clear()
        self.calculator_window.resultDisplay.clear()

    def delete_last(self):

        current = self.calculator_window.expressionDisplay.text()

        self.calculator_window.expressionDisplay.setText(
            current[:-1]
        )

    def insert_answer(self):

        if self.last_answer == "":
            self.show_error("No previous answer")
            return

        current = self.calculator_window.expressionDisplay.text()

        self.calculator_window.expressionDisplay.setText(
            current + str(self.last_answer)
        )

    def calculate(self):

        expression = self.calculator_window.expressionDisplay.text()

        if expression == "":
            self.show_error("Expression is empty")
            return

        try:

            result = eval(expression)

            self.last_answer = result

            self.calculator_window.resultDisplay.setText(
                str(result)
            )

        except ZeroDivisionError:

            self.show_error("Cannot divide by zero")

        except SyntaxError:

            self.show_error("Invalid syntax")

        except Exception:

            self.show_error("Calculation error")

    # =========================
    # UTIL
    # =========================

    def load_users(self):

        try:
            with open(USERS_FILE, "r") as file:
                return json.load(file)

        except:
            return []

    def show_error(self, message):

        QMessageBox.critical(
            None,
            "Error",
            message
        )


app = QApplication(sys.argv)

main_app = MainApp()

sys.exit(app.exec())