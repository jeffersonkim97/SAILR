# Imports
import csv

# Import csv file
print('Reading CSV')
csvFilePath = 'log_53_2020-3-6-14-38-12_vehicle_gps_position_0.csv'

dic_id = []
timestamp = []
lat = []
lon = []

with open(csvFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for i in range(0, 25):
                dic_id.append(row[i])
                line_count += 1
        else:
            timestamp.append(row[0])
            lat.append(row[2])
            lon.append(row[3])
        print('...Loading...')
print('done')

# Calculating time spent
# Assume input data is a array, based on time spent from departure

# Example input:
print('Take Inputs')
input_time = [1924598, 2145633, 2887386, 2916457, 3145967] # in sec
init_time = int(timestamp[0]) # in milisec
print('Initial time:' + str(init_time/1000))

# Calculate time difference
print('Calculate time difference')
time_diff = []
for i in range(len(input_time)):
    time_diff.append(input_time[i] - init_time/1000)
time_diff = time_diff*1000 # convert to milisec

# Calculate time in milisecond
time = []
for i in range(len(time_diff)):
    time.append(time_diff[i] + init_time)

# Track timestamp to check index of timestamp which photo is taken
print('Find time which photos are taken')
record = []
for i in range(len(input_time)):
    for j in range(len(timestamp)):
        diff = int(timestamp[j]) - input_time[i]*1000
        if diff < 1: # 0.001 second interval
            record.append(j)
print(record)