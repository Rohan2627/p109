import pandas as pd 
import csv
import statistics as st

data = pd.read_csv("project109.csv")

readingTime = data["reading score"].tolist()


# ----------------------------------- mean/median/mode/stdev -----------------------------------------
mean = st.mean(readingTime)
median = st.median(readingTime)
mode = st.mode(readingTime)
stdev = st.stdev(readingTime)

print("Mean : " , mean)
print("Mode : " , mode)
print("Median : " , median)
print("Std dev : " , stdev)



# ------------------------------- stdev 1/2/3 start & end ----------------------------------

stdevStart1 , stdevEnd1 = mean - stdev  , mean + stdev

stdevStart2 , stdevEnd2 = mean - (2 * stdev)  , mean + (2 * stdev)

stdevStart3 , stdevEnd3 = mean - (3 * stdev)  , mean + (3 * stdev)


# --------------------------- list of data lying within stdev 1/2/3 -----------------------------------

# listOfDataWithinSD1 = [res for res in dice_result if res > stdevStart1 and res < stdevEnd1 ]

listOfDataWithinSD1 = []

for i in readingTime:
    if i > stdevStart1 and i < stdevEnd1:
        listOfDataWithinSD1.append(i)



listOfDataWithinSD2 = []

for i in readingTime:
    if i > stdevStart2 and i < stdevEnd2:
        listOfDataWithinSD2.append(i)



listOfDataWithinSD3 = []

for i in readingTime:
    if i > stdevStart3 and i < stdevEnd3:
        listOfDataWithinSD3.append(i)


# -------------------------------------- percentage of data lying within stdev 1/2/3 --------------------------------------------------

p1 = (len(listOfDataWithinSD1) * 100) / len(readingTime)

p2 = (len(listOfDataWithinSD2)* 100)/len(readingTime)

p3 = (len(listOfDataWithinSD3)* 100)/len(readingTime)



print("The percentage of the data lying within 1 stdev : " , p1 )

print("The percentage of the data lying within 2 stdev : " , p2)

print("The percentage of the data lying within 3 stdev : " , p3 )



