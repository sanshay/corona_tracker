import requests 
import json
import sys
import os
import matplotlib.pyplot as plt
# sys.stdout=open("config.py","w")
states_daily = requests.get("https://api.covid19india.org/states_daily.json")
raw = requests.get("https://api.covid19india.org/data.json")

def print_json(object):
 data = json.dumps(object, sort_keys=True, indent=4)
 # print(data)

states={}

states = states_daily.json()  #'["statewise"]
b=states


statewise = raw.json()["statewise"]
c=statewise



cases_time_series = raw.json()["cases_time_series"]
d=cases_time_series




dailyconfirmed=[]
dailydeceased=[]
dailyrecovered=[]
totalconfirmed=[]
totaldeceased=[]
totalrecovered=[]
for i in d:
    for j in i:
        a=i['dailyconfirmed']
        dailyconfirmed.append(a)
        break
for i in d:
    for j in i:
        a=i['dailydeceased']
        dailydeceased.append(a)
        break
for i in d:
    for j in i:
        a=i['dailyrecovered']
        dailyrecovered.append(a)
        break
for i in d:
    for j in i:
         a=i['totalconfirmed']
         totalconfirmed.append(a)
         break
for i in d:
    for j in i:
        a=i['totaldeceased']
        totaldeceased.append(a)
        break
for i in d:
    for j in i:        
        a=i['totalrecovered']
        totalrecovered.append(a)
        break

dailyconfirmed1=[int(item) for item in dailyconfirmed]
dailydeceased1=[int(item) for item in dailydeceased]
dailyrecovered1=[int(item) for item in dailyrecovered]
totalconfirmed1=[int(item) for item in totalconfirmed]
totaldeceased1=[int(item) for item in totaldeceased]
totalrecovered1=[int(item) for item in totalrecovered]

# print("daily confirmed :",dailyconfirmed1)
# print("daily deceased :",dailydeceased1)
# print("daily recovered",dailyrecovered1)
# print("Total confirmed :",totalconfirmed1)
# print("Total deceased :",totaldeceased1)
# print("Total recovered :",totalrecovered1)




date=[]
for i in d:
    for j in i:
        a=i['date']
        date.append(a)
        break
# print("Date :",date)  

#.................................................................................#


# #.................................FINAL.........................................#


import matplotlib.pyplot as plt
# line 1 points
x1 = date
y1 = dailyconfirmed1
# plotting the line 1 points 
plt.plot(x1, y1, label = "Daily comfirmed")

# line 2 points
x2 =date
y2 = dailydeceased1
# plotting the line 2 points 
plt.plot(x2, y2, label = "Daily deceased")

# line 3 points
x3 =date
y3 = dailyrecovered1
# plotting the line 2 points 
plt.plot(x3, y3, label = "Daily recovered")


plt.xlabel('Date')
# Set the y axis label of the current axis.
plt.ylabel('On daily basis')
# Set a title of the current axes.
plt.title('DAILY CASES ')
plt.suptitle('Covid-19')
#.adding grid.....#
plt.grid(True)
#...saving plot as a picture..
plt.savefig("test1.png")
# show a legend on the plot
plt.legend()


#......FOR A SEPARATE WINDOW.........#
fig, ax= plt.subplots()


# line 1 points
x1 = date
y1 = totalconfirmed1
# plotting the line 1 points 
plt.plot(x1, y1, label = "total comfirmed")

# line 2 points
x2 =date
y2 = totaldeceased1
# plotting the line 2 points 
plt.plot(x2, y2, label = "total deceased")

# line 3 points
x3 =date
y3 = totalrecovered1
# plotting the line 2 points 
plt.plot(x3, y3, label = "total recovered")

# Set the X axis label of the current axis.
plt.xlabel('Date')
# Set the y axis label of the current axis.
plt.ylabel('Overall')
# Set a title of the current axes.
plt.title('TOTAL CASES ')
plt.suptitle('Covid-19')
#.adding grid.....#
plt.grid(True)
#...saving plot as a picture..
plt.savefig("test2.png")
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()








for i in c:
    for key,value in i.items():
        a=[]

        # print(key,":",value)
        a.append(i['active'])
        a.append(i['confirmed'])
        a.append(i['deaths'])
        a.append(i['recovered'])
        a.append(i['deltaconfirmed'])
        a.append(i['deltadeaths'])
        a.append(i['deltarecovered'])
        state= i['state']
        fig, ax= plt.subplots()
        labels = ['active','confirmed','deaths','recovered','deltaconfirmed', 'deltadeaths', 'deltarecovered']
        sizes = a
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True)

        explode = (0.1, 0, 0, 0) 

        plt.pie(sizes,  colors=colors, autopct='%1.0f%%',shadow=True, startangle=140)


        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.suptitle(state)
        plt.title('Covid-19')

        plt.show()

        break
        
