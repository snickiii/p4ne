from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

list_of_years = list(map(getvalue, sheet['A'][1:]))
list_of_temperatures = list(map(getvalue, sheet['C'][1:]))
list_of_activity = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(list_of_years, list_of_temperatures, label="Temperatures")
pyplot.plot(list_of_years, list_of_activity, label="Sun activity")

pyplot.xlabel('Year')
pyplot.ylabel('Temperature')
pyplot.legend(loc='upper left')

pyplot.show()
