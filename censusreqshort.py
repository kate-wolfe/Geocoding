import censusgeocode
import pandas as pd
import time

starttime = time.perf_counter()
print(starttime)

cg = censusgeocode.CensusGeocode()

getFile = pd.read_csv('C:/Users/Kate/Desktop/filenames.csv', header=None)
nameList = getFile[0].tolist()

for x in nameList:
    print(time.perf_counter())
    result = cg.addressbatch(x)
    print(time.perf_counter())
    df = pd.DataFrame(result, columns=result[0].keys())
    if x == nameList[0]:
        df.to_csv('C:/Users/Kate/Desktop/outputPatronsFinal3.csv', mode='a', header=True)
    else:
        df.to_csv('C:/Users/Kate/Desktop/outputPatronsFinal3.csv', mode='a', header=False)
    print(time.perf_counter())

endtime = time.perf_counter()
print(endtime)

print(f"Total time: {endtime - starttime:0.4f} seconds")

'''
8.84 hours for 81,000 lines
92% success
'''
