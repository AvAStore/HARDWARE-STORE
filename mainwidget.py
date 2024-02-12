import sys
import DB
from PySide6.QtCore import Qt,QPointF
from PySide6.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem,QPushButton
from PySide6.QtGui import QFontDatabase,QPainter
from PySide6.QtCharts import (QBarSet, QChart, QChartView,QBarCategoryAxis,
                              QValueAxis,QStackedBarSeries)
from ui_main import Ui_MainWindow
import datetime
import Invoice
import Statistics

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized() # Maximize window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Coustom Main Window..")
        QFontDatabase.addApplicationFont("horyzen/Horyzen Regular.ttf")
        QFontDatabase.addApplicationFont("horyzen/Horyzen Light.ttf")
        QFontDatabase.addApplicationFont("horyzen/Horyzen Bold.ttf")
        QFontDatabase.addApplicationFont("horyzen/Horyzen Headline.ttf")
        QFontDatabase.addApplicationFont("horyzen/Horyzen Extra Bold.ttf")
        self.stackedWidget.setCurrentWidget(self.page)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.minimize)
        self.pushButton_3.clicked.connect(self.CashiePage)
        self.pushButton_4.clicked.connect(self.InventoryPage)
        self.pushButton_5.clicked.connect(self.TranactionPage)
        self.pushButton_6.clicked.connect(self.StaticPage)
        self.pushButton_7.clicked.connect(self.Loginpage)
        self.pushButton_8.clicked.connect(self.SettingPage)
        self.pushButton_11.clicked.connect(self.Coustmeradditem)
        self.pushButton_12.clicked.connect(self.additeamtoDB)
        self.pushButton_13.clicked.connect(self.edititem)
        self.pushButton_10.clicked.connect(self.placeOder)
        self.pushButton_15.clicked.connect(self.finishOder)
        self.pushButton_14.clicked.connect(self.deleteDB)
        self.pushButton_16.clicked.connect(self.AddUser)
        
        self.comboBox_3.textActivated.connect(self.selectitem)
        self.pushButton_9.clicked.connect(self.LogtoSoftware)
        self.comboBox_2.textActivated.connect(self.Custitemlist)
        self.comboBox_3.editTextChanged.connect(self.itemtexttrig)
        self.comboBox_2.editTextChanged.connect(self.Custclear)
        self.lineEdit_12.editingFinished.connect(self.Custitemlistbycode)
        self.lineEdit_12.textEdited.connect(self.Custitemreset)
        
        self.label_4.setText("")
        self.pushButton_15.setEnabled(False)

        self.Oderinglist={}
        self.totalPrice=0
        self.invoice_num=""
        self.LockSoftware()
        self.recommend()
        self.comboBox.textActivated.connect(lambda :self.label_4.setText(str(self.comboBox.currentText())))


    #Add Customer Ordering items to the database. Also check Customer Cash amount is higher than total price of the items.
    def placeOder(self):
        self.invoice_num = self.__generate_invoice_number()
        try:
            cashRecive=float(self.lineEdit_3.text())
            if cashRecive>=self.totalPrice:
                Database = DB.Database()
                Database.place_order(self.invoice_num,self. Oderinglist,self.totalPrice)
                Database.close_connection()
                self.label_8.setText(self.invoice_num)
                self.lineEdit_13.setText(str(round((cashRecive-self.totalPrice),2)))
                self.pushButton_11.setEnabled(False)
                self.pushButton_10.setEnabled(False)
                self.pushButton_15.setEnabled(True)
                self.lineEdit_3.setEnabled(False)
                self.tableWidget.setEnabled(False)

            else:
                self.popupMessage("Invalid Amount","Please Check the Amount.")
        except:
            self.popupMessage("Invalid Amount","Please Check the Amount.")
    
    #Create a Invoice PDF and clear Ordering list and Cashier page Input fields
    def finishOder(self):
        invose=Invoice.MainWindow()
        invose.save_pdf(self.invoice_num,self. Oderinglist,self.totalPrice)
        self.Oderinglist={}
        self.totalPrice=0
        self.invoice_num=""
        self.refreshOderlist()
        self.label_8.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_2.setText("")
        self.pushButton_11.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.pushButton_15.setEnabled(False)
        self.pushButton_10.setEnabled(True)
        self.tableWidget.setEnabled(True)

    #Create unique invoice number. This is a private function.
    def __generate_invoice_number(self):
        now = datetime.datetime.now()
        date_part = now.strftime("%Y%m%d")  # Format: YearMonthDay
        time_part = now.strftime("%H%M%S")  # Format: HourMinuteSecond
        invoice_number = f"INV-{date_part}-{time_part}"
        return invoice_number

    #Find item from the database, when user select item from the combobox in cashier page.
    def Custitemlist(self,itemname):
        Database = DB.Database()
        list=Database.get_item_data_ByName(itemname)
        ItmCo,ItmNa,ItmImg,Qnt,UBP,USP,Sup,Email=list[0]
        self.comboBox_2.setCurrentText(ItmNa)
        self.lineEdit_12.setText(ItmCo)
        self.lineEdit_5.setText(str(USP))
        Database.close_connection()

    #Add item to the customer ordering list. item stock quantity is also checking.
    def Coustmeradditem(self):
        Database = DB.Database()
        list=Database.get_item_data_ByCode(self.lineEdit_12.text())
        ItmCo,ItmNa,ItmImg,Qnt,UBP,USP,Sup,Email=list[0]
        Database.close_connection()
        try:
            buying_quantity = int(self.lineEdit_4.text())
            if buying_quantity <= 0:
                self.popupMessage("Invalid quantity",f"Please enter valid quantity maximum:{Qnt}")
            elif Qnt>=int(buying_quantity):
                self.Oderinglist.update({ItmCo:(buying_quantity,USP,ItmNa)})
                self.clearfields(1)
                self.refreshOderlist()
            else:
                self.popupMessage("Stock exceed",f"Only Have:{Qnt}")
        except:
            self.popupMessage("Invalid quantity",f"Please enter valid quantity maximum:{Qnt}")

    
    #Listing items in the Cashier page table.
    def refreshOderlist(self):
        OderRow=0
        buttonlist=[]
        self.totalPrice=0
        AllQuntity=0
        self.tableWidget.setRowCount(len(self.Oderinglist.items()))
        for x,y in self.Oderinglist.items():
            button = QPushButton("Remove")
            button.clicked.connect(lambda code=x, x3=x: self.DeleteOderiteamButton(x3))
            buttonlist.append(button)
            
            self.tableWidget.setItem(OderRow,0,QTableWidgetItem(x))
            self.tableWidget.setItem(OderRow,1,QTableWidgetItem(y[2]))
            self.tableWidget.setItem(OderRow,2,QTableWidgetItem(str(y[0])))
            self.tableWidget.setItem(OderRow,3,QTableWidgetItem(str(y[1])))
            self.tableWidget.setItem(OderRow,4,QTableWidgetItem(str(round(y[0]*y[1],2))))
            self.tableWidget.setCellWidget(OderRow,5,buttonlist[OderRow])
            self.totalPrice=self.totalPrice+round((y[0]*y[1]),2)
            AllQuntity+=y[0]
            OderRow+=1
        self.label_22.setText(str(self.totalPrice))
        self.lineEdit_2.setText(str(self.totalPrice))
        self.label_26.setText(str(len(self.Oderinglist.items())))
        self.label_24.setText(str(AllQuntity))
        recom=Statistics.Recommendations()
        self.textEdit.setText("")
        for i,item in enumerate(recom.get_recommend_items(self.Oderinglist)):
            self.textEdit.append(f"{i+1}.  {item}")

        

    #Deleting items from the coustomer's odering list.
    def DeleteOderiteamButton(self,code):
        del self.Oderinglist[code]
        self.refreshOderlist()  
        print(f"Deleteing:{code}")
        print(self.Oderinglist)

    #Search and load data to the cashier page combobox and line edit fields, when cashier enter item code. 
    def Custitemlistbycode(self):
        Database = DB.Database()
        list=Database.get_item_data_ByCode(self.lineEdit_12.text())
        ItmCo,ItmNa,ItmImg,Qnt,UBP,USP,Sup,Email=list[0]
        self.comboBox_2.setCurrentText(ItmNa)
        self.lineEdit_12.setText(ItmCo)
        self.lineEdit_5.setText(str(USP))
        Database.close_connection()

    #Clear comboboxes and line edit fields
    def Custitemreset(self):
        self.comboBox_2.setCurrentText("")
        self.lineEdit_5.setText("")

    #Clear  edit fields
    def Custclear(self):
        self.lineEdit_5.setText("")
        self.lineEdit_12.setText("")

    #Resize Casher page's table columns.
    def Cashertable(self):
        self.tableWidget.setColumnWidth(0,int(((self.tableWidget.frameGeometry().width())/6)))
        self.tableWidget.setColumnWidth(1,int(((self.tableWidget.frameGeometry().width())/6)))
        self.tableWidget.setColumnWidth(2,int(((self.tableWidget.frameGeometry().width())/6)))
        self.tableWidget.setColumnWidth(3,int(((self.tableWidget.frameGeometry().width())/6)))
        self.tableWidget.setColumnWidth(4,int(((self.tableWidget.frameGeometry().width())/6)))
        self.tableWidget.setColumnWidth(5,int(((self.tableWidget.frameGeometry().width())/6)))


    #Show items in side the Inventory page's table. Data added form the using SQL database
    def Showitemlisttable(self):
        self.tableWidget_2.setColumnWidth(0,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(1,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(2,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(3,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(4,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(5,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(6,int(((self.tableWidget_2.frameGeometry().width())/8)))
        self.tableWidget_2.setColumnWidth(7,int(((self.tableWidget_2.frameGeometry().width())/10)))


        Database = DB.Database()
        tabledata=Database.get_all_table_data()
        self.tableWidget_2.setRowCount(len(tabledata))
        Database.close_connection()
        buttonlist=[]
        cursorrow=0
        for row in tabledata:
            button = QPushButton("Edit")
            button.clicked.connect(lambda r=row, row=row: self.editButtonClicked(row))

            
            buttonlist.append(button)
            self.tableWidget_2.setItem(cursorrow,0,QTableWidgetItem(row[0]))
            self.tableWidget_2.setItem(cursorrow,1,QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(cursorrow,2,QTableWidgetItem(str(row[3])))
            self.tableWidget_2.setItem(cursorrow,3,QTableWidgetItem(str(row[4])))
            self.tableWidget_2.setItem(cursorrow,4,QTableWidgetItem(str(row[5])))
            self.tableWidget_2.setItem(cursorrow,5,QTableWidgetItem(str(row[6])))
            self.tableWidget_2.setItem(cursorrow,6,QTableWidgetItem(row[7]))
            self.tableWidget_2.setCellWidget(cursorrow,7,buttonlist[cursorrow])
            cursorrow+=1

    #Load item to the Inventory page edit button clicked.
    def editButtonClicked(self, row):
        self.comboBox_3.setCurrentText(row[1])
        self.selectitem(row[1])

    #Add items names to the dropdown list of the comboBox(Cashier page combobox and Inventory page combobox)
    def recommend(self):
        Database = DB.Database()
        self.comboBox_3.clear()
        self.comboBox_2.clear()
        self.comboBox_3.addItems(Database.get_table_data())
        self.comboBox_2.addItems(Database.get_table_data())
        Database.close_connection()
        self.comboBox_2.clearEditText()
        self.comboBox_3.clearEditText()


    def itemtexttrig(self):
        self.clearfields(0)
        self.pushButton_12.setEnabled(True)
        self.lineEdit_9.setEnabled(True)
    
    #Edit already presented data in the SQL Database.
    def edititem(self):
        Database = DB.Database()
        Database.update_data(self.lineEdit_9.text(),self.comboBox_3.currentText(),'NULL',int(self.lineEdit_6.text()),float(self.lineEdit_7.text()),float(self.lineEdit_8.text()),self.lineEdit_10.text(),self.lineEdit_11.text())
        Database.close_connection()
        self.clearfields()
        self.popupMessage("Successful","Item Edit successfully")
        self.Showitemlisttable()

    #Delete item from the database.
    def deleteDB(self):
        Database = DB.Database()
        Database.delete_data(self.lineEdit_9.text())
        Database.close_connection()
        self.clearfields()
        self.recommend()
        self.Showitemlisttable()
        self.popupMessage("Successful","Item Delete successfully")



    #Load data to the inventory page fields.
    def selectitem(self,itemname):
        Database = DB.Database()
        list=Database.get_item_data_ByName(itemname)
        ItmCo,ItmNa,ItmImg,Qnt,UBP,USP,Sup,Email=list[0]
        self.lineEdit_9.setText(ItmCo)
        self.lineEdit_6.setText(str(Qnt))
        self.lineEdit_7.setText(str(UBP))
        self.lineEdit_8.setText(str(USP))
        self.lineEdit_10.setText(Sup)
        self.lineEdit_11.setText(Email)
        Database.close_connection()
        self.pushButton_12.setEnabled(False)
        self.lineEdit_9.setEnabled(False)

    #Add items to SQL database when clicked Add button
    def additeamtoDB(self):
        Database = DB.Database()
        try:
            verify=Database.insert_item(self.lineEdit_9.text(),self.comboBox_3.currentText(),'NULL',int(self.lineEdit_6.text()),float(self.lineEdit_7.text()),float(self.lineEdit_8.text()),self.lineEdit_10.text(),self.lineEdit_11.text())
            if verify==1:
                self.clearfields()
                self.Showitemlisttable()
                self.popupMessage("Successful","Item added successfully")
                self.recommend()
            else:
                self.popupMessage("Database Error","Check Item code already exist!")
        except:
            self.popupMessage("Input Data error","Check Details")
        Database.close_connection()


    #when user clicked lock button. showing login page.
    def Loginpage(self):
        self.stackedWidget.setCurrentWidget(self.page)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_6.setStyleSheet("")
        self.pushButton_5.setStyleSheet("")
        self.pushButton_4.setStyleSheet("")
        self.LockSoftware()

    #Check user and Unlock Software
    def LogtoSoftware(self):
        Database=DB.Database()
        userVerify=Database.verify_password(self.comboBox.currentText(),self.lineEdit.text())
        
        if userVerify==1:
            self.frame_7.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.CashiePage()
        elif userVerify==2:
            self.frame_7.setEnabled(True)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.CashiePage()
        # if self.comboBox.currentText() == "Admin":
        #     if Database.verify_password(self.comboBox.currentText(),self.lineEdit.text()):
                
        else:
            self.popupMessage("Login Error","Password is incorrect.")
        Database.close_connection()
        # elif self.comboBox.currentText() =="Cashier":
        #     if self.lineEdit.text() == "Cash123":
        #         self.frame_7.setEnabled(True)
        #         self.pushButton_4.setEnabled(False)
        #         self.pushButton_5.setEnabled(False)
        #         self.pushButton_6.setEnabled(False)
        #         self.pushButton_8.setEnabled(False)
        #         self.CashiePage()
        #     else:
        #         self.popupMessage("Login Error","Password is incorrect.")
        self.lineEdit.setText("")

    #software side button panel disabling
    def LockSoftware(self):
        self.frame_7.setEnabled(False)
        self.comboBox.clear()
        Database=DB.Database()
        self.comboBox.addItems(Database.get_user_list(0))
        Database.close_connection()



    #User direct to the Cashier Page.
    def CashiePage(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.recommend()
        self.Cashertable()
        self.pushButton_3.setStyleSheet("QPushButton{\n"
        "background-color: rgb(42, 57, 66);\n"
        "border-left: 3px solid rgb(255, 61, 75);\n"
        "border-top-left-radius:30px;\n"
        "border-bottom-left-radius:30px;\n"
        "}")
        self.pushButton_4.setStyleSheet("")
        self.pushButton_5.setStyleSheet("")
        self.pushButton_6.setStyleSheet("")
        
                
    #User direct to the Inventory Page.
    def InventoryPage(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.Showitemlisttable()
        self.pushButton_4.setStyleSheet("QPushButton{\n"
        "background-color: rgb(42, 57, 66);\n"
        "border-left: 3px solid rgb(255, 61, 75);\n"
        "border-top-left-radius:30px;\n"
        "border-bottom-left-radius:30px;\n"
        "}")
        self.pushButton_3.setStyleSheet("")
        self.pushButton_5.setStyleSheet("")
        self.pushButton_6.setStyleSheet("")
   
    #User direct to the StaticPage Page.
    def StaticPage(self):
        self.pushButton_6.setStyleSheet("QPushButton{\n"
        "background-color: rgb(42, 57, 66);\n"
        "border-left: 3px solid rgb(255, 61, 75);\n"
        "border-top-left-radius:30px;\n"
        "border-bottom-left-radius:30px;\n"
        "}")
        self.pushButton_3.setStyleSheet("")
        self.pushButton_4.setStyleSheet("")
        self.pushButton_5.setStyleSheet("")
        self.stackedWidget.setCurrentWidget(self.page_5)

        self.showChart()

    #User direct to the issued Invoices data Page.
    def TranactionPage(self):
        self.pushButton_5.setStyleSheet("QPushButton{\n"
        "background-color: rgb(42, 57, 66);\n"
        "border-left: 3px solid rgb(255, 61, 75);\n"
        "border-top-left-radius:30px;\n"
        "border-bottom-left-radius:30px;\n"
        "}")
        self.pushButton_3.setStyleSheet("")
        self.pushButton_6.setStyleSheet("")
        self.pushButton_4.setStyleSheet("")
        self.stackedWidget.setCurrentWidget(self.page_4)

        self.Transaction()

    #Minimuizing the software
    def minimize(self):
        self.showMinimized()

    
    #Close the software
    def close(self):
        sys.exit()
    
    #Clear ComboBoxes and line edit fields.
    def clearfields(self,NameWant=1):
        self.lineEdit_9.setText('')
        if NameWant == 1:
            self.comboBox_3.clearEditText()
            self.comboBox_2.clearEditText()
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')

        self.lineEdit_12.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')

        
    #Showing Popup Messages. 
    def popupMessage(self,Messege,Messege1):
        message=QMessageBox()
        ret=QMessageBox.information(self,Messege,Messege1,QMessageBox.Ok)
        if ret ==QMessageBox.Ok:
            print(Messege1)
            print("User choose OK")
    
    #Show Invoices by using the SQL Database and show that data in the Table Window.
    def Transaction(self):
        self.tableWidget_4.setColumnWidth(0,int(((self.tableWidget_4.frameGeometry().width())/5)))
        self.tableWidget_4.setColumnWidth(1,int(((self.tableWidget_4.frameGeometry().width())/5)))
        self.tableWidget_4.setColumnWidth(2,int(((self.tableWidget_4.frameGeometry().width())/5)))
        self.tableWidget_4.setColumnWidth(3,int(((self.tableWidget_4.frameGeometry().width())/5)))
        self.tableWidget_4.setColumnWidth(4,int(((self.tableWidget_4.frameGeometry().width())/5)))


        Database=DB.Database()
        Customers=Database.get_Customers_data()
        self.tableWidget_4.setRowCount(len(Customers))
        Database.close_connection()
        buttonlist=[]
        cursorrow=0
        for row in Customers:
            button = QPushButton("View Details")
            button.clicked.connect(lambda r=row, row=row: self.InvoiceData(row))           
            buttonlist.append(button)
            self.tableWidget_4.setItem(cursorrow,0,QTableWidgetItem(row[0]))
            self.tableWidget_4.setItem(cursorrow,1,QTableWidgetItem(row[1]))
            self.tableWidget_4.setItem(cursorrow,2,QTableWidgetItem(row[2]))
            self.tableWidget_4.setItem(cursorrow,3,QTableWidgetItem(str(row[3])))
            self.tableWidget_4.setCellWidget(cursorrow,4,buttonlist[cursorrow])
            cursorrow+=1


    #Show Respective Invoice data by using the SQL Database and show that data in the Table Window.
    def InvoiceData(self,row):
        self.tableWidget_3.setColumnWidth(0,int(((self.tableWidget_3.frameGeometry().width())/6)))
        self.tableWidget_3.setColumnWidth(1,int(((self.tableWidget_3.frameGeometry().width())/6)))
        self.tableWidget_3.setColumnWidth(2,int(((self.tableWidget_3.frameGeometry().width())/6)))
        self.tableWidget_3.setColumnWidth(3,int(((self.tableWidget_3.frameGeometry().width())/6)))
        self.tableWidget_3.setColumnWidth(4,int(((self.tableWidget_3.frameGeometry().width())/6)))

        Database=DB.Database()
        self.label_32.setText(f"Invoice Number: {row[0]}")
        oderData=(Database.get_Order_data(row[0]))
        self.tableWidget_3.setRowCount(len(oderData))
        for i,num in enumerate(oderData):
            iteamdata=Database.get_item_data_ByCode(num[2])
            iteamname=iteamdata[0]
            self.tableWidget_3.setItem(i,0,QTableWidgetItem(num[2]))
            self.tableWidget_3.setItem(i,1,QTableWidgetItem(iteamname[1]))
            self.tableWidget_3.setItem(i,2,QTableWidgetItem(str(num[3])))
            self.tableWidget_3.setItem(i,3,QTableWidgetItem(str(num[4])))
            self.tableWidget_3.setItem(i,4,QTableWidgetItem(str(num[3]*num[4])))
        Database.close_connection()


    #Showing Chart in side the Statistic page
    def showChart(self):
        chart_view = QChartView(self.create_Bar_chart())
        chart_view.chart().setTheme(QChart.ChartThemeDark)
        chart_view.chart().setAnimationOptions(QChart.AllAnimations)
        chart_view.setRenderHint(QPainter.Antialiasing,True)
        self.gridLayout_5.addWidget(chart_view,0,0,1,1)

    #Creating Bar chart and return that chart to showChart function
    def create_Bar_chart(self):
        chart = QChart()
        chart.setTitle("Pofit vs Data")

        Database=DB.Database()
        Customers=Database.get_graph_data_DateVs("profit")
        Database.close_connection()
        data_table = []  # Initialize the table with an empty list
        dates=[]
        for Charts in range(0,1):
            ChartData=[]
            for i,Chartpoints in enumerate(Customers):
                val=(QPointF(i, Customers[Chartpoints]), Chartpoints)
                ChartData.append((val))
                dates.append(Chartpoints)
                # print(Chartpoints)
            data_table.append(ChartData)

        chart = QChart()
        chart.setTitle("Bar chart")

        series = QStackedBarSeries(chart)

        for i in range(len(data_table)):
            barset = QBarSet(f"Profit")
            for data in data_table[i]:
                barset.append(data[0].y())
            series.append(barset)

        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(dates)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)
        
        axis_y = QValueAxis()
        axis_y.setRange(0, max(Customers.values())+(max(Customers.values())/10))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)
        return chart

    def SettingPage(self):
        self.stackedWidget.setCurrentWidget(self.page_6)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_3.setStyleSheet("")
        self.pushButton_4.setStyleSheet("")
        self.pushButton_5.setStyleSheet("")
        self.tableWidget_5.setColumnWidth(0,int(((self.tableWidget_5.frameGeometry().width())/2)))
        self.tableWidget_5.setColumnWidth(1,int(((self.tableWidget_5.frameGeometry().width())/2)))
        
        DataBase=DB.Database()
        userlist=DataBase.get_user_list(1)
        
        self.tableWidget_5.setRowCount(len(userlist))
        
        for row,user in enumerate(userlist):
            role = "Super User" if userlist[user] == 1 else "Cashier"
            self.tableWidget_5.setItem(row, 0, QTableWidgetItem(user))
            self.tableWidget_5.setItem(row, 1, QTableWidgetItem(role))
        
        DataBase.close_connection()

    def AddUser(self):
        userName=self.lineEdit_14.text()
        password_1=self.lineEdit_15.text()
        password_2=self.lineEdit_16.text()

        if password_2==password_1 and userName != "":
            Database=DB.Database()
            if Database.save_user(userName,password_2,int(self.radioButton.isChecked())+1):
                self.popupMessage("Saved Successfully","You can login with username")
                self.lineEdit_14.setText("")
                self.lineEdit_15.setText("")
                self.lineEdit_16.setText("")
                self.SettingPage()
            else:
                self.popupMessage("Saved Failed", "Username already exist")
            Database.close_connection()
        else:
            self.popupMessage("Saved Failed", "User name or Password is not match")


            # Database=DB.Database()
            # if self.radioButton_2.isChecked():
            #     Database.save_user(userName,password_2,1)
            # else:
            #     Database.save_user(userName,password_2,2)
            # Database.close_connection()
            


