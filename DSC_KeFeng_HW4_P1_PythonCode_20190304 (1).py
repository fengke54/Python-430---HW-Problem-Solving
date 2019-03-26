#Name: Feng, Ke
#DePaul ID: 1927931
#Date:03/04/2019
#HW2, Problem 1
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Import Library
import csv
import math
import statistics

###Part I. (a-c) Using the statistics module

#MeanSM
def readAndComputeMean_SM(csv_head):
    # open the file
    file = open('avocado.csv', 'r')
    # read the csv file
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        data_values = []
        for data_line in reader:
            data_values.append(float(data_line[head_index]))
        file.close()
        return statistics.mean(data_values)
    else:
        file.close()
        print(csv_head + ' not found.')

#Standard Deviation
def readAndComputeSD_SM(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        data_values = []
        for data_line in reader:
            data_values.append(float(data_line[head_index]))
        file.close()
        return statistics.stdev(data_values)
    else:
        file.close()
        print(csv_head + ' not found.')

#Function for Median
def readAndComputeMedian_SM(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        data_values = []
        for data_line in reader:
            data_values.append(float(data_line[head_index]))
        file.close()
        return statistics.median(data_values)
    else:
        file.close()
        print(csv_head + ' not found.')

###Part II. (d) Not Using the statistics model

#Function for Mean
def readAndComputeMean_HG(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        data_values = []
        for data_line in reader:
            data_values.append(float(data_line[head_index]))
        file.close()
        #formula: avarage=totoal/length
        return sum(data_values) / len(data_values)
    else:
        file.close()
        print(csv_head + ' not found.')

#Function for Standard Deviation 
def readAndComputeSD_HG(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        data_values = []
        for data_line in reader:
            data_values.append(float(data_line[head_index]))
        file.close()
        # SD formula
        # step 1: find out mean
        mean = sum(data_values) / len(data_values)
        # (num1-mean)2...(numn-mean)2=sum
        sum_value = 0
        for v in data_values:
            sum_value += math.pow(v - mean, 2)
        # sqrt(sum/len)
        return math.sqrt(sum_value / (len(data_values) - 1))
    else:
        file.close()
        print(csv_head + ' not found.')

#Function for Median
def readAndComputeMedian_HG(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        data_values = []
        for data_line in reader:
            data_values.append(float(data_line[head_index]))
        file.close()
        # median formula 
        # sort
        sort_values = sorted(data_values)
        #even or odd, find the middle
        data_len = len(sort_values)
        if data_len % 2 == 0:
            return (sort_values[int(data_len / 2)] + sort_values[int(data_len / 2 - 1)]) / 2
        else:
            return sort_values[math.floor(data_len / 2)]
    else:
        file.close()
        print(csv_head + ' not found.')

###Part III. (e) Function Memoryless

#Function for Mean
def readAndComputeMean_MML(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        count = 0
        sum_value = 0
        for data_line in reader:
            sum_value += float(data_line[head_index])
            count += 1
        file.close()
        return sum_value / count
    else:
        file.close()
        print(csv_head + ' not found.')

#Function for SD
def readAndComputeSD_MML(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        count = 0
        sum_value = 0
        sum_value_sq = 0
        for data_line in reader:
            sum_value += float(data_line[head_index])
            sum_value_sq += math.pow(float(data_line[head_index]), 2)
            count += 1
        file.close()
        # SD formula
        return math.sqrt((sum_value_sq - (math.pow(sum_value, 2) / count)) / (count - 1))
    else:
        file.close()
        print(csv_head + ' not found.')

#Function for Median
def readAndComputeMedian_MML(csv_head):
    # open file
    file = open('avocado.csv', 'r')
    # read csv
    reader = csv.reader(file)
    # read first line -> csv header
    header = next(reader)
    if csv_head in header:
        head_index = header.index(csv_head)
        # similar data only store once， appearance & total count
        count = 0
        total_count = {}
        for data_line in reader:
            data_value = float(data_line[head_index])
            if data_value in total_count:
                total_count[data_value] += 1
            else:
                total_count[data_value] = 1
            count += 1
        file.close()
        # Sort the data
        iter_total = 0
        half_count = count / 2
        data_key = sorted(total_count.keys())
        # odd even， if odd， find the middle， if even， find the average of two numbers 
        for i in range(0, len(data_key)):
            iter_total += total_count[data_key[i]]
            if iter_total > half_count:
                if count % 2 == 0:
                    if total_count[data_key[i]] == 1:
                        return (data_key[i] + data_key[i - 1]) / 2
                    else:
                        return data_key[i]
                else:
                    return data_key[i]
    else:
        file.close()
        print(csv_head + ' not found.')

#To show memories are stored 
if __name__ == '__main__':
    print('Total Volume')
    head = 'Total Volume'
    mean_SM = readAndComputeMean_SM(head)
    print('Mean_SM:')
    print(mean_SM)
    sd_SM = readAndComputeSD_SM(head)
    print('sd_SM:')
    print(sd_SM)
    median_SM = readAndComputeMedian_SM(head)
    print('median_SM：')
    print(median_SM)
    mean_HG = readAndComputeMean_HG(head)
    print('mean_HG:')
    print(mean_HG)
    sd_HG = readAndComputeSD_HG(head)
    print('sd_HG:')
    print(sd_HG)
    median_HG = readAndComputeMedian_HG(head)
    print('median_HG:')
    print(median_HG)    

###Part IV. (f) Test Code
    head_list = ['AveragePrice', 'Total Volume', 'Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags']
    print('\n' + "This is the test result---Only numeric variables AveragePrice/Volume/TotalBags/SmallBags/LargeBags/XLargeBags are included: " + '\n') 
    for head in head_list:
        print("Result for " + head)
        print('Func\t\tSM\t\tHG\t\tMML')
        print('mean\t%10.3f\t%10.3f\t%10.3f' % (readAndComputeMean_SM(head), readAndComputeMean_HG(head), readAndComputeMean_MML(head)))
        print('sd\t%10.3f\t%10.3f\t%10.3f' % (readAndComputeSD_SM(head), readAndComputeSD_HG(head), readAndComputeSD_MML(head)))
        print('median\t%10.3f\t%10.3f\t%10.3f' % (readAndComputeMedian_SM(head), readAndComputeMedian_HG(head), readAndComputeMedian_MML(head)))
        print('\n')



    


