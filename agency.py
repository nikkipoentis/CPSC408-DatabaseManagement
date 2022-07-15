class agency():
    def __init__(self, connection):
        self.db = connection

    def set(self, data_dict, length):
        data = [] # list of lists (one list for each record/row)
        for i in range(length):
            row = [] # list of values for a single record
            row.append(str(data_dict.get("Agency")[i])) # Name
            row.append(str(data_dict.get("agencyOrigin")[i])) # Origin
            if self.exists(data, row) == False: # gets rid of any duplicates
                data.append(tuple(row)) # if the row doesn't already exist, then add it to the data list
        self.add(data)

    def add(self, data):
        placeholders = ("%s," * 2)[:-1] # creates a placeholder for each attribute
        query = "INSERT INTO agency(Name, Origin) VALUES("+placeholders+");"
        self.db.bulk_insert(query, data)

    # function for checking if the new row already exists or not
    def exists(self, data, row):
        for r in data:
            if row[0] == r[0]:
                if row[1] == r[1]:
                    return True
        return False
