import sqlite3
import customer_dao
def main():
    dao = customer_dao.CustomerDAO("customers_db.db")
    
    for cust in dao.find_all():
        print(cust.name)





    # con = sqlite3.connect("customers_db.db")
    # cur = con.cursor()
    # # select all data from customers_tbl
    # sql = "SELECT * FROM customers_tbl"
    # cur.execute(sql)
    # data = cur.fetchall()
    # for d in data:
    #     print(d)


if __name__=='__main__':
    main()

