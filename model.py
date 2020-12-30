from DBConnector import DBConnect

class Model:
    def __init__(self,table,column):
        self.table = table
        self.column = column

    def insert(self,values):
        connection = DBConnect()
        query = """INSERT INTO """+self.table+"("
        for column in self.column:
            query+=column+","
        query = query[:-1]
        query+=") VALUES ("
        for value in values:
            query+="'"+str(value)+"',"
        query = query[:-1]
        query+=")"
        connection.execute(query)
        print("Data berhasil dientrikan")
    
    def insert_single(self,values):
        connection = DBConnect()
        query = "INSERT INTO "+self.table+"("+self.column+")"+" VALUES (\'%s\');"
        query = query  % (values)
        connection.execute(query)
        
        
    def update(self,values,wherekey,keyword):
        connection = DBConnect()
        query = "UPDATE "+self.table+" SET "+self.column+" = "+str(values)
        query+= " WHERE "+str(wherekey)
        query+= " = "+str(keyword)
        connection.execute(query)
        print("Data berhasil di update")
        
    def view(self):
        connection = DBConnect()
        query = "SELECT * FROM "+self.table
        result = connection.select(query)
        return result
    
    def getColumn(self):
        return self.column
    
    def getTableName(self):
        return self.table
        