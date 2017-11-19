import os
import csv
for file_ in os.listdir("raw"):
    with open('raw/'+ file_, 'rb') as csvfile:
        
        spamreader = csv.reader(csvfile, delimiter=',')
        
        for row in spamreader:
            if os.path.isfile("processed/" + row[0] +"-processed.csv"):
                
                with open("processed/" + row[0] +"-processed.csv", 'a') as csvfile1:
                    spamwriter = csv.writer(csvfile1, delimiter=',')
                    spamwriter.writerow(row)
            else:
                
                with open("processed/" + row[0] +"-processed.csv", 'wb') as csvfile1:
                    spamwriter = csv.writer(csvfile1, delimiter=',')
                    spamwriter.writerow(row)
