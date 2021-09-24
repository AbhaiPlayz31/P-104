import csv
from collections import Counter

with open ('nou.csv', newline='') as file:
    reader=csv.reader(file)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num=fileData[i][2]
    newData.append(float(num))

n =  len(newData)

# #Mean:
# total = 0
# for e in newData:
#     total+=e

# mean = total/n
# print('Mean is:' +str(mean))



# # Median:
# newData.sort()

# if n % 2 == 0:
#     median1=float(newData[n//2])
#     median2=float(newData[n//2-1])   
#     median = (median1 + median2)/2

# else:
#     median = newData[n//2]

# print('Median is:' + str(median)) 



data = Counter(newData)
range={'100-110':0, '110-120':0, '120-130':0, '130-140':0, '140-150':0, '150-160':0}

for height,occurrence in data.items():

    if 100<float(height)<110:
        range['100-110']+=occurrence

    elif 110<float(height)<120:
        range['110-120']+=occurrence

    elif 120<float(height)<130:
        range['120-130']+=occurrence

    elif 130<float(height)<140:
        range['130-140']+=occurrence
    
    elif 140<float(height)<150:
        range['140-150']+=occurrence

    elif 150<float(height)<160:
        range['150-160']+=occurrence

   

modeRange, modeOccurrence = 0,0
for r,occurrence in range.items():
    if occurrence > modeOccurrence:
        modeRange, modeOccurrence = [int(r.split('-')[0]),int(r.split('-')[1])], occurrence

mode = float((modeRange[0]+modeRange[1])/2)
print(f'Mode is-> {mode:2f}')
