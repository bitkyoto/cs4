
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 30, 181, 125))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.securityNameInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.securityNameInput.setObjectName("securityNameInput")
        self.verticalLayout.addWidget(self.securityNameInput)
        self.securityLevelinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.securityLevelinput.setObjectName("securityLevelinput")
        self.verticalLayout.addWidget(self.securityLevelinput)
        self.createSecurityLevelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.createSecurityLevelButton.setObjectName("createSecurityLevelButton")
        self.verticalLayout.addWidget(self.createSecurityLevelButton)
        self.deleteSecurityLevelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteSecurityLevelButton.setObjectName("deleteSecurityLevelButton")
        self.verticalLayout.addWidget(self.deleteSecurityLevelButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 30, 181, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.newNameOfSecurityLevel = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.newNameOfSecurityLevel.setObjectName("newNameOfSecurityLevel")
        self.verticalLayout_2.addWidget(self.newNameOfSecurityLevel)
        self.newLevelOfSecurityLevel = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.newLevelOfSecurityLevel.setObjectName("newLevelOfSecurityLevel")
        self.verticalLayout_2.addWidget(self.newLevelOfSecurityLevel)
        self.renameSecurityLevelButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.renameSecurityLevelButton.setObjectName("renameSecurityLevelButton")
        self.verticalLayout_2.addWidget(self.renameSecurityLevelButton)
        spacerItem = QtWidgets.QSpacerItem(20, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(340, 200, 181, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.folderNameInput = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.folderNameInput.setObjectName("folderNameInput")
        self.verticalLayout_3.addWidget(self.folderNameInput)
        self.createFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.createFolderButton.setObjectName("createFolderButton")
        self.verticalLayout_3.addWidget(self.createFolderButton)
        self.deleteFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.deleteFolderButton.setObjectName("deleteFolderButton")
        self.verticalLayout_3.addWidget(self.deleteFolderButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(540, 200, 181, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.newNameOfFolder = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.newNameOfFolder.setObjectName("newNameOfFolder")
        self.verticalLayout_4.addWidget(self.newNameOfFolder)
        self.renameFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.renameFolderButton.setObjectName("renameFolderButton")
        self.verticalLayout_4.addWidget(self.renameFolderButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(340, 370, 181, 116))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.securityLevelSelector = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.securityLevelSelector.setObjectName("securityLevelSelector")
        self.verticalLayout_6.addWidget(self.securityLevelSelector)
        self.setSecurityLevelButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.setSecurityLevelButton.setObjectName("setSecurityLevelButton")
        self.verticalLayout_6.addWidget(self.setSecurityLevelButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem2)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(30, 30, 261, 471))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget_6)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.showFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.showFolderButton.setObjectName("showFolderButton")
        self.verticalLayout_5.addWidget(self.showFolderButton)
        self.copyButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout_5.addWidget(self.copyButton)
        self.copytreeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget_6)
        self.copytreeWidget.setObjectName("copytreeWidget")
        self.copytreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.copytreeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Управление уровнями секретности"))
        self.createSecurityLevelButton.setText(_translate("MainWindow", "Создать "))
        self.deleteSecurityLevelButton.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Новое название"))
        self.renameSecurityLevelButton.setText(_translate("MainWindow", "Переименовать"))
        self.label_3.setText(_translate("MainWindow", "Управление папками"))
        self.createFolderButton.setText(_translate("MainWindow", "Создать "))
        self.deleteFolderButton.setText(_translate("MainWindow", "Удалить"))
        self.label_4.setText(_translate("MainWindow", "Новое название"))
        self.renameFolderButton.setText(_translate("MainWindow", "Переименовать"))
        self.label_6.setText(_translate("MainWindow", "Задать уровень секретности"))
        self.setSecurityLevelButton.setText(_translate("MainWindow", "Задать"))
        self.showFolderButton.setText(_translate("MainWindow", "Отобразить папки"))
        self.copyButton.setText(_translate("MainWindow", "Копировать"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
