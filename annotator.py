import os
import yaml
import csv
policies=os.listdir('dataset/annotations')

for j in policies:
    with open('dataset/annotations/'+j) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        segment_list = yaml.load(file, Loader=yaml.FullLoader)
    for i in segment_list['segments']:
        print(i['segment_id'],i['segment_text'])
        n=int(input())
        with open('test.csv', mode='a') as segment_file:
            segment_writer = csv.writer(segment_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            segment_writer.writerow([i['segment_id'],n])
