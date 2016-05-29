import mysql


class UseDatabase:
    def __init__(self):
        cnx = mysql.connector.connect(user='root', password='tiger',
                                      host='localhost',
                                      database='datas')
        cursor = cnx.cursor()


    def insertData(self, fileName, detectedData):
        addData = ("INSERT INTO datas "
                        "(first_name, last_name, hire_date, gender, birth_date) "
                        "VALUES (%s, %s, %s, %s, %s)")

        cursor.execute(addData, detectedData)
        self.cnx.commit()

    def getRow(self):

    def getTimelapse(self):

    def closeDatabase(self):
        self.cnx.close()
