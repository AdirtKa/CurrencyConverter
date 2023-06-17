import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from CurConUi import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.line_new_currency.setPlaceholderText("В какую валюту перевести")
        self.ui.line_old_currency.setPlaceholderText("Из какой валюты перевести")
        self.ui.line_old_amount.setPlaceholderText("У вас было")
        self.ui.button_convert.clicked.connect(self.convert)

    #        self.ui.button_convert.setObjectName()

    def convert(self):
        converter = CurrencyConverter()
        old_currency = self.ui.line_old_currency.text().upper()
        new_currency = self.ui.line_new_currency.text().upper()
        old_amount = self.ui.line_old_amount.text()
        if old_amount.isdigit() and old_currency and new_currency:
            new_amount = round(converter.convert(int(old_amount), f"{old_currency}", f"{new_currency}"), 2)
            self.ui.line_new_amount.setText(str(new_amount))
        else:
            self.ui.line_new_amount.setText("Ошибка ввода")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = CurrencyConv()
    application.show()

    sys.exit(app.exec())
