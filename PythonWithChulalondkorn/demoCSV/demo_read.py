import csv


def read_text():
    with open(r"d:\Pyrthon\PythonWithChulalondkorn\data\rio2016.csv") as f:
        data = f.read()
        print(type(data))
        print(data)
def read_csv():
    with open(r"d:\Pyrthon\PythonWithChulalondkorn\data\rio2016.csv") as f:
        data = csv.reader(f)
        # print(type(data))
        # print(data)
        for row in data :
            # print(row)
            print("{:25} : {:2} {:2} {:2} {:3}".format(row[0],row[1],row[2],row[3],int(row[1])+int(row[2])+int(row[3])))
# read_text()
# read_csv()

def read_csv_tab():
    with open(r"d:\Pyrthon\PythonWithChulalondkorn\data\rio2016tab.txt") as f:
        data = csv.reader(f, delimiter = "\t",newline = "")
        for row in data :

            print("{:25} : {:2} {:2} {:2} {:3}".format(row[0],row[1],row[2],row[3],int(row[1])+int(row[2])+int(row[3])))
# read_csv_tab()



def read_csv_header():
    with open(r"d:\Pyrthon\PythonWithChulalondkorn\data\rio2016_header_column.csv") as f:
        data = csv.DictReader(f)
        print(type(data))
        print(data)
        print(data.fieldnames) #return ilst header
        for row in data:
            print(row)
            print(row["country"])
        # for row in data :
        #     # print(row)
        #     print("{:25} : {:2} {:2} {:2} {:3}".format(row[0],row[1],row[2],row[3],int(row[1])+int(row[2])+int(row[3])))
read_csv_header()