import csv
from collections import Counter

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




#how many distinct destination IP addresses there are in IPLog.csv
#20243 distinct destinations
#115414 total destinations
def distinct_destinations():
  dest_set = set([])
  count = 0

  with open('IPLog.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    first_row = next(spamreader)
    for row in spamreader:
        count +=1
        if row[1] not in dest_set:
          dest_set.add(row[1])

  #return len(dest_set)
  return count
#print distinct_destinations()
#new data structure: destination, size, count
#dictionary: destination: size, count

#top_ten_comm_sizes()

