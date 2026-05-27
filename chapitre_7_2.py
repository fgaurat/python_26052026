import json 
import csv

def main():
    # read csv file: MOCK_DATA.csv with csv module with dictreader
    with open("MOCK_DATA.csv") as f:
        reader = csv.DictReader(f)
        all_data = []
        for data in reader:
            all_data.append(data)


def main_read_json():
    with open("the_data.json") as f:
        all_data = json.load(f)

        for data in all_data:
            print(data['id'],data['first_name'])


def main_write_json():
    
    with open("MOCK_DATA.csv") as f:

        lines = f.readlines()
        clean_lines = [line.strip() for line in lines]

        # [id,first_name,last_name,email,gender,ip_address]

        the_keys = clean_lines[0].split(",")
        the_data = clean_lines[1:]
        all_values = []
        for data in the_data:
            # [1,Ingmar,Swinburn,iswinburn0@cbslocal.com,Male,161.196.74.228]
            # [('id',1),('first_name','Ingmar'),...]
            data = data.split(",")
            d = dict(zip(the_keys,data))
            all_values.append(d)

    with open('the_data.json','w') as f:
        json.dump(all_values,f,indent=4)

if __name__=='__main__':
    main()
