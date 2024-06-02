from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from main import Audio_Item 
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QHBoxLayout()
        verticalLayout = QVBoxLayout()

        mainLayout.addLayout(verticalLayout)
        self.setLayout(mainLayout)

        self.myLable=QLabel('kolichestvo nagatiy')
        myLable1=QLabel('Ya ochen krutoy')
        

        select_file_button = QPushButton('Vibrat file')
        spectre_button = QPushButton('Pokazat spectre')
        osc_button = QPushButton('Pokazat oscillogrammu')

        verticalLayout.addWidget(self.myLable)
        verticalLayout.addWidget(myLable1)
        verticalLayout.addWidget(select_file_button)
        verticalLayout.addWidget(spectre_button)
        verticalLayout.addWidget(osc_button)

        select_file_button.clicked.connect(self.select_file)

        

    
    def select_file(self):
        filename = QFileDialog.getOpenFileName()
        self.audio_item = Audio_Item(filename)
        self.myLable.setText(f'Vibraniy file={filename}')
        print(self.audio_item )
        

app=QApplication([])
mainwidget =MyWidget()
mainwidget.show()
app.exec()
