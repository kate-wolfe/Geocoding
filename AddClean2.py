import pandas as pd
import numpy as np
import re

df = pd.read_csv('C:/Users/Kate/Desktop/campatrons11-24-20.txt', sep='^', encoding='utf8', \
    dtype={'RECORD #(PATRON)': str, 'MA TOWN': int, 'P TYPE': int, 'TOT CHKOUT': int, \
    'CUR CHKOUT': int, 'HOME LIBR': str, 'PCODE4': int, 'CREATED (PATRON)': str, \
    'ADDRESS': str, 'ADDRESS2': str, 'DRA CREATE': str, 'PATRN NAME': str, 'BIRTH DATE': str, \
    'DECADE': str})


add1List = df['ADDRESS'].tolist()
add2List = df['ADDRESS2'].tolist()
patrec = df['RECORD #(PATRON)'].tolist()


pat1dollarstreet = r"(\d.*)"
pat1dollarcity = r"(.*)([A-Za-z][A-Za-z])(.*)(\d\d\d\d\d)"

pat2dollarstreet = r"^((?!(Mail|mail)).)*$"

street = []
city = []
state = []
zipcode = []
patID = []

for i in range(len(add1List)):
    addSplit1 = str(add1List[i]).split('$')
    addSplit2 = str(add2List[i]).split('$')
    if len(addSplit1) == 2:
        if re.match(pat1dollarstreet, addSplit1[0]) and re.match(pat1dollarcity, addSplit1[1]):
            patID.append(patrec[i])
            street.append(re.search(pat1dollarstreet, addSplit1[0]).group(1))
            city.append(re.search(pat1dollarcity, addSplit1[1]).group(1))
            state.append(re.search(pat1dollarcity, addSplit1[1]).group(2))
            zipcode.append(re.search(pat1dollarcity, addSplit1[1]).group(4))
        else:
            if len(addSplit2) == 2:
                if re.match(pat1dollarstreet, addSplit2[0]) and re.match(pat1dollarcity, addSplit2[1]):
                    patID.append(patrec[i])
                    street.append(re.search(pat1dollarstreet, addSplit2[0]).group(1))
                    city.append(re.search(pat1dollarcity, addSplit2[1]).group(1))
                    state.append(re.search(pat1dollarcity, addSplit2[1]).group(2))
                    zipcode.append(re.search(pat1dollarcity, addSplit2[1]).group(4))
                else:
                    pass
            elif len(addSplit2) == 3:
                if re.match(pat2dollarstreet, addSplit2[0]) and re.match(pat1dollarcity, addSplit2[2]):
                    patID.append(patrec[i])
                    street.append(re.search(pat2dollarstreet, addSplit2[0]).group(1))
                    city.append(re.search(pat1dollarcity, addSplit2[2]).group(1))
                    state.append(re.search(pat1dollarcity, addSplit2[2]).group(2))
                    zipcode.append(re.search(pat1dollarcity, addSplit2[2]).group(4))
                elif re.match(pat2dollarstreet, addSplit2[1]) and re.match(pat1dollarcity, addSplit2[2]):
                    patID.append(patrec[i])
                    street.append(re.search(pat2dollarstreet, addSplit2[1]).group(1))
                    city.append(re.search(pat1dollarcity, addSplit2[2]).group(1))
                    state.append(re.search(pat1dollarcity, addSplit2[2]).group(2))
                    zipcode.append(re.search(pat1dollarcity, addSplit2[2]).group(4))
                else:
                    pass
            else:
                pass
    elif len(addSplit1) == 3:
        if re.match(pat2dollarstreet, addSplit1[0]) and re.match(pat1dollarcity, addSplit1[2]):
            patID.append(patrec[i])
            street.append(re.search(pat2dollarstreet, addSplit1[0]).group(1))
            city.append(re.search(pat1dollarcity, addSplit1[2]).group(1))
            state.append(re.search(pat1dollarcity, addSplit1[2]).group(2))
            zipcode.append(re.search(pat1dollarcity, addSplit1[2]).group(4))
        elif re.match(pat2dollarstreet, addSplit1[1]) and re.match(pat1dollarcity, addSplit1[2]):
            patID.append(patrec[i])
            street.append(re.search(pat2dollarstreet, addSplit1[1]).group(1))
            city.append(re.search(pat1dollarcity, addSplit1[2]).group(1))
            state.append(re.search(pat1dollarcity, addSplit1[2]).group(2))
            zipcode.append(re.search(pat1dollarcity, addSplit1[2]).group(4))
        else:
            pass
    else:
        pass

dfOut = pd.DataFrame() 

dfOut['ID'] = patID
dfOut['Street'] = street
dfOut['City'] = city
dfOut['State'] = state
dfOut['Zipcode'] = zipcode

#dfOut.to_csv('C:/Users/Kate/Desktop/outfullco.csv', sep=',', index=False, header=False)

df1 = dfOut.iloc[:10000,:]
df2 = dfOut.iloc[10001:20000,:]
df3 = dfOut.iloc[20001:30000,:]
df4 = dfOut.iloc[30001:40000,:]
df5 = dfOut.iloc[40001:50000,:]
df6 = dfOut.iloc[50001:60000,:]
df7 = dfOut.iloc[60001:70000,:]
df8 = dfOut.iloc[70001:80000,:]
df9 = dfOut.iloc[80001:,:]

df1.to_csv('C:/Users/Kate/Desktop/out1.csv', sep=',', index=False, header=False)
df2.to_csv('C:/Users/Kate/Desktop/out2.csv', sep=',', index=False, header=False)
df3.to_csv('C:/Users/Kate/Desktop/out3.csv', sep=',', index=False, header=False)
df4.to_csv('C:/Users/Kate/Desktop/out4.csv', sep=',', index=False, header=False)
df5.to_csv('C:/Users/Kate/Desktop/out5.csv', sep=',', index=False, header=False)
df6.to_csv('C:/Users/Kate/Desktop/out6.csv', sep=',', index=False, header=False)
df7.to_csv('C:/Users/Kate/Desktop/out7.csv', sep=',', index=False, header=False)
df8.to_csv('C:/Users/Kate/Desktop/out8.csv', sep=',', index=False, header=False)
df9.to_csv('C:/Users/Kate/Desktop/out9.csv', sep=',', index=False, header=False)
