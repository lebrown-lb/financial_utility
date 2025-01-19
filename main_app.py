#!/usr/bin/env python
import sys
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from xproclib.base_ui import Ui_mainWindow
from xproclib import catexp

class date:
    def __init__(self, year, month, day ,dstr, dfmt):
        self.year = year
        self.month = month
        self.day = day
        self.dstr = dstr
        self.dfmt = dfmt
        self.year_int = int(self.year)
        self.month_int = int(self.month)
        self.day_int = int(self.day)


class Main(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.actionOpen.setShortcut("Ctrl+o")
        self.ui.actionOpen.setStatusTip("Open Transaction csv")
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.setShortcut("Ctrl+q")
        self.ui.actionExit.setStatusTip("Exit Utility")
        self.ui.actionExit.triggered.connect(self.exit_util)
        self.ui.actionSave_Cat.setShortcut("Ctrl+Shift+s")
        self.ui.actionSave_Cat.setStatusTip("Save Categories")
        self.ui.actionSave_Cat.triggered.connect(self.save_cat)
        self.ui.actionSave_Data.setShortcut("Ctrl+s")
        self.ui.actionSave_Data.setStatusTip("Save Data")
        self.ui.actionSave_Data.triggered.connect(self.save_data)
        self.ui.actionPrint.setShortcut("Ctrl+p")
        self.ui.actionPrint.setStatusTip("Print Data")
        self.ui.actionPrint.triggered.connect(self.handlePrint)
        self.ui.actionPrint_Preview.setShortcut("Ctrl+Shift+p")
        self.ui.actionPrint_Preview.setStatusTip("Print Data")
        self.ui.actionPrint_Preview.triggered.connect(self.handlePreview)

        self.ui.csv_idx_upd.clicked.connect(self.upd_csv_indexs)
        self.ui.cat_add.clicked.connect(self.add_catagory)
        self.ui.cat_rmv.clicked.connect(self.rmv_catagory)
        self.ui.kword_add.clicked.connect(self.cat_kword_add)
        self.ui.upd_catg_exp.clicked.connect(self.upd_exp_catgories)
        self.ui.gen_sums.clicked.connect(self.gen_monthly_sums)
        self.ui.csv_date_flt_pb.clicked.connect(self.upd_csv_filter)
        self.ui.csv_date_flt_lsm_pb.clicked.connect(self.upd_csv_filter_lsm)

        self.ui.sort_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.cat_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.trans_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.ui.sort_table.itemSelectionChanged.connect(self.sort_sel_chg)
        self.ui.cat_table.itemSelectionChanged.connect(self.cat_sel_chg)
        self.ui.csv_date_flt_dfmt_le.setText("YYYY-MM-DD")
        self.ui.date_idx.setText("0")
        self.ui.desc_idx.setText("1")
        self.ui.in_idx.setText("3")
        self.ui.out_idx.setText("2")

        self.csv = None
        self.sort_exp = None
        self.exp_cat = []
        self.uncat_exp = None
        self.bwsr_txt = ''
        self.load_flg = False

    def open_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '.')[0]
        if filename == '':
            return
        self.ui.filePath_lbl.setText(filename)
        self.csv = catexp.prc_trans_csv(filename)
        c0 = int(self.ui.date_idx.text())
        c1 = int(self.ui.desc_idx.text())
        c2 = int(self.ui.in_idx.text())
        c3 = int(self.ui.out_idx.text())
        c = [c0, c1, c2, c3]

        self.upd_tbl(self.ui.trans_table, self.csv, c)
        self.sort_exp = catexp.prc_trans_srt(self.csv, c1, c3)
        self.upd_tbl(self.ui.sort_table, self.sort_exp, [0, 1, 2])
        self.uncat_exp = self.sort_exp
        self.upd_tbl(self.ui.uncat_exp_table, self.uncat_exp, [0, 1, 2])
        sd = self.find_first_date(self.csv[:, c0], self.ui.csv_date_flt_dfmt_le.text())
        ed = self.find_last_date(self.csv[:, c0], self.ui.csv_date_flt_dfmt_le.text())
        if sd is None or ed is None:
            self.load_flg = True
            return
        self.ui.csv_date_flt_sd_le.setText(sd.dstr)
        self.ui.csv_date_flt_ed_le.setText(ed.dstr)
        self.load_flg = True
        return

    def save_cat(self):
        fp = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open Directory', './')
        for obj in self.exp_cat:
            p = fp + '/' + obj.name
            f = open(p, 'w')
            f.write(obj.kwrds)
            f.close

    def save_data(self):
        fp = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '.')[0]
        print(fp)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = self.makeTableDocument()
        document.print_(printer)

    def makeTableDocument(self):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        rows = self.ui.month_sums_tbl.rowCount()
        columns = self.ui.month_sums_tbl.columnCount()
        cursor.insertText("********************************[MONTHLY SUMS]********************************\n\n")
        table = cursor.insertTable(rows + 1, columns)
        format = table.format()
        format.setHeaderRowCount(1)
        table.setFormat(format)
        format = cursor.blockCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        for column in range(columns):
            cursor.setCharFormat(format)
            cursor.insertText(
                self.ui.month_sums_tbl.horizontalHeaderItem(column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(rows):
            for column in range(columns):
                cursor.insertText(
                    self.ui.month_sums_tbl.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)

        cursor.movePosition(QtGui.QTextCursor.End)
        rows = self.ui.cat_table.rowCount()
        columns = self.ui.cat_table.columnCount()
        cursor.insertText("\n\n********************************[CATGORIES]********************************\n\n")
        table = cursor.insertTable(rows + 1, columns)
        format = table.format()
        format.setHeaderRowCount(1)
        table.setFormat(format)
        format = cursor.blockCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        for column in range(columns):
            cursor.setCharFormat(format)
            cursor.insertText(
                self.ui.cat_table.horizontalHeaderItem(column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(rows):
            for column in range(columns):
                cursor.insertText(
                    self.ui.cat_table.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)

        cursor.movePosition(QtGui.QTextCursor.End)
        rows = self.ui.uncat_exp_table.rowCount()
        columns = self.ui.uncat_exp_table.columnCount()
        cursor.insertText("\n\n********************[UNCATGORIZED EXPENSES]********************\n\n")
        table = cursor.insertTable(rows + 1, columns)
        format = table.format()
        format.setHeaderRowCount(1)
        table.setFormat(format)
        format = cursor.blockCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        for column in range(columns):
            cursor.setCharFormat(format)
            cursor.insertText(
                self.ui.uncat_exp_table.horizontalHeaderItem(column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(rows):
            for column in range(columns):
                cursor.insertText(
                    self.ui.uncat_exp_table.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        return document

    def exit_util(self):
        print("EXITING UTILITY")
        sys.exit()

    def upd_csv_indexs(self):
        if (self.load_flg):
            c0 = int(self.ui.date_idx.text())
            c1 = int(self.ui.desc_idx.text())
            c2 = int(self.ui.in_idx.text())
            c3 = int(self.ui.out_idx.text())
            c = [c0, c1, c2, c3]
            self.upd_tbl(self.ui.trans_table, self.csv, c)
        return

    def upd_csv_filter(self):
        dfmt = self.ui.csv_date_flt_dfmt_le.text()
        tmp_csv = []

        sd = self.parse_date(self.ui.csv_date_flt_sd_le.text(), dfmt) 
        ed = self.parse_date(self.ui.csv_date_flt_ed_le.text(), dfmt)

        if (sd != None) and (ed != None):
            cb = self.gen_calender_blk(sd, ed)
            
            c0 = int(self.ui.date_idx.text())
            c1 = int(self.ui.desc_idx.text())
            c2 = int(self.ui.in_idx.text())
            c3 = int(self.ui.out_idx.text())
            c = [c0, c1, c2, c3]
            
            for x in self.csv:
                if x[c0] in cb:
                    tmp_csv.append(x)
            self.csv = np.asarray(tmp_csv)

            self.upd_tbl(self.ui.trans_table, self.csv, c)
            self.sort_exp = catexp.prc_trans_srt(self.csv, c1, c3)
            self.upd_tbl(self.ui.sort_table, self.sort_exp, [0, 1, 2])
            self.uncat_exp = self.sort_exp
            self.upd_tbl(self.ui.uncat_exp_table, self.uncat_exp, [0, 1, 2])
            self.load_flg = True

            print("Generate Filter")

    def upd_csv_filter_lsm(self):
        dfmt = self.ui.csv_date_flt_dfmt_le.text()
        tmp_csv = []

        c0 = int(self.ui.date_idx.text())
        ed = self.find_last_date(self.csv[:,c0],dfmt)
        td = 1
        ty = ed.year_int
        tm = ed.month_int
        if  tm > 6:
            tm -= 6
        else:
            ty -= 1
            tm = 12 - (6 - tm)
        sd = self.build_date(ty, tm, td, dfmt)        

        if (sd != None) and (ed != None):
            self.ui.csv_date_flt_sd_le.setText(sd.dstr)
            cb = self.gen_calender_blk(sd, ed)
            for x in self.csv:
                if x[0] in cb:
                    tmp_csv.append(x)
            self.csv = np.asarray(tmp_csv)
            c0 = int(self.ui.date_idx.text())
            c1 = int(self.ui.desc_idx.text())
            c2 = int(self.ui.in_idx.text())
            c3 = int(self.ui.out_idx.text())
            c = [c0, c1, c2, c3]

            self.upd_tbl(self.ui.trans_table, self.csv, c)
            self.sort_exp = catexp.prc_trans_srt(self.csv, c1, c3)
            self.upd_tbl(self.ui.sort_table, self.sort_exp, [0, 1, 2])
            self.uncat_exp = self.sort_exp
            self.upd_tbl(self.ui.uncat_exp_table, self.uncat_exp, [0, 1, 2])
            self.load_flg = True

            print("Generate Filter")

    def gen_calender_blk(self, sdate, edate):
        mdays = [31,28,31,30,31,30,31,31,30,31,30,31]
        c = ["", "", ""]
        cb = []
        print("{} - {}".format(sdate.dstr, edate.dstr))

        dfmt = sdate.dfmt
        ds = "_-\\/"
        a = [dfmt.find(x) for x in [*ds]]
        b = [dfmt[x] for x in a if x >=0]
        k = b[0]
        df = dfmt.split(k)
        y_idx = [x for x in range(len(df)) if df[x].find('Y')>= 0]
        m_idx = [x for x in range(len(df)) if df[x].find('M')>= 0]
        d_idx = [x for x in range(len(df)) if df[x].find('D')>= 0]

        if ((len(df) != 3) or (len(y_idx) != 1) or (len(m_idx) != 1) or (len(d_idx) != 1)):
            print("DATE FORMAT INVAlID ")
            return None
        if (sdate.year_int > edate.year_int):
            print("INVALID START AND END DATE 1")
            return None
        if ((sdate.year_int == edate.year_int) and (sdate.month_int > edate.month_int)):
            print("INVALID START AND END DATE 2")
            return None
        if ((sdate.year_int == edate.year_int) and (sdate.month_int == edate.month_int) and (sdate.day_int > edate.day_int)):
            print("INVALID START AND END DATE 3")
            return None
        
        if ((sdate.month_int > 12) or (edate.month_int > 12)):
            print("INVALID START AND END DATE 4")
            return None
        sm_days = mdays[sdate.month_int - 1]
        em_days = mdays[edate.month_int - 1]
        if ((sdate.day_int > sm_days) or (edate.day_int > em_days)):
            print("INVALID START AND END DATE 5")
            return None

        cy = sdate.year_int
        cm = sdate.month_int
        cd = sdate.day_int
        cm_days = mdays[sdate.month_int - 1]
        cd_str = sdate.dstr

        while(cd_str != edate.dstr):

            c[y_idx[0]] = "{:04d}".format(cy)
            c[m_idx[0]] = "{:02d}".format(cm)
            c[d_idx[0]] = "{:02d}".format(cd)
            cd_str = "{0}{3}{1}{3}{2}".format(c[0], c[1], c[2], k)
            cb.append(cd_str)

            if (cd == cm_days):
                cd = 1
                if (cm == 12):
                    cy += 1
                    cm = 1
                    cm_days = mdays[cm -1]
                else:
                    cm += 1
                    cm_days = mdays[cm -1]
            else:
                cd += 1
        return cb

    def parse_date(self, dstr, dfmt):
        ds = "_-\\/"
        a = [dfmt.find(x) for x in [*ds]]
        b = [dfmt[x] for x in a if x >=0]
        k = b[0]
        df = dfmt.split(k)
        y_idx = [x for x in range(len(df)) if df[x].find('Y')>= 0]
        m_idx = [x for x in range(len(df)) if df[x].find('M')>= 0]
        d_idx = [x for x in range(len(df)) if df[x].find('D')>= 0]

        if ((len(df) != 3) or (len(y_idx) != 1) or (len(m_idx) != 1) or (len(d_idx) != 1)):
            print("DATE FORMAT INVAlID ")
            return None

        d = dstr.split(k)

        if (len(d) != 3):
            print("INVALID DATE")
            return None

        return date(d[y_idx[0]], d[m_idx[0]], d[d_idx[0]], dstr, dfmt) 

    def build_date(self, year, month, day, dfmt):
        c = ["", "", ""]
        ds = "_-\\/"
        a = [dfmt.find(x) for x in [*ds]]
        b = [dfmt[x] for x in a if x >=0]
        k = b[0]
        df = dfmt.split(k)
        y_idx = [x for x in range(len(df)) if df[x].find('Y')>= 0]
        m_idx = [x for x in range(len(df)) if df[x].find('M')>= 0]
        d_idx = [x for x in range(len(df)) if df[x].find('D')>= 0]

        if ((len(df) != 3) or (len(y_idx) != 1) or (len(m_idx) != 1) or (len(d_idx) != 1)):
            print("DATE FORMAT INVAlID ")
            return None

        c[y_idx[0]] = "{:04d}".format(year)
        c[m_idx[0]] = "{:02d}".format(month)
        c[d_idx[0]] = "{:02d}".format(day)
        cd_str = "{0}{3}{1}{3}{2}".format(c[0], c[1], c[2], k)

        return date(c[y_idx[0]], c[m_idx[0]],c[d_idx[0]], cd_str, dfmt)

    def find_first_date(self, adate, dfmt):
        ad = [self.parse_date(x, dfmt)for x in adate]
        if None in ad:
            return None
        #find earliest year
        y = min([x.year_int for x in ad])
        #filter for year
        ad_fy = [x for x in ad if x.year_int == y]
        #earliest month
        m = min([x.month_int for x in ad_fy])
        #filter for month
        ad_fm = [x for x in ad_fy if x.month_int == m]
        #earliest day
        d = min([x.day_int for x in ad_fm])
        #filter day
        ad_fd = [x for x in ad_fm if x.day_int == d]

        return ad_fd[0]

    def find_last_date(self, adate, dfmt):
        ad = [self.parse_date(x, dfmt)for x in adate]
        if None in ad:
            return None
        #find last year
        y = max([x.year_int for x in ad])
        #filter for year
        ad_fy = [x for x in ad if x.year_int == y]
        #last month
        m = max([x.month_int for x in ad_fy])
        #filter for month
        ad_fm = [x for x in ad_fy if x.month_int == m]
        #last day
        d = max([x.day_int for x in ad_fm])
        #filter day
        ad_fd = [x for x in ad_fm if x.day_int == d]

        return ad_fd[0]

    def upd_tbl(self, tbl, td, colmn_idxs):
        tbl.setRowCount(len(td))
        for i in range(len(td)):
            for x in range(len(colmn_idxs)):
                c = colmn_idxs[x]
                tbl.setItem(i, x, QtWidgets.QTableWidgetItem(td[i][c]))
        tbl.resizeColumnsToContents()
        return

    def sort_sel_chg(self):
        se = []
        idxs = self.ui.sort_table.selectionModel().selectedRows()
        x = int(self.ui.desc_idx.text())
        c0 = int(self.ui.date_idx.text())
        c1 = int(self.ui.desc_idx.text())
        c2 = int(self.ui.out_idx.text())
        if len(idxs) > 0:
            for i in idxs:
                e = self.sort_exp[i.row()]
                exps = catexp.prc_trans_merch_srch(self.csv, x, e[x])
                se.append(exps)
            exp = np.concatenate(se, axis=0)
            self.upd_tbl(self.ui.merch_table, exp, [c0, c1, c2])
        else:
            self.upd_tbl(self.ui.merch_table, [['', '', '']], [c0, c1, c2])
        return

    def cat_sel_chg(self):
        text = ''
        cexps = []
        idxs = self.ui.cat_table.selectionModel().selectedRows()
        if len(idxs) > 0:
            for i in idxs:
                text += self.exp_cat[i.row()].kwrds
                cexps += self.exp_cat[i.row()].exps
            self.ui.kword_tb.setText(text)
            self.upd_tbl(self.ui.cat_exp_tbl, cexps, [0, 1, 2])
        else:
            self.ui.kword_tb.clear()
            self.upd_tbl(self.ui.cat_exp_tbl, [['', '', '']], [0, 1, 2])
        return

    def add_catagory(self):
        rcnt = self.ui.cat_table.rowCount()
        idx = rcnt
        xc = []
        t = self.ui.cat_lst_le.text()
        if len(t) > 0:
            xc.append(catexp.ExpCat(t, '', 0, 0.00, []))
            print("CREATE NEW CAT")
        else:
            fp = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File', '.')[0]
            for p in fp:
                f = open(p, 'r')
                kwrds = f.read()
                f.close()
                n = p.split('/')[-1]
                xc.append(catexp.ExpCat(n, kwrds, 0, 0.00, []))
            print("LOAD CAT FILE")
        for x in xc:
            rcnt += 1
            idx = rcnt - 1
            self.ui.cat_table.setRowCount(rcnt)
            self.ui.cat_table.setItem(idx, 0, QtWidgets.QTableWidgetItem(x.name))
            self.ui.cat_table.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(x.trans)))
            self.ui.cat_table.setItem(idx, 2, QtWidgets.QTableWidgetItem(str(x.tcst)))
            self.exp_cat.append(x)
        print('LEN: {}'.format(len(self.exp_cat)))
        self.ui.cat_lst_le.clear()
        return

    def rmv_catagory(self):
        idxs = []
        sel_idxs = self.ui.cat_table.selectionModel().selectedRows()
        for mdx in sel_idxs:
            index = QtCore.QPersistentModelIndex(mdx)
            idxs.append(index)
        for index in idxs:
            self.ui.cat_table.removeRow(index.row())

        for i in sorted(sel_idxs, reverse=True):
            del self.exp_cat[i.row()]
        return

    def cat_kword_add(self):
        for xc in self.ui.cat_table.selectionModel().selectedRows():
            self.exp_cat[xc.row()].add_kwrd(self.ui.kword_le.text())
            self.ui.kword_tb.setText(self.exp_cat[xc.row()].kwrds)
        self.ui.kword_le.clear()

    def upd_exp_catgories(self):
        if (self.load_flg):
            self.uncat_exp = self.sort_exp
            cnt = 0
            for xobj in self.exp_cat:
                if (len(xobj.kwrds) > 0):
                    self.uncat_exp = catexp.prc_trans_exp_cat(self.uncat_exp, xobj)
                    self.ui.cat_table.setItem(cnt, 0, QtWidgets.QTableWidgetItem(xobj.name))
                    self.ui.cat_table.setItem(cnt, 1, QtWidgets.QTableWidgetItem(str(xobj.trans)))
                    self.ui.cat_table.setItem(cnt, 2, QtWidgets.QTableWidgetItem(str(np.round(xobj.tcst, decimals=2))))
                    cnt += 1
            self.upd_tbl(self.ui.uncat_exp_table, self.uncat_exp, [0, 1, 2])
        return

    def gen_monthly_sums(self):
        if (self.load_flg):
            a0 = int(self.ui.date_idx.text())
            a1 = int(self.ui.in_idx.text())
            a2 = int(self.ui.out_idx.text())
            mdat = catexp.prc_trans_msum(self.csv, a0, a1, a2)
            self.upd_tbl(self.ui.month_sums_tbl, mdat, [0, 1, 2, 3])
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
