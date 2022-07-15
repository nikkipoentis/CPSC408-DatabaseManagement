import csv
from db_operations import db_operations
from agency import agency
from expedition import expedition
from astronaut import astronaut
from astro_expedition import astro_expedition

db = db_operations()
# creates class instances for each database table passing in the db operations object (database connection)
agencyInfo = agency(db)
expeditionInfo = expedition(db)
astronautInfo = astronaut(db)
astro_expeditionInfo = astro_expedition(db)

def load_csv():
    file = open('expeditionData.csv')
    reader = csv.reader(file, delimiter = '\n')
    data = [] # list of lists (one list per row)
    for row in reader: # reads each row in the file as a string
        newrow = row[0].split(',') # converts each row into a list by splitting at commas
        data.append(newrow)
    return create_attributes(data)

def create_attributes(data):
    data_dict = {}
    for i in range(0,len(data[0])): # each value from the first row is used as an attribute name
        column = [] # list of lists (one list per column)
        for j in range(1,len(data)):
            column.append(data[j][i]) # iterates through all rows to get the value for the current column
        data_dict[data[0][i]] = column # uses list of value as the value in the dictionary (attribute name is key)
    return data_dict

data_dict = load_csv()
numrow = len(data_dict.get("Age")) # find number of rows in original csv file (how many to iterate through)
agencyInfo.set(data_dict, numrow)
expeditionInfo.set(data_dict, numrow)
astronautInfo.set(data_dict, numrow)
astro_expeditionInfo.set(data_dict, numrow)
