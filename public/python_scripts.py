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

def output_data_structure(comm_map, counts):
  #destination, commSize, count
  output_list = []
  for key in comm_map:
    output_list.append([key, int(comm_map[key]), counts[key]])

  return output_list

#input should be IPLogData (source, dest, reqsize, ressize, commsize)
def add_comm_sizes(num, logdata):
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

  final_list = output_data_structure(comm_size_dict, counter_dict)
  sorted_list = list(reversed(sorted(final_list, key = lambda x: int(x[1]))))

  return sorted_list[:num]

def write_csv(input_list, filename, firstrow):
  with open(filename, 'wb') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(firstrow)
    for item in input_list:
      w.writerow(item)

sorted_list = add_comm_sizes(10, IPLogData)
write_csv(sorted_list, 'topCommSize.csv', ['destIP','Size','Freq'])

#VISUALIZATION 2

#Find most frequent contactors to suspicious IP
def most_frequent_contactors(num, logdata, sus_ID):
  #ID, commSize, frequency

  comm_size_dict = {}
  counter_dict = {}
  for i in logdata:

    if i[1] == sus_ID:
      source = i[0]
      if source not in comm_size_dict:
        comm_size_dict[source] = float(i[4])
        counter_dict[source] = 1
      else:
        comm_size_dict[source] = comm_size_dict[source] + float(i[4])
        counter_dict[source] = counter_dict[source] + 1

  list_format = output_data_structure(comm_size_dict, counter_dict)
  sorted_list = sorted(list_format, key = lambda x: int(x[2]))
  in_order_list = list(reversed(sorted_list))
  return in_order_list[:num]


frequent_contactors = most_frequent_contactors(10, IPLogData, sorted_list[0][0])
write_csv(frequent_contactors, 'freqSusContactors.csv', ['sourceIP','Size','Freq'])

#how many distinct destination IP addresses there are in IPLog.csv
#20243 distinct destinations
#115414 total destinations

