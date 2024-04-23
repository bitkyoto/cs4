import os
import random
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os
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

        self.createSecurityLevelButton.clicked.connect(self.create_sec_lvl_handler)
        self.deleteSecurityLevelButton.clicked.connect(self.delete_sec_lvl_handler)
        self.renameSecurityLevelButton.clicked.connect(self.rename_sec_lvl_handler)
        self.createFolderButton.clicked.connect(self.create_fldr_handler)
        self.deleteFolderButton.clicked.connect(self.delete_fldr_hadler)
        self.renameFolderButton.clicked.connect(self.rename_fldr_handler)
        self.securityLevelSelector.addItems(self.read_from_cfg(self.cfg_path))
        self.setSecurityLevelButton.clicked.connect(self.set_lvl)
        self.showFolderButton.clicked.connect(self.show_available_folders)
        self.copyButton.clicked.connect(self.copy_files_handler)


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

        self.load_tree_structure(self.root_path, self.treeWidget)
        self.load_copytree_structure(self.root_path, self.copytreeWidget)
        self.treeWidget.setHeaderHidden(True)
        self.copytreeWidget.setHeaderHidden(True)

    def show_available_folders(self):
        self.copytreeWidget.clear()
        self.load_copytree_structure(self.root_path,self.copytreeWidget)

    def dump_copy_files(self, from_fldr, to_fldr):
        content_ = self.read_from_cfg(self.files_cfg)
        files_ = [r.split(" ")[0] for r in content_]
        lvls_ = [r.split(" ")[1] for r in content_]
        for element in os.listdir(from_fldr):
            path_info = from_fldr + "/" + element
            if os.path.isdir(path_info):
                if path_info in files_:
                    desc = to_fldr + " " + lvls_[files_.index(path_info)]
                    content_.append(desc)
                else:
                    content_.append(path_info + " " + "1")
                    content_.append(to_fldr + " " + "1")
                self.write_to_cfg(content_, self.files_cfg)
                self.dump_copy_files(path_info, to_fldr)




        # for element in os.listdir(cur_path):
        #     path_info = cur_path + "/" + element
        #     content = self.read_from_cfg(self.files_cfg)
        #     files = [r.split(" ")[0] for r in content]
        #     sec_lvls = [r.split(" ")[1] for r in content]
        #     if not os.path.isdir(path_info):
        #         shutil.copy2(path_info,to_fldr)
        #     else:
        #         if path_info in files:
        #             shutil.copytree(path_info,to_fldr)
        #         else:
        #             level = "1"
        #             content.append(path_info + " " + level)
        #             self.write_to_cfg(content, self.files_cfg)
        #     if os.path.isdir(path_info):
        #         self.load_tree_structure(path_info, parent_itm)


    def copy_files_handler(self):
        if len(self.treeWidget.selectedItems()) == 0:
            return
        if len(self.copytreeWidget.selectedItems()) == 0:
            return

        from_fldr = self.treeWidget.selectedItems()[0].get_abs_path()
        to_fldr = self.copytreeWidget.selectedItems()[0].get_abs_path()

        if not os.path.isdir(from_fldr):
            print(f"copy_files_handler: Selected item is a file!")
            return
        if not os.path.isdir(to_fldr):
            print(f"copy_files_handler: Selected item is a file!")
            return

        content_ = self.read_from_cfg(self.files_cfg)
        files_ = [r.split(" ")[0] for r in content_]
        lvls_ = [r.split(" ")[1] for r in content_]
        from_fldr_lvl = lvls_[files_.index(from_fldr)]
        to_fldr_lvl = lvls_[files_.index(to_fldr)]
        print(f"from {from_fldr} lvl: {from_fldr_lvl}")

        to_fldr += "/" + from_fldr.split("/")[-1]
        print(f"to {to_fldr} lvl: {to_fldr_lvl}")
        if from_fldr_lvl <= to_fldr_lvl:
            shutil.copytree(from_fldr,to_fldr)
            print("Here")
            self.dump_copy_files(from_fldr, to_fldr)
            self.treeWidget.clear()
            self.copytreeWidget.clear()
            self.load_tree_structure(self.root_path, self.treeWidget)
            self.load_copytree_structure(self.root_path,self.copytreeWidget)


    def load_copytree_structure(self, startroot_path, tree):
        if len(self.treeWidget.selectedItems()) == 0:
            return
        from_fldr = self.treeWidget.selectedItems()[0].get_abs_path()
        if from_fldr == self.root_path + "/root":
            return
        if not os.path.isdir(from_fldr):
            print(f"load_copytree_structure: Selected item is a file!")
            return
        content_ = self.read_from_cfg(self.files_cfg)
        files_ = [r.split(" ")[0] for r in content_]
        lvls_ = [r.split(" ")[1] for r in content_]
        from_fldr_lvl = lvls_[files_.index(from_fldr)]
        for element in os.listdir(startroot_path):
            path_info = startroot_path + "/" + element
            if not os.path.isdir(path_info):
                continue
            content = self.read_from_cfg(self.files_cfg)
            if path_info in files_:
                level = lvls_[files_.index(path_info)]
            else:
                level = "1"
                content.append(path_info + " " + level)
                self.write_to_cfg(content, self.files_cfg)
            if path_info == self.root_path + "/root":
                parent_itm = TreeWidgetItem(tree, [os.path.basename(element)], path_info, "10")
            else:
                if level >= from_fldr_lvl:
                    parent_itm = TreeWidgetItem(tree, [os.path.basename(element)], path_info, "1")
                else:
                    parent_itm = TreeWidgetItem(tree, [os.path.basename(element)], path_info,"1000")
            if os.path.isdir(path_info):
                self.load_copytree_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            else:
                parent_itm.setIcon(0, QIcon('assets/file.ico'))

    def set_lvl(self):
        level = self.securityLevelSelector.currentText()
        if len(self.treeWidget.selectedItems()) == 0:
            return
        folder = self.treeWidget.selectedItems()[0].get_abs_path()
        if not os.path.isdir(folder):
            print(f"set_lvl: Selected item is a file!")
            return
        content = self.read_from_cfg(self.files_cfg)
        for i in range(len(content)):
            fldr, lvl = content[i].split(" ")
            if fldr == folder:
                content[i] = fldr + " " + level
                break
        self.write_to_cfg(content, self.files_cfg)
        self.treeWidget.clear()
        self.copytreeWidget.clear()
        self.load_tree_structure(self.root_path, self.treeWidget)

    def configure_selector(self):
        self.securityLevelSelector.clear()
        content = self.read_from_cfg(self.cfg_path)
        self.securityLevelSelector.addItems(content)

    def create_fldr_handler(self):
        fldr = self.folderNameInput.text()
        self.folderNameInput.clear()
        if len(self.treeWidget.selectedItems()) == 0:
            print(f"create_fldr_handler: No element is selected!")
            return
        if not os.path.isdir(self.treeWidget.selectedItems()[0].get_abs_path()):
            print(f"create_fldr_handler: Selected item is a file!")
            return
        path = self.treeWidget.selectedItems()[0].get_abs_path() + "/" + fldr
        print(path)
        os.mkdir(path, 0o666)
        content = self.read_from_cfg(self.files_cfg)
        content.append(path + " 1")
        self.write_to_cfg(content, self.files_cfg)
        self.treeWidget.clear()
        self.copytreeWidget.clear()
        self.load_tree_structure(self.root_path,self.treeWidget)

    def delete_fldr_hadler(self):
        if len(self.treeWidget.selectedItems()) == 0:
            return
        path = self.treeWidget.selectedItems()[0].get_abs_path()
        if not os.path.isdir(path):
            print(f"delete_fldr_handler: Selected item is a file!")
            return
        shutil.rmtree(path)
        content = self.read_from_cfg(self.files_cfg)
        for i in range(len(content)):
            fldr, lvl = content[i].split(" ")
            if fldr == path:
                content.pop(i)
                break
        self.write_to_cfg(content, self.files_cfg)
        self.treeWidget.clear()
        self.copytreeWidget.clear()
        self.load_tree_structure(self.root_path, self.treeWidget)


    def rename_fldr_handler(self):
        if len(self.treeWidget.selectedItems()) == 0:
            return
        old_name = self.treeWidget.selectedItems()[0].get_abs_path()
        new_name = self.newNameOfFolder.text()
        if not os.path.isdir(old_name):
            print(f"delete_fldr_handler: Selected item is a file!")
            return
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
        self.copytreeWidget.clear()
        self.load_tree_structure(self.root_path, self.treeWidget)


    def load_tree_structure(self, startroot_path, tree):

        for element in os.listdir(startroot_path):
            path_info = startroot_path + "/" + element
            if not os.path.isdir(path_info):
                parent_itm = TreeWidgetItem(tree, [os.path.basename(element)], path_info)
                parent_itm.setIcon(0, QIcon('assets/file.ico'))
            else:
                content = self.read_from_cfg(self.files_cfg)
                files = [r.split(" ")[0] for r in content]
                sec_lvls = [r.split(" ")[1] for r in content]
                if path_info in files:
                    level = sec_lvls[files.index(path_info)]
                else:
                    level = "1"
                    content.append(path_info + " " + level)
                    self.write_to_cfg(content, self.files_cfg)
                parent_itm = TreeWidgetItem(tree, [os.path.basename(element) + " " + level], path_info)
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


