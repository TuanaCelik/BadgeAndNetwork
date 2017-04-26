import csv
from collections import Counter
import json

#VISUALIZATION 1
def put_csv_into_list(file_name):
  data = []
  with open(file_name, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    first_row = next(spamreader)
    for row in spamreader:
      data.append(row)
  return data

IPLogData = put_csv_into_list('IPLog.csv')

#input should be IPLogData (source, dest, reqsize, ressize, commsize)
def add_comm_sizes(logdata):
  comm_size_dict = {}
  counter_dict = {}
  for i in logdata:
    dest = i[1]
    if dest not in comm_size_dict:
      comm_size_dict[dest] = float(i[4])
      counter_dict[dest] = 1
    else:
      comm_size_dict[dest] = comm_size_dict[dest] + float(i[4])
      counter_dict[dest] = counter_dict[dest] + 1

  return (comm_size_dict, counter_dict)

(added_comm_sizes, counts) = add_comm_sizes(IPLogData)

def output_data_structure(comm_map, counts):
  #destination, commSize, count
  output_list = []
  for key in comm_map:
    output_list.append([key, int(comm_map[key]), counts[key]])

  return output_list

final_list = output_data_structure(added_comm_sizes, counts)
sorted_list = sorted(final_list, key = lambda x: int(x[1]))

def sort_and_cut_list(num, sorted_list):
  truncated_list = []
  for i in xrange(1, num + 1):
    truncated_list.append(sorted_list[-i])
  return truncated_list

sorted_list = sort_and_cut_list(10, sorted_list)


def write_csv(input_list):
  with open('topCommSize.csv', 'wb') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(['destIP','Size','Freq'])
    for item in input_list:
      w.writerow(item)

#write_csv(sorted_list)

#VISUALIZATION 2

#Find most frequent contactors to suspicious IP



#how many distinct destination IP addresses there are in IPLog.csv
#20243 distinct destinations
#115414 total destinations

