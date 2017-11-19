import os
import csv
for file_ in os.listdir("raw"):
    with open('raw/'+ file_, 'rb') as csvfile:                 #opening file
        
        spamreader = csv.reader(csvfile, delimiter=',')       #reading csv file word by word
        
        for row in spamreader:                                                  #function for pushing row
            if os.path.isfile("processed/" + row[0] +"-processed.csv"):         
                
                with open("processed/" + row[0] +"-processed.csv", 'a') as csvfile1:       
                    spamwriter = csv.writer(csvfile1, delimiter=',')             #writing to csv file in given format        
                    spamwriter.writerow(row)                                     #inserting row
            else:
                
                with open("processed/" + row[0] +"-processed.csv", 'wb') as csvfile1:
                    spamwriter = csv.writer(csvfile1, delimiter=',')
                    spamwriter.writerow(row)                             
