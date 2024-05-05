import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, 
QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QLabel; 
 
class DataBarang(QWidget): 
    def _init_(self): 
        super()._init_() 
 
        self.setWindowTitle("Input Data Barang") 
        self.setGeometry(200, 200, 400, 300) 
 
        layout = QVBoxLayout() 
 
        self.table = QTableWidget() 
        self.table.setColumnCount(2) 
        self.table.setHorizontalHeaderLabels(['Nama Barang', 
'Harga']) 
        layout.addWidget(self.table) 
 
        self.nama_barang = QLineEdit() 
        layout.addWidget(self.nama_barang) 
 
        self.harga_barang = QLineEdit() 
        layout.addWidget(self.harga_barang) 
 
        tambah_button = QPushButton("Tambahkan") 
        tambah_button.clicked.connect(self.tambah_data) 
        layout.addWidget(tambah_button) 
 
        self.setLayout(layout) 
 
    def tambah_data(self): 
        row_position = self.table.rowCount() 
        self.table.insertRow(row_position) 
        self.table.setItem(row_position, 0, 
QTableWidgetItem(self.nama_barang.text())) 
        self.table.setItem(row_position, 1, 
QTableWidgetItem(self.harga_barang.text())) 
 
def main(): 
    app = QApplication(sys.argv) 
    window = DataBarang() 
    window.show() 
    sys.exit(app.exec_()) 
 
if _name_ == '_main_': 
    main()