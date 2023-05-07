import csv
import random
from faker import Faker
import datetime


def data_generate(records, headers):
    fake = Faker()
    with open("People_data.csv", 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            f_lname = full_name.split(" ")
            fname = f_lname[0]
            lname = f_lname[1]
            domain_name = "@gmail.com"
            user_id = str(fname).lower() + "." + str(lname).lower() + domain_name
            salary = fake.random_number(digits=3, fix_len=True)
            patterns = {1: "%d-%m-%Y", 2: "%Y-%m-%d", 3: "%d-%m-%Y %H:%M:%S"}
            writer.writerow({
                "Name": fake.name(),
                "Email Id": user_id,
                "Birth Date": str(
                    fake.date(pattern=patterns[random.randint(1, 3)], end_datetime=datetime.date(2000, 1, 1))),
                "Salary": "$" + str(salary) if random.randint(0, 9) != 0 else None
            })


# patterns[random.randint(1, 3)]
if __name__ == '__main__':
    records1 = 1
    headers1 = ["Name", "Email Id", "Birth Date", "Salary"]
    data_generate(records1, headers1)
    print("CSV generation complete!")
