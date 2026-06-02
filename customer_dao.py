import sqlite3
from customer import Customer
class CustomerDAO:


    def __init__(self,db_file):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)

    def save(self,customer):
        cur = self.connection.cursor()
        sql = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address)
                    VALUES(?,?,?,?,?)"""
        
        cur.execute(sql, (customer.first_name, customer.last_name, customer.email, customer.gender, customer.ip_address))
        self.connection.commit()


    def find_all_old(self):
        cur = self.connection.cursor()
        sql = "SELECT * FROM customers_tbl"
        cur.execute(sql)
        # Map to customer object
        data = cur.fetchall()
        customers = []
        for d in data:
            c = Customer(*d)
            customers.append(c)
        return customers
    
    def find_all(self):
        cur = self.connection.cursor()
        sql = "SELECT * FROM customers_tbl"
        cur.execute(sql)
        # Map to customer object
        data = cur.fetchall()
        for d in data:
            c = Customer(*d)
            yield c    

    def __del__(self):
        self.connection.close()