import csv

def put_csv_into_list(file_name):
  data = []
  with open(file_name, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    first_row = next(spamreader)
    for row in spamreader:
      data.append(row)
  return data

IPLogData = put_csv_into_list('IPLog.csv')

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

  return len(dest_set)
  #return count


def top_ten_comm_sizes():

  #for i in xrange(10):
    #print IPLogData[i]
  f = open('commSize.txt', 'w')

  IPLogData.sort(key=lambda x: x[4])
  new_list = sorted(IPLogData, key = lambda x: int(x[4]))
  for i in xrange(1, 11):
    print i
    f.write(str(new_list[-i]))
    f.write('\n')
  f.close()


top_ten_comm_sizes()
