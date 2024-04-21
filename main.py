from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    root_path = "C:/Users/hello/PycharmProjects/cs4/root"
    cfg_path = "C:/Users/hello/PycharmProjects/cs4/config/cfg.txt"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(30, 30, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 30, 181, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(340, 370, 181, 101))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.createSecurityLevelButton.clicked.connect(self.create_sec_lvl_handler)
        self.deleteSecurityLevelButton.clicked.connect(self.delete_sec_lvl_handler)
        self.renameSecurityLevelButton.clicked.connect(self.rename_sec_lvl_handler)


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

        self.load_tree_structure(self.root_path, self.treeWidget)
        self.treeWidget.setHeaderHidden(True)

    def load_tree_structure(self, startroot_path, tree):
        import os
        from PyQt5.QtWidgets import QTreeWidgetItem
        from PyQt5.QtGui import QIcon
        for element in os.listdir(startroot_path):
            path_info = startroot_path + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                self.load_tree_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            else:
                parent_itm.setIcon(0, QIcon('assets/file.ico'))

    def create_sec_lvl_handler(self):
        inp = self.securityLevelinput.text()
        self.securityLevelinput.clear()
        if not inp.isalpha():
            print("create_sec_lvl_handler: Wrong input")
            return
        with open(self.cfg_path, "r+") as m:
            content = m.readline().split("|")
            if inp in content:
                print("create_sec_lvl_handler: Security level already exists")
                return
            content.append(inp)
        self.write_to_cfg(content)

    def delete_sec_lvl_handler(self):
        inp = self.securityLevelinput.text()
        self.securityLevelinput.clear()
        if not inp.isalpha():
            print("delete_sec_lvl_handler: Wrong input")
            return
        content = self.read_from_cfg()
        if inp not in content:
            print("delete_sec_lvl_handler: Security level doesn't exist")
            return
        content.remove(inp)
        self.write_to_cfg(content)

    def rename_sec_lvl_handler(self):
        old_name = self.securityLevelinput.text()
        self.securityLevelinput.clear()
        new_name = self.newNameOfSecurityLevel.text()
        self.newNameOfSecurityLevel.clear()
        if not old_name.isalpha() or not new_name.isalpha():
            print("rename_sec_lvl_handler: Wrong input")
            return
        content = self.read_from_cfg()
        if old_name not in content or new_name in content:
            print("rename_sec_lvl_handler: Wrong input 2")
            return
        content[content.index(old_name)] = new_name
        self.write_to_cfg(content)
    def write_to_cfg(self, content):
        with open(self.cfg_path, "w+") as m:
            content_towrite = "|".join(content)
            print(f"Writing {content_towrite} to file")
            m.writelines(content_towrite)

    def read_from_cfg(self):
        with open(self.cfg_path, "r+") as m:
            content = m.readline().split("|")
        return content
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())


