import os
import random
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import Qt
colors = dict()
colors["1000"] = QtGui.QBrush(Qt.red)
colors["1"] = QtGui.QBrush(Qt.green)
colors["10"] = QtGui.QBrush(Qt.black)
class TreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, tree, path, abs_path:str, color:str = "10"):
        super().__init__(tree, path)
        self.path = abs_path
        self.setForeground(0, colors[color])
    def get_abs_path(self):
        return self.path

class Ui_MainWindow(object):
    root_path = "C:/Users/hello/Desktop/root"
    cfg_path = "C:/Users/hello/PycharmProjects/cs4/config/cfg.txt"
    files_cfg = "C:/Users/hello/PycharmProjects/cs4/config/files_cfg.txt"
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
        self.createFolderButton.clicked.connect(self.create_fldr_handler)
        self.deleteFolderButton.clicked.connect(self.delete_fldr_hadler)
        self.renameFolderButton.clicked.connect(self.rename_fldr_handler)
        self.securityLevelSelector.addItems(self.read_from_cfg(self.cfg_path))
        self.setSecurityLevelButton.clicked.connect(self.set_lvl)



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


    def set_lvl(self):
        level = self.securityLevelSelector.currentText()
        if len(self.treeWidget.selectedItems()) == 0:
            return
        folder = self.treeWidget.selectedItems()[0].get_abs_path()
        content = self.read_from_cfg(self.files_cfg)
        for i in range(len(content)):
            fldr, lvl = content[i].split(" ")
            if fldr == folder:
                content[i] = fldr + " " + level
                break
        self.write_to_cfg(content, self.files_cfg)
        self.treeWidget.clear()
        self.load_tree_structure(self.root_path, self.treeWidget)

    def configure_selector(self):
        self.securityLevelSelector.clear()
        content = self.read_from_cfg(self.cfg_path)
        self.securityLevelSelector.addItems(content)

    def create_fldr_handler(self):
        fldr = self.folderNameInput.text()
        self.folderNameInput.clear()
        if len(self.treeWidget.selectedItems()) == 0:
            return
        path = self.treeWidget.selectedItems()[0].get_abs_path() + "/" + fldr
        print(path)
        os.mkdir(path, 0o666)
        content = self.read_from_cfg(self.files_cfg)
        content.append(path + " 10")
        self.write_to_cfg(content, self.files_cfg)
        self.treeWidget.clear()
        self.load_tree_structure(self.root_path,self.treeWidget)

    def delete_fldr_hadler(self):
        if len(self.treeWidget.selectedItems()) == 0:
            return
        path = self.treeWidget.selectedItems()[0].get_abs_path()
        shutil.rmtree(path)
        content = self.read_from_cfg(self.files_cfg)
        for i in range(len(content)):
            fldr, lvl = content[i].split(" ")
            if fldr == path:
                content.pop(i)
                break
        self.write_to_cfg(content, self.files_cfg)
        self.treeWidget.clear()
        self.load_tree_structure(self.root_path, self.treeWidget)


    def rename_fldr_handler(self):
        if len(self.treeWidget.selectedItems()) == 0:
            return
        old_name = self.treeWidget.selectedItems()[0].get_abs_path()
        new_name = self.newNameOfFolder.text()
        temp = old_name.split("/")
        temp[-1] = new_name
        new_path = "/".join(temp)
        print("rename_fldr_handler: " + new_path)
        self.newNameOfFolder.clear()
        content = self.read_from_cfg(self.files_cfg)
        for i in range(len(content)):
            fldr, lvl = content[i].split(" ")
            if fldr == old_name:
                content[i] = new_name + " " + lvl
                break
        self.write_to_cfg(content, self.files_cfg)
        shutil.move(old_name, new_path)
        self.treeWidget.clear()
        self.load_tree_structure(self.root_path, self.treeWidget)


    def load_tree_structure(self, startroot_path, tree):
        import os
        from PyQt5.QtWidgets import QTreeWidgetItem
        from PyQt5.QtGui import QIcon
        for element in os.listdir(startroot_path):
            path_info = startroot_path + "/" + element
            content = self.read_from_cfg(self.files_cfg)
            files = [r.split(" ")[0] for r in content]
            sec_lvls = [r.split(" ")[1] for r in content]
            if path_info in files:
                level = sec_lvls[files.index(path_info)]
            else:
                level = "10"
                content.append(path_info + " " + level)
                self.write_to_cfg(content, self.files_cfg)
            parent_itm = TreeWidgetItem(tree, [os.path.basename(element)], path_info, level)
            if os.path.isdir(path_info):
                self.load_tree_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            else:
                parent_itm.setIcon(0, QIcon('assets/file.ico'))
    def create_sec_lvl_handler(self):
        inp = self.securityLevelinput.text()
        self.securityLevelinput.clear()
        if not inp.isnumeric() or int(inp) > 1000 or int(inp) < 0:
            print("create_sec_lvl_handler: Wrong input")
            return
        content = self.read_from_cfg(self.cfg_path)
        if inp in content:
            print("create_sec_lvl_handler: Security level already exists")
            return
        content.append(inp)
        self.write_to_cfg(content, self.cfg_path)
        self.configure_selector()
        #colors[inp] = QtGui.QBrush(QtGui.QColor(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #print(colors[inp])
    def delete_sec_lvl_handler(self):
        inp = self.securityLevelinput.text()
        self.securityLevelinput.clear()
        if not inp.isnumeric():
            print("delete_sec_lvl_handler: Wrong input")
            return
        content = self.read_from_cfg(self.cfg_path)
        if inp not in content:
            print("delete_sec_lvl_handler: Security level doesn't exist")
            return
        content.remove(inp)
        self.write_to_cfg(content, self.cfg_path)
        self.configure_selector()

    def rename_sec_lvl_handler(self):
        old_name = self.securityLevelinput.text()
        self.securityLevelinput.clear()
        new_name = self.newNameOfSecurityLevel.text()
        self.newNameOfSecurityLevel.clear()
        if not old_name.isnumeric() or not new_name.isnumeric() or int(new_name) > 1000 or int(new_name) < 0:
            print("rename_sec_lvl_handler: Wrong input")
            return
        content = self.read_from_cfg(self.cfg_path)
        if old_name not in content or new_name in content:
            print("rename_sec_lvl_handler: Wrong input 2")
            return
        content[content.index(old_name)] = new_name
        self.write_to_cfg(content, self.cfg_path)
        self.configure_selector()
    def write_to_cfg(self, content, path):
        with open(path, "w+") as m:
            content_towrite = "|".join(content)
            print(f"Writing {content_towrite} to file")
            m.writelines(content_towrite)

    def read_from_cfg(self, path):
        with open(path, "r+") as m:
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


