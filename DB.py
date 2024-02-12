import sqlite3
from typing import Union
from datetime import datetime
import hashlib
import os

class Database:
    def __init__(self,db_name = 'database.db'): #Create Database and Create Table if does not exists.
        if not os.path.exists("database.db"):
            does_not_exists = True
        else:
            does_not_exists = False
        self.database_connection = sqlite3.connect(db_name)
        self.cursor = self.database_connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Stock (ItemCode TEXT PRIMARY KEY, ItemName TEXT,ItemImage BLOB,Quantity INTEGER, UnitBuyingPrice REAL, UnitSellingPrice REAL, SupplierName TEXT, SupplierEmail TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Customers (InvoiceNumber TEXT PRIMARY KEY,Date TEXT,Time TEXT,TotalAmount REAL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Orders (ID INTEGER PRIMARY KEY, InvoiceNumber TEXT, ItemCode TEXT, Quantity INTEGER, SellingPrice REAL, FOREIGN KEY (ItemCode) REFERENCES Stock(ItemCode))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Login (ID INTEGER PRIMARY KEY, UserName TEXT, Password TEXT, Priority INTEGER)")
        if does_not_exists:
            self.cursor.execute("INSERT INTO Login (UserName, Password, Priority) VALUES ('admin','4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2','1')")
        self.database_connection.commit()
    
    def insert_item(self, ItemCode : str, ItemName: str, ItemImage, Quantity: int, UnitBuyingPrice: float, UnitSellingPrice: float, SupplierName: str, SupplierEmail: str) -> int:
        """
        This function return 1 or 0

        Returns:
        -If data successfully added to database return 1. Otherwise return 0.
        """
        try:
            self.cursor.execute("""INSERT INTO Stock VALUES (?,?,?,?,?,?,?,?)""", (ItemCode, ItemName, ItemImage, Quantity, UnitBuyingPrice, UnitSellingPrice, SupplierName, SupplierEmail))
        except:
            return 0
        else:
            self.database_connection.commit()
            return 1
    
    def get_item_data_ByName(self,ItemName: str) -> Union[int,list]:
        """
        This function return either 0 or list.

        Returns:
        -If data not found in database then return 0. Otherwise return list of data.
        """
        self.cursor.execute("""SELECT * FROM Stock WHERE ItemName like ?""",(ItemName + '%',))
        result = self.cursor.fetchall()
        if len(result) == 0:
            return 0
        else:
            return result
    
    def get_item_data_ByCode(self,ItemCode: str)-> Union[int,list]:
        """
        This function return either 0 or list.

        Returns:
        -If data not found in database then return 0.Otherwise return list of data.
        """
        self.cursor.execute("""SELECT * FROM Stock WHERE ItemCode = ?""",(ItemCode,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            return 0
        else:
            return result
        
    def get_current_quantity(self, ItemCode: str) -> list:
        self.cursor.execute("""SELECT Quantity FROM Stock WHERE ItemCode = ?""",(ItemCode,))
        result = self.cursor.fetchall()
        return [x for x in result[0]]
    
    def update_data(self, ItemCode : str, ItemName: str, ItemImage, Quantity: int, UnitBuyingPrice: float, UnitSellingPrice: float, SupplierName: str, SupplierEmail: str):
        """
        This function return 1 or 0

        Returns:
        -If data successfully updated to database return 1. Otherwise return 0.
        """
        try:
            self.cursor.execute("""UPDATE Stock SET ItemName = ?, ItemImage = ?, Quantity = ?, UnitBuyingPrice = ?, UnitSellingPrice = ?, SupplierName = ?, SupplierEmail = ? WHERE ItemCode = ?""", (ItemName, ItemImage, Quantity, UnitBuyingPrice, UnitSellingPrice, SupplierName, SupplierEmail, ItemCode))
        except:
            return 0
        else:
            self.database_connection.commit()
            return 1
    
    def delete_data(self,ItemCode : str):
        """
        This function return 1 or 0

        Returns:
        -If data successfully deleted to database return 1. Otherwise return 0.
        """
        try:
            self.cursor.execute("""DELETE FROM Stock WHERE ItemCode = ?""",(ItemCode,))
        except:
            return 0
        else:
            self.database_connection.commit()
            return 1

    def place_order(self, InvoiceNumber: str, Item_dictionary: dict, TotalAmount: float):
        """
        Parameters:
        -Item_dictionary = {ItemCode:(Quantity,SellingPrice)}
        """
        # Get Datetime using invoice number, First convert to datetime_object and then convert to format
        date_str = InvoiceNumber.split('-')[1]
        time_str = InvoiceNumber.split('-')[2]
        datetime_obj = datetime.strptime(date_str + time_str, '%Y%m%d%H%M%S')
        formatted_date = datetime_obj.strftime('%Y-%m-%d')
        formatted_time = datetime_obj.strftime('%H:%M:%S')

        self.cursor.execute("""INSERT INTO Customers VALUES (?,?,?,?)""",(InvoiceNumber, formatted_date, formatted_time, TotalAmount))
        self.database_connection.commit()
        for item_code,quantity_price in Item_dictionary.items():
            self.cursor.execute("""INSERT INTO Orders (InvoiceNumber, ItemCode, Quantity, SellingPrice) VALUES (?,?,?,?)""",(InvoiceNumber, item_code, quantity_price[0], quantity_price[1]))
            self.database_connection.commit()
            data = self.__update_stock_ByOrder(item_code,quantity_price[0])
    
    def __update_stock_ByOrder(self, ItemCode, Quantity):
        self.cursor.execute("""SELECT Quantity FROM Stock WHERE ItemCode = ?""", (ItemCode,))
        current_quantity = self.cursor.fetchall()
        updated_quantity = int(current_quantity[0][0]) - Quantity
        self.cursor.execute("""UPDATE Stock SET Quantity = ? WHERE ItemCode = ?""", (updated_quantity,ItemCode))
        self.database_connection.commit()

    def get_table_data(self):
        self.cursor.execute("""SELECT ItemName FROM Stock ORDER BY ItemName ASC""")
        result = self.cursor.fetchall()
        return [x[0] for x in result]
    
    def get_all_table_data(self):
        self.cursor.execute("""SELECT * FROM Stock ORDER BY ItemCode ASC""")
        result = self.cursor.fetchall()
        return result

    def get_Customers_data(self):
        self.cursor.execute("""SELECT * FROM Customers ORDER BY InvoiceNumber DESC""")
        result = self.cursor.fetchall()
        return result
    
    def get_Order_data(self,InvoiceNumber: str)-> Union[int,list]:
        self.cursor.execute("""SELECT * FROM Orders WHERE InvoiceNumber = ?""",(InvoiceNumber,))
        result = self.cursor.fetchall()
        if len(result) == 0:
            return 0
        else:
            return result
    
    def get_graph_data_DateVs(self,Y_axis: str) -> dict:
        """
        Parameters :
        - Y_axis = profit | items | item_types
        Return :
        - return a Dictionary. Date vs Number of selected Y_axis items [Date (str) : Profit(float)]
        """
        self.cursor.execute("""SELECT Customers.Date, Customers.InvoiceNumber, Orders.ItemCode, Orders.Quantity, Stock.UnitBuyingPrice, Stock.UnitSellingPrice
                               FROM Customers JOIN Orders ON Customers.InvoiceNumber = Orders.InvoiceNumber
                               JOIN Stock ON Orders.ItemCode == Stock.ItemCode""")
        result = self.cursor.fetchall()

        if Y_axis == "profit":
            profit_per_day = {}

            for entry in result:
                date = entry[0]
                quantity = entry[3]
                unit_buying_price = entry[4]
                unit_selling_price = entry[5]
                profit = (unit_selling_price - unit_buying_price) * quantity
                
                if date in profit_per_day:
                    profit_per_day[date] += profit
                else:
                    profit_per_day[date] = profit

            return profit_per_day

        elif Y_axis == "item_types":
            item_types_per_day = {}

            for entry in result:
                date = entry[0]
                item_code = entry[2]
                
                if date in item_types_per_day:
                    if item_code not in item_types_per_day[date]:
                        item_types_per_day[date].append(item_code)
                else:
                    item_types_per_day[date] = [item_code]

            # Count number of item types for each day
            item_types_count_per_day = {date: len(item_types) for date, item_types in item_types_per_day.items()}
            
            return item_types_count_per_day
        
        else:
            items_sold_per_day = {}

            for entry in result:
                date = entry[0]
                quantity = entry[3]
                
                if date in items_sold_per_day:
                    items_sold_per_day[date] += quantity
                else:
                    items_sold_per_day[date] = quantity
            
            return items_sold_per_day
        
    def __hash_password(self,password):
        # Hash the password using a secure hashing algorithm
        return hashlib.sha256(password.encode()).hexdigest()
    
    def save_user(self, username:str, password:str, priority:int) -> bool:
        user_list = self.get_user_list(0)
        if username not in user_list:
            password_hash = self.__hash_password(password)
            self.cursor.execute("INSERT INTO Login (UserName, Password, Priority) VALUES (?,?,?)", (username, password_hash, priority))
            self.database_connection.commit()
            return True
        else:
            return False

    def verify_password(self, username, password):
        self.cursor.execute("SELECT * FROM Login WHERE UserName=?", (username,))
        result = self.cursor.fetchone()
        if result:
            stored_password_hash = str(result[2])
            input_password_hash = self.__hash_password(password)
            if stored_password_hash == input_password_hash:
                return result[3]
        return False
    
    def get_user_list(self,Want_user_priority:bool)-> list:
        self.cursor.execute("SELECT UserName,Priority FROM Login")
        result = self.cursor.fetchall()
        if Want_user_priority:
            return {x[0]:x[1] for x in result}
        else:
            return [x[0] for x in result]

    def close_connection(self):
        self.cursor.close()
        self.database_connection.close()