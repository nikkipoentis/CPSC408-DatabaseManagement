class expedition():
    def __init__(self, connection):
        self.db = connection

    def set(self, data_dict, length):
        data = [] # list of lists (one list for each record/row)
        for i in range(length):
            row = [] # list of values for a single record
            row.append(int(data_dict.get("Expedition")[i])) # expeditionNumber
            row.append(int(data_dict.get("Duration")[i])) # Duration
            if self.exists(data, row) == False: # gets rid of any duplicates
                data.append(tuple(row)) # if the row doesn't already exist, then add it to the data list
        self.add(data)

    def add(self, data):
        placeholders = ("%s," * 2)[:-1] # creates a placeholder for each attribute
        query = "INSERT INTO expedition(expeditionNumber, Duration) VALUES("+placeholders+");"
        self.db.bulk_insert(query, data)

    # function for checking if the new row already exists or not
    def exists(self, data, row):
        for r in data:
            if row[0] == r[0]:
                if row[1] == r[1]:
                    return True
        return False
