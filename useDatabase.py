from mysql import connector


class UseDatabase:
    def __init__(self):
        cnx = connector.connect(user='root', password='Skoda313100',
                                      host='localhost',
                                      database='datas')
        cursor = cnx.cursor()


    def insertData(self, fileName, detectedData):
        addData = ("INSERT INTO datas "
                        "(id,timelapse_name, frame_number, time_taken, weather_data, pollution_data, other) "
                        "VALUES (,%s, %s, %s, %s, %s)")

        self.cursor.execute(addData, detectedData)
        self.cnx.commit()
        cursor.close()

    def getRow(self, timelapseName, frameNumber):
        query = ("SELECT * FROM datas "
                 "WHERE timelapse_name = %s AND frame_number = %s")
        cnx.execute(query, (timelapseName, frameNumber))
        cursor.close()

    def getTimelapse(self, timelapseName):
        query = ("SELECT * FROM datas "
                 "WHERE timelapse_name = %s ORDER BY frame_number ASC")
        cnx.execute(query,(timelapseName))
        cursor.close()

    def closeDatabase(self):
        cnx.close()
