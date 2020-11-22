import censusgeocode
import pandas as pd

cg = censusgeocode.CensusGeocode()

# Create a file with all the names of the address files you want to run through in one column.

getFile = pd.read_csv('filenames.csv', header=None)
nameList = getFile[0].tolist()

# Loop through the files and request a batch geocoding from the census geocoder. Each file should contain no more than 10,000 addresses (no header).

for x in nameList:
    result = cg.addressbatch(x)
    df = pd.DataFrame(result, columns=result[0].keys())
    if x == nameList[0]:
        df.to_csv('output.csv', mode='a', header=True)
    else:
        df.to_csv('output.csv', mode='a', header=False)

# Results are saved to one output file.

'''
After testing 3 10,000 line files:

Time1 = 33.57 minutes
Time2 = 29.83 minutes
Time3 = 36.9 minutes
Total Time = 1 hour 40 minutes

94.45% success rate
'''
