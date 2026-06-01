from customer import Customer
from customer_dao import CustomerDAO
import csv

def main():
    dao = CustomerDAO("customers_db.db")
    customers = dao.find_all()
    for cust in customers:
        print(cust.first_name)

def main_write():

    dao = CustomerDAO("customers_db.db")

    # read csv file: MOCK_DATA.csv with csv module with dictreader
    with open("MOCK_DATA.csv") as f:
        reader = csv.DictReader(f)
        for data in reader:
            data["id"] = int(data["id"])
            c = Customer(**data)
            dao.save(c)


if __name__=='__main__':
    main()


