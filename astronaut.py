class astronaut():
    def __init__(self, connection):
        self.db = connection

    def set(self, data_dict, length):
        data = [] # list of lists (one list for each record/row)
        for i in range(length):
            row = [] # list of values for a single record
            row.append(str(data_dict.get("Astronaut")[i])) # Name
            row.append(int(data_dict.get("Age")[i])) # Age
            # gets the agency name from the dictionary of data (in the corresponding row)
            agency_name = str(data_dict.get("Agency")[i])
            # retrieves agencyID value from the agency table and adds to the row
            query = "SELECT agencyID FROM agency WHERE Name = %s;"
            row.append(self.db.getID(query, agency_name)) # Agency
            if self.exists(data, row) == False: # gets rid of any duplicates
                data.append(tuple(row)) # if the row doesn't already exist, then add it to the data list
        self.add(data)

    def add(self, data):
        placeholders = ("%s," * 3)[:-1] # creates a placeholder for each attribute
        query = "INSERT INTO astronaut(Name, Age, Agency) "
        query += "VALUES("+placeholders+");"
        self.db.bulk_insert(query, data)

    # function for checking if the new row already exists or not
    def exists(self, data, row):
        for r in data:
            if row[0] == r[0]:
                if row[1] == r[1]:
                    if row[2] == r[2]:
                        return True
        return False
