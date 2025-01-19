# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finac_hist_util.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(949, 783)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.trans_tab = QtWidgets.QWidget()
        self.trans_tab.setObjectName("trans_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.trans_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.trans_tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.trans_table = QtWidgets.QTableWidget(self.splitter)
        self.trans_table.setObjectName("trans_table")
        self.trans_table.setColumnCount(4)
        self.trans_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.trans_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.trans_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.trans_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.trans_table.setHorizontalHeaderItem(3, item)
        self.trans_table.horizontalHeader().setCascadingSectionResizes(True)
        self.trans_table.horizontalHeader().setStretchLastSection(False)
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.csv_idx_vl = QtWidgets.QVBoxLayout()
        self.csv_idx_vl.setObjectName("csv_idx_vl")
        self.csv_idx_lbl = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.csv_idx_lbl.setFont(font)
        self.csv_idx_lbl.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.csv_idx_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.csv_idx_lbl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.csv_idx_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.csv_idx_lbl.setObjectName("csv_idx_lbl")
        self.csv_idx_vl.addWidget(self.csv_idx_lbl)
        self.csv_idx_hl0 = QtWidgets.QHBoxLayout()
        self.csv_idx_hl0.setObjectName("csv_idx_hl0")
        self.date_idx_lbl = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_idx_lbl.sizePolicy().hasHeightForWidth())
        self.date_idx_lbl.setSizePolicy(sizePolicy)
        self.date_idx_lbl.setMinimumSize(QtCore.QSize(65, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_idx_lbl.setFont(font)
        self.date_idx_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.date_idx_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.date_idx_lbl.setObjectName("date_idx_lbl")
        self.csv_idx_hl0.addWidget(self.date_idx_lbl)
        self.date_idx = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_idx.sizePolicy().hasHeightForWidth())
        self.date_idx.setSizePolicy(sizePolicy)
        self.date_idx.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.date_idx.setFont(font)
        self.date_idx.setMaxLength(1)
        self.date_idx.setAlignment(QtCore.Qt.AlignCenter)
        self.date_idx.setObjectName("date_idx")
        self.csv_idx_hl0.addWidget(self.date_idx)
        self.csv_idx_vl.addLayout(self.csv_idx_hl0)
        self.csv_idx_hl1 = QtWidgets.QHBoxLayout()
        self.csv_idx_hl1.setObjectName("csv_idx_hl1")
        self.desc_idx_lbl = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_idx_lbl.sizePolicy().hasHeightForWidth())
        self.desc_idx_lbl.setSizePolicy(sizePolicy)
        self.desc_idx_lbl.setMinimumSize(QtCore.QSize(65, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.desc_idx_lbl.setFont(font)
        self.desc_idx_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.desc_idx_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.desc_idx_lbl.setObjectName("desc_idx_lbl")
        self.csv_idx_hl1.addWidget(self.desc_idx_lbl)
        self.desc_idx = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desc_idx.sizePolicy().hasHeightForWidth())
        self.desc_idx.setSizePolicy(sizePolicy)
        self.desc_idx.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.desc_idx.setFont(font)
        self.desc_idx.setMaxLength(1)
        self.desc_idx.setAlignment(QtCore.Qt.AlignCenter)
        self.desc_idx.setObjectName("desc_idx")
        self.csv_idx_hl1.addWidget(self.desc_idx)
        self.csv_idx_vl.addLayout(self.csv_idx_hl1)
        self.csv_idx_hl2 = QtWidgets.QHBoxLayout()
        self.csv_idx_hl2.setObjectName("csv_idx_hl2")
        self.in_idx_lbl = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_idx_lbl.sizePolicy().hasHeightForWidth())
        self.in_idx_lbl.setSizePolicy(sizePolicy)
        self.in_idx_lbl.setMinimumSize(QtCore.QSize(65, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.in_idx_lbl.setFont(font)
        self.in_idx_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.in_idx_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.in_idx_lbl.setObjectName("in_idx_lbl")
        self.csv_idx_hl2.addWidget(self.in_idx_lbl)
        self.in_idx = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_idx.sizePolicy().hasHeightForWidth())
        self.in_idx.setSizePolicy(sizePolicy)
        self.in_idx.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.in_idx.setFont(font)
        self.in_idx.setMaxLength(1)
        self.in_idx.setAlignment(QtCore.Qt.AlignCenter)
        self.in_idx.setObjectName("in_idx")
        self.csv_idx_hl2.addWidget(self.in_idx)
        self.csv_idx_vl.addLayout(self.csv_idx_hl2)
        self.csv_idx_hl3 = QtWidgets.QHBoxLayout()
        self.csv_idx_hl3.setObjectName("csv_idx_hl3")
        self.out_idx_lbl = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_idx_lbl.sizePolicy().hasHeightForWidth())
        self.out_idx_lbl.setSizePolicy(sizePolicy)
        self.out_idx_lbl.setMinimumSize(QtCore.QSize(65, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.out_idx_lbl.setFont(font)
        self.out_idx_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.out_idx_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.out_idx_lbl.setObjectName("out_idx_lbl")
        self.csv_idx_hl3.addWidget(self.out_idx_lbl)
        self.out_idx = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_idx.sizePolicy().hasHeightForWidth())
        self.out_idx.setSizePolicy(sizePolicy)
        self.out_idx.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.out_idx.setFont(font)
        self.out_idx.setMaxLength(1)
        self.out_idx.setAlignment(QtCore.Qt.AlignCenter)
        self.out_idx.setObjectName("out_idx")
        self.csv_idx_hl3.addWidget(self.out_idx)
        self.csv_idx_vl.addLayout(self.csv_idx_hl3)
        self.csv_idx_upd = QtWidgets.QPushButton(self.frame)
        self.csv_idx_upd.setObjectName("csv_idx_upd")
        self.csv_idx_vl.addWidget(self.csv_idx_upd)
        self.verticalLayout_3.addLayout(self.csv_idx_vl)
        self.csv_date_flt_vl = QtWidgets.QVBoxLayout()
        self.csv_date_flt_vl.setObjectName("csv_date_flt_vl")
        self.csv_date_flt_lbl = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.csv_date_flt_lbl.setFont(font)
        self.csv_date_flt_lbl.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.csv_date_flt_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.csv_date_flt_lbl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.csv_date_flt_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.csv_date_flt_lbl.setObjectName("csv_date_flt_lbl")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_lbl)
        self.csv_date_flt_dfmt_lbl = QtWidgets.QLabel(self.frame)
        self.csv_date_flt_dfmt_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.csv_date_flt_dfmt_lbl.setObjectName("csv_date_flt_dfmt_lbl")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_dfmt_lbl)
        self.csv_date_flt_dfmt_le = QtWidgets.QLineEdit(self.frame)
        self.csv_date_flt_dfmt_le.setObjectName("csv_date_flt_dfmt_le")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_dfmt_le)
        self.csv_date_flt_sd_lbl = QtWidgets.QLabel(self.frame)
        self.csv_date_flt_sd_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.csv_date_flt_sd_lbl.setObjectName("csv_date_flt_sd_lbl")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_sd_lbl)
        self.csv_date_flt_sd_le = QtWidgets.QLineEdit(self.frame)
        self.csv_date_flt_sd_le.setObjectName("csv_date_flt_sd_le")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_sd_le)
        self.csv_date_flt_ed_lbl = QtWidgets.QLabel(self.frame)
        self.csv_date_flt_ed_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.csv_date_flt_ed_lbl.setObjectName("csv_date_flt_ed_lbl")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_ed_lbl)
        self.csv_date_flt_ed_le = QtWidgets.QLineEdit(self.frame)
        self.csv_date_flt_ed_le.setObjectName("csv_date_flt_ed_le")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_ed_le)
        self.csv_date_flt_pb = QtWidgets.QPushButton(self.frame)
        self.csv_date_flt_pb.setObjectName("csv_date_flt_pb")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_pb)
        self.csv_date_flt_lsm_pb = QtWidgets.QPushButton(self.frame)
        self.csv_date_flt_lsm_pb.setObjectName("csv_date_flt_lsm_pb")
        self.csv_date_flt_vl.addWidget(self.csv_date_flt_lsm_pb)
        self.verticalLayout_3.addLayout(self.csv_date_flt_vl)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.trans_tab, "")
        self.sort_tab = QtWidgets.QWidget()
        self.sort_tab.setObjectName("sort_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sort_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.sort_tab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.sort_table_vl = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.sort_table_vl.setContentsMargins(0, 0, 0, 0)
        self.sort_table_vl.setObjectName("sort_table_vl")
        self.sort_table_lbl = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.sort_table_lbl.setFont(font)
        self.sort_table_lbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.sort_table_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sort_table_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_table_lbl.setObjectName("sort_table_lbl")
        self.sort_table_vl.addWidget(self.sort_table_lbl)
        self.sort_table = QtWidgets.QTableWidget(self.layoutWidget)
        self.sort_table.setObjectName("sort_table")
        self.sort_table.setColumnCount(3)
        self.sort_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sort_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sort_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sort_table.setHorizontalHeaderItem(2, item)
        self.sort_table.horizontalHeader().setCascadingSectionResizes(True)
        self.sort_table.horizontalHeader().setStretchLastSection(False)
        self.sort_table_vl.addWidget(self.sort_table)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.merch_table_vl = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.merch_table_vl.setContentsMargins(0, 0, 0, 0)
        self.merch_table_vl.setObjectName("merch_table_vl")
        self.merch_tabke_lbl = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.merch_tabke_lbl.setFont(font)
        self.merch_tabke_lbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.merch_tabke_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.merch_tabke_lbl.setLineWidth(2)
        self.merch_tabke_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.merch_tabke_lbl.setObjectName("merch_tabke_lbl")
        self.merch_table_vl.addWidget(self.merch_tabke_lbl)
        self.merch_table = QtWidgets.QTableWidget(self.layoutWidget1)
        self.merch_table.setColumnCount(3)
        self.merch_table.setObjectName("merch_table")
        self.merch_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.merch_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.merch_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.merch_table.setHorizontalHeaderItem(2, item)
        self.merch_table.horizontalHeader().setCascadingSectionResizes(True)
        self.merch_table.horizontalHeader().setStretchLastSection(False)
        self.merch_table_vl.addWidget(self.merch_table)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.sort_tab, "")
        self.cat_tab = QtWidgets.QWidget()
        self.cat_tab.setObjectName("cat_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.cat_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cat_display_splitter = QtWidgets.QSplitter(self.cat_tab)
        self.cat_display_splitter.setOrientation(QtCore.Qt.Vertical)
        self.cat_display_splitter.setObjectName("cat_display_splitter")
        self.cat_sub_splitter = QtWidgets.QSplitter(self.cat_display_splitter)
        self.cat_sub_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.cat_sub_splitter.setObjectName("cat_sub_splitter")
        self.layoutWidget2 = QtWidgets.QWidget(self.cat_sub_splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.cat_lst_gl = QtWidgets.QGridLayout(self.layoutWidget2)
        self.cat_lst_gl.setContentsMargins(0, 0, 0, 0)
        self.cat_lst_gl.setObjectName("cat_lst_gl")
        self.cat_lst_le = QtWidgets.QLineEdit(self.layoutWidget2)
        self.cat_lst_le.setObjectName("cat_lst_le")
        self.cat_lst_gl.addWidget(self.cat_lst_le, 2, 0, 1, 1)
        self.cat_lst_lbl = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cat_lst_lbl.setFont(font)
        self.cat_lst_lbl.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.cat_lst_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.cat_lst_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cat_lst_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.cat_lst_lbl.setObjectName("cat_lst_lbl")
        self.cat_lst_gl.addWidget(self.cat_lst_lbl, 0, 0, 1, 4)
        self.cat_table = QtWidgets.QTableWidget(self.layoutWidget2)
        self.cat_table.setObjectName("cat_table")
        self.cat_table.setColumnCount(3)
        self.cat_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cat_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cat_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cat_table.setHorizontalHeaderItem(2, item)
        self.cat_lst_gl.addWidget(self.cat_table, 1, 0, 1, 3)
        self.cat_add = QtWidgets.QPushButton(self.layoutWidget2)
        self.cat_add.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.cat_add.setFont(font)
        self.cat_add.setObjectName("cat_add")
        self.cat_lst_gl.addWidget(self.cat_add, 2, 2, 1, 1)
        self.cat_rmv = QtWidgets.QPushButton(self.layoutWidget2)
        self.cat_rmv.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.cat_rmv.setFont(font)
        self.cat_rmv.setObjectName("cat_rmv")
        self.cat_lst_gl.addWidget(self.cat_rmv, 2, 1, 1, 1)
        self.tabWidget1 = QtWidgets.QTabWidget(self.cat_sub_splitter)
        self.tabWidget1.setObjectName("tabWidget1")
        self.tw_kwrds = QtWidgets.QWidget()
        self.tw_kwrds.setObjectName("tw_kwrds")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tw_kwrds)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.kword_gl = QtWidgets.QGridLayout()
        self.kword_gl.setObjectName("kword_gl")
        self.kword_add = QtWidgets.QPushButton(self.tw_kwrds)
        self.kword_add.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.kword_add.setFont(font)
        self.kword_add.setObjectName("kword_add")
        self.kword_gl.addWidget(self.kword_add, 4, 1, 1, 1)
        self.kword_le = QtWidgets.QLineEdit(self.tw_kwrds)
        self.kword_le.setObjectName("kword_le")
        self.kword_gl.addWidget(self.kword_le, 4, 0, 1, 1)
        self.kword_lbl = QtWidgets.QLabel(self.tw_kwrds)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.kword_lbl.setFont(font)
        self.kword_lbl.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.kword_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.kword_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.kword_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.kword_lbl.setObjectName("kword_lbl")
        self.kword_gl.addWidget(self.kword_lbl, 0, 0, 1, 2)
        self.kword_tb = QtWidgets.QTextBrowser(self.tw_kwrds)
        self.kword_tb.setObjectName("kword_tb")
        self.kword_gl.addWidget(self.kword_tb, 1, 0, 1, 2)
        self.verticalLayout_5.addLayout(self.kword_gl)
        self.tabWidget1.addTab(self.tw_kwrds, "")
        self.tw_exps = QtWidgets.QWidget()
        self.tw_exps.setObjectName("tw_exps")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tw_exps)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cat_exp_tbl = QtWidgets.QTableWidget(self.tw_exps)
        self.cat_exp_tbl.setObjectName("cat_exp_tbl")
        self.cat_exp_tbl.setColumnCount(3)
        self.cat_exp_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cat_exp_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cat_exp_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cat_exp_tbl.setHorizontalHeaderItem(2, item)
        self.verticalLayout_8.addWidget(self.cat_exp_tbl)
        self.tabWidget1.addTab(self.tw_exps, "")
        self.layoutWidget3 = QtWidgets.QWidget(self.cat_display_splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.uncat_exp_vl = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.uncat_exp_vl.setContentsMargins(0, 0, 0, 0)
        self.uncat_exp_vl.setObjectName("uncat_exp_vl")
        self.uncat_exp_lbl = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.uncat_exp_lbl.setFont(font)
        self.uncat_exp_lbl.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.uncat_exp_lbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.uncat_exp_lbl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uncat_exp_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.uncat_exp_lbl.setObjectName("uncat_exp_lbl")
        self.uncat_exp_vl.addWidget(self.uncat_exp_lbl)
        self.uncat_exp_table = QtWidgets.QTableWidget(self.layoutWidget3)
        self.uncat_exp_table.setObjectName("uncat_exp_table")
        self.uncat_exp_table.setColumnCount(3)
        self.uncat_exp_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.uncat_exp_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uncat_exp_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uncat_exp_table.setHorizontalHeaderItem(2, item)
        self.uncat_exp_table.horizontalHeader().setCascadingSectionResizes(True)
        self.uncat_exp_table.horizontalHeader().setStretchLastSection(False)
        self.uncat_exp_vl.addWidget(self.uncat_exp_table)
        self.verticalLayout_9.addWidget(self.cat_display_splitter)
        self.upd_catg_exp = QtWidgets.QPushButton(self.cat_tab)
        self.upd_catg_exp.setObjectName("upd_catg_exp")
        self.verticalLayout_9.addWidget(self.upd_catg_exp)
        self.tabWidget.addTab(self.cat_tab, "")
        self.sum_tab = QtWidgets.QWidget()
        self.sum_tab.setObjectName("sum_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.sum_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.month_sums_tbl = QtWidgets.QTableWidget(self.sum_tab)
        self.month_sums_tbl.setObjectName("month_sums_tbl")
        self.month_sums_tbl.setColumnCount(4)
        self.month_sums_tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.month_sums_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.month_sums_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.month_sums_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.month_sums_tbl.setHorizontalHeaderItem(3, item)
        self.verticalLayout_6.addWidget(self.month_sums_tbl)
        self.gen_sums = QtWidgets.QPushButton(self.sum_tab)
        self.gen_sums.setObjectName("gen_sums")
        self.verticalLayout_6.addWidget(self.gen_sums)
        self.tabWidget.addTab(self.sum_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.filePath_lbl = QtWidgets.QLabel(self.centralwidget)
        self.filePath_lbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.filePath_lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.filePath_lbl.setTextFormat(QtCore.Qt.PlainText)
        self.filePath_lbl.setObjectName("filePath_lbl")
        self.verticalLayout.addWidget(self.filePath_lbl)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Cat = QtWidgets.QAction(mainWindow)
        self.actionSave_Cat.setObjectName("actionSave_Cat")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_Data = QtWidgets.QAction(mainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionPrint = QtWidgets.QAction(mainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtWidgets.QAction(mainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Cat)
        self.menuFile.addAction(self.actionSave_Data)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Financial History Utility"))
        item = self.trans_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "DATE"))
        item = self.trans_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "DESC"))
        item = self.trans_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "IN"))
        item = self.trans_table.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "OUT"))
        self.csv_idx_lbl.setText(_translate("mainWindow", "CSV INDEX\'S"))
        self.date_idx_lbl.setText(_translate("mainWindow", "DATE"))
        self.date_idx.setText(_translate("mainWindow", "0"))
        self.desc_idx_lbl.setText(_translate("mainWindow", "DESC"))
        self.desc_idx.setText(_translate("mainWindow", "2"))
        self.in_idx_lbl.setText(_translate("mainWindow", "IN"))
        self.in_idx.setText(_translate("mainWindow", "3"))
        self.out_idx_lbl.setText(_translate("mainWindow", "OUT"))
        self.out_idx.setText(_translate("mainWindow", "4"))
        self.csv_idx_upd.setText(_translate("mainWindow", "UPDATE"))
        self.csv_date_flt_lbl.setText(_translate("mainWindow", "CSV DATE FILTER"))
        self.csv_date_flt_dfmt_lbl.setText(_translate("mainWindow", "Date Format"))
        self.csv_date_flt_sd_lbl.setText(_translate("mainWindow", "Start Date"))
        self.csv_date_flt_ed_lbl.setText(_translate("mainWindow", "End Date"))
        self.csv_date_flt_pb.setText(_translate("mainWindow", "FILTER"))
        self.csv_date_flt_lsm_pb.setText(_translate("mainWindow", "LAST 6 MONTHS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trans_tab), _translate("mainWindow", "TRANS"))
        self.sort_table_lbl.setText(_translate("mainWindow", "SORTED EXPENSES"))
        item = self.sort_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "TRANS"))
        item = self.sort_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "DESC"))
        item = self.sort_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "COST"))
        self.merch_tabke_lbl.setText(_translate("mainWindow", "MERCHANT BREAKDOWN"))
        item = self.merch_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "DATE"))
        item = self.merch_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "DESC"))
        item = self.merch_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "COST"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sort_tab), _translate("mainWindow", "SORT"))
        self.cat_lst_lbl.setText(_translate("mainWindow", "CATEGORY LIST"))
        item = self.cat_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "CAT"))
        item = self.cat_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "TRANS"))
        item = self.cat_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "TOTAL"))
        self.cat_add.setText(_translate("mainWindow", "+"))
        self.cat_rmv.setText(_translate("mainWindow", "-"))
        self.tabWidget1.setToolTip(_translate("mainWindow", "<html><head/><body><p>EXPENSES</p></body></html>"))
        self.tabWidget1.setWhatsThis(_translate("mainWindow", "<html><head/><body><p>KEWORDS</p></body></html>"))
        self.kword_add.setText(_translate("mainWindow", "+"))
        self.kword_lbl.setText(_translate("mainWindow", "KEWORDS (CONTENTS)"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tw_kwrds), _translate("mainWindow", "KEYWORDS"))
        item = self.cat_exp_tbl.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "TRANS"))
        item = self.cat_exp_tbl.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "DESC"))
        item = self.cat_exp_tbl.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "COST"))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tw_exps), _translate("mainWindow", "EXPENSES"))
        self.uncat_exp_lbl.setText(_translate("mainWindow", "UNCATAGORIZED"))
        item = self.uncat_exp_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "TRANS"))
        item = self.uncat_exp_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "DESC"))
        item = self.uncat_exp_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "COST"))
        self.upd_catg_exp.setText(_translate("mainWindow", "UPDATE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cat_tab), _translate("mainWindow", "CAT"))
        item = self.month_sums_tbl.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "MONTH"))
        item = self.month_sums_tbl.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "FUNDS IN"))
        item = self.month_sums_tbl.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "FUNDS OUT"))
        item = self.month_sums_tbl.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "NET"))
        self.gen_sums.setText(_translate("mainWindow", "Generate Monthly Sums"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sum_tab), _translate("mainWindow", "SUM"))
        self.filePath_lbl.setText(_translate("mainWindow", " NO FILE LOADED"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionSave_Cat.setText(_translate("mainWindow", "Save Categories"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionSave_Data.setText(_translate("mainWindow", "Save Data"))
        self.actionPrint.setText(_translate("mainWindow", "Print"))
        self.actionPrint_Preview.setText(_translate("mainWindow", "Print Preview"))
