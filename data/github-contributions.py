from bs4 import BeautifulSoup
import requests

#Brackets: 0 1-3 4-7 8-12 12-18

def median(data):       
    sorted_data = sorted(data)
    mid = len(sorted_data) / 2
    if (len(sorted_data) % 2 == 0):
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    else:
        return sorted_data[mid]

def quartiles(data):
    sorted_data = sorted(data)
    mid = len(sorted_data) / 2
    
    if (len(sorted_data) % 2 == 0):
        return median(sorted_data[:mid]), median(sorted_data[mid:])
    else:
        return median(sorted_data[:mid]), median(sorted_data[mid + 1:])

profile = requests.get('https://github.com/jackiehluo')
data = profile.text
soup = BeautifulSoup(data)
r = soup.findAll('rect')
contributions = [int(c['data-count']) for c in r if int(c['data-count']) > 0]
q1, q3 = quartiles(contributions)
median = median(contributions)

print "First Quartile:", q1
print "Second Quartile:", median
print "Third Quartile:", q3
print "Fourth Quartile:", max(contributions)

first, second, third, fourth = 0, 0, 0, 0

for c in contributions:
    if c > 0 and c < 4:
        first += 1
    elif c >= 4 and c < 8:
        second += 1
    elif c >= 8 and c < 12:
        third += 1
    else:
        fourth += 1

print "Light Green:", first
print "Medium Green:", second
print "Bright Green:", third
print "Dark Green:", fourth