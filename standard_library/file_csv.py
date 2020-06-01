#!usr/bin/env python3
import csv

# list the dialects that are available to use
print(csv.list_dialects())


# Open a CSV file and read each row of data
def reader_sample():
    with open("stock_quotes.csv") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            print(row)


# Use the CSV module Sniffer to see what dialect the CSV file is using
def use_sniffer():
    with open("stock_quotes.csv") as csv_file:
        # I'm going to read the first 1024 bytes
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        has_header = csv.Sniffer().has_header(csv_file.read(1024))
        csv_file.seek(0)
        print("Headers found: " + str(has_header))
        print("Dialect information")
        print('delimiter:', dialect.delimiter)
        print('escapechar:', dialect.escapechar)
        print('quotechar:', dialect.quotechar)
        print('lineterminator:', dialect.lineterminator)


# Write data to a CSV file
def writer_sample():
    with open("sample_data.csv", mode="w") as csv_file:
        # create a csv writer
        csv_writer = csv.writer(csv_file)
        # write the header
        csv_writer.writerow(["Name", "Department", "Location"])
        # write a few rows
        csv_writer.writerow(["John Doe", "Accounting", "San Francisco CA"])
        csv_writer.writerow(["Jane Dae", "Engineering", "Seattle WA"])
        csv_writer.writerow(["Jim Due", "Human Resources", "New York NY"])
        csv_writer.writerows([["Tim Smith", "Accounting", "San Francisco CA"],
                              ["Kate Williams", "Engineering", "Seattle WA"]])


# Exercise the samples
writer_sample()
use_sniffer()
reader_sample()

# CONSOLE OUTPUT:
# ['excel', 'excel-tab', 'unix']
# ['excel', 'excel-tab', 'unix']
# Headers found: True
# delimiter: ,
# escapechar: None
# quotechar: "
# ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
# ['2017-11-06', '1028.989990', '1034.869995', '1025.000000', '1025.900024', '1025.900024', '1125200']
# ['2017-11-07', '1027.270020', '1033.969971', '1025.130005', '1033.329956', '1033.329956', '1112300']
# ['2017-11-08', '1030.520020', '1043.521973', '1028.449951', '1039.849976', '1039.849976', '1088700']
# ['2017-11-09', '1033.989990', '1033.989990', '1019.666016', '1031.260010', '1031.260010', '1245200']
# ['2017-11-10', '1026.459961', '1030.760010', '1025.280029', '1028.069946', '1028.069946', '720000']
# ['2017-11-13', '1023.419983', '1031.579956', '1022.570007', '1025.750000', '1025.750000', '885800']
# ['2017-11-14', '1022.590027', '1026.810059', '1014.150024', '1026.000000', '1026.000000', '959200']
# ['2017-11-15', '1019.210022', '1024.089966', '1015.419983', '1020.909973', '1020.909973', '854000']
# ['2017-11-16', '1022.520020', '1035.920044', '1022.520020', '1032.500000', '1032.500000', '1129700']
# ['2017-11-17', '1034.010010', '1034.420044', '1017.750000', '1019.090027', '1019.090027', '1397100']
