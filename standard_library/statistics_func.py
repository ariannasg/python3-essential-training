#!usr/bin/env python3
import array
import csv
import statistics

# simple statistics operations
sample_data1 = [1, 3, 5, 7]
sample_data2 = [2, 3, 5, 4, 3, 5, 3, 2, 5, 6, 4, 3]
sample_data3 = ['dog', 'cat', 'dog', 'rabbit', 'hedgehog']

# Use the mean function - calculates an average value
print('Mean:', statistics.mean(sample_data1))

# Use the different median functions. the median of a dataset is the midpoint
# value. is the value where half the numbers are lower and the other half are
# higher
# median calculates the median even if that number is not on my data set
print('Median:', statistics.median(sample_data1))
# median calculates the median and returns the low value from my data set
print('Median low:', statistics.median_low(sample_data1))
# median calculates the median and returns the high value from my data set
print('Median high:', statistics.median_high(sample_data1))

# The mode function indicates which data item occurs
# most frequently (most common value)
print('Most frequent value in sample2:', statistics.mode(sample_data2))
print('Most frequent value in sample3:', statistics.mode(sample_data3))


# Read data from a CSV file and calculate statistics
def read_data():
    with open("stock_quotes.csv") as dataFile:
        data = array.array('f', [])

        reader = csv.reader(dataFile)
        cur_line = 0
        for row in reader:
            if cur_line == 0:
                pass  # this is the headers row
            else:
                # get the closing value
                item = float(row[4])
                data.append(item)
            cur_line += 1

        print(f"Read {cur_line + 1} rows of data.")
        return data


def calc_stats():
    # read the data from the CSV file
    data = read_data()

    data_mean = round(statistics.mean(data), 2)
    data_med = round(statistics.median(data), 2)
    # the standard deviation tells us how close the data is to the average
    data_std = round(statistics.stdev(data), 2)
    # the variance function tells us how much variation there is among the data
    data_var = round(statistics.variance(data), 2)

    print("Mean: ", data_mean)
    print("Median: ", data_med)
    print("Standard deviation: ", data_std)
    print("Variance: ", data_var)


calc_stats()

# CONSOLE OUTPUT:
# Mean: 4
# Median: 4.0
# Median low: 3
# Median high: 5
# Most frequent value in sample2: 3
# Most frequent value in sample3: dog
# Read 12 rows of data.
# Mean:  1028.27
# Median:  1027.03
# Standard deviation:  6.17
# Variance:  38.01
