import openpyxl as xls
import pprint
wb = xls.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}
for row in range(2, sheet.max_row + 1):
    state = sheet['b' + str(row)].value
    county = sheet['c' + str(row)].value
    pop = sheet['d' + str(row)].value

    countyData.setdefault(state,{})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData)) #Print in Python format
resultFile.close()
