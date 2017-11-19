import urllib2
from bs4 import BeautifulSoup
import csv


regions = ["american","arabic","australian","christian","english","french","german","indian"]

genders = ["boy","girl"]

letters = list("abcdefghijklmnopqrstuvwxyz")

url = "https://www.babynamesdirect.com/baby-names"

def check_redirection(url):
    req = urllib2.Request(url=url)
    resp = urllib2.urlopen(req, timeout=3)                 #fetching internet resources
    redirect = resp.geturl() != url                        # redirect will take boolean value True or false 
    return redirect


with open("names.csv", "wb") as csvfile:
    spamwriter = csv.writer(csvfile1, delimiter=',')           #writing to csv file
    spamwriter.writerow(["name","gender"])                     #writing in particular row

def get_names(url,gender):
    page = urllib2.urlopen(url)                                #fetching internet resources
    soup = BeautifulSoup(page)
    all_li=soup.find_all('li', class_='ntr')
    for i in all_li:
    if(i.dl):
        if(i.dl.dt):
            if(i.dl.dt.b):
                if(i.dl.dt.b.a):
                    with open("names.csv", "a") as csvfile:                       #opening file
                        spamwriter = csv.writer(csvfile, delimiter=',')           #writing names seprated by comma
                        spamwriter.writerow([i.dl.dt.b.text, gender])             #writing gender

for region in regions:                                             #loop for matching gender and writing to csv file under gender column
    url_now = url + "/" + region
    for gender in genders:
        url_now_2 = url_now + "/" + gender
        for letter in letters:
            url_now_1 = url_now_2 + "/" + letter
            get_names(url_now_1, gender)
            print url_now_1
            const = 2
            url_number = url_now_1 + "/" + str(const)
            while(not(check_redirection(url_number))):
                get_names(url_number, gender)
                print url_number
                const = const + 1
                url_number = url_now_1 + "/" + str(const)
