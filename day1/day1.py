import os


list_of_measures = []
with open("data.txt", "r") as file:
    for line in file.readlines():
        list_of_measures.append(int(line))


previous_item = None
amt_larger = 0

for x in range(0,len(list_of_measures)):
    try: 
        sum = list_of_measures[x] + list_of_measures[x + 1] + list_of_measures[x + 2]
    except IndexError as e:
        try: 
            sum = list_of_measures[x] + list_of_measures[x + 1]
        except:
            sum = list_of_measures[x]
    if  previous_item != None and sum > previous_item : 
        amt_larger += 1 
    previous_item = sum

print(amt_larger)