class astro_expedition():
    def __init__(self, connection):
        self.db = connection

    def set(self, data_dict, length):
        data = [] # list of lists (one list for each record/row)
        astronauts = data_dict.get("Astronaut")
        expeditions = data_dict.get("Expedition")
        for i in range(length):
            row = [] # list of values for a single record
            row.append(int(expeditions[i])) # Expedition
            query = "SELECT astronautID FROM astronaut WHERE Name = %s;"
            row.append(self.db.getID(query, str(astronauts[i]))) # Astronaut
            if self.exists(data, row) == False: # gets rid of any duplicates
                data.append(tuple(row)) # if the row doesn't already exist, then add it to the data list
        self.add(data)

    def add(self, data):
        placeholders = ("%s," * 2)[:-1] # creates a placeholder for each attribute
        query = "INSERT INTO astro_expedition(Expedition, Astronaut) "
        query += "VALUES("+placeholders+");"
        self.db.bulk_insert(query, data)

    # function for checking if the new row already exists or not
    def exists(self, data, row):
        for r in data:
            if row[0] == r[0]:
                if row[1] == r[1]:
                    return True
        return False
