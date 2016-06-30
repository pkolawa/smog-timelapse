import MySQLdb


class UseDatabase:
    def __init__(self):
        self.cnx = MySQLdb.connect(user='root', passwd='Skoda313100',
                                      host='localhost',
                                      db='timelapses')

    def insertData(self, fileName, frame_number):
        addData = ("""INSERT INTO datass (timelapse_name, frame_number) VALUES ('"""+str(fileName)+"""', """+str(frame_number)+""")""")
        self.cnx.query(addData)
        self.cnx.commit()

    def getRow(self, frameNumber):
        selection = ("""SELECT * FROM datass WHERE frame_number = '"""+str(frameNumber)+"""'""")
        self.cnx.query(selection)
        results = self.cnx.use_result()
        return results

    def getTimelapse(self, fileName):
        selection = ("""SELECT * FROM datass WHERE timelapse_name = '"""+str(fileName)+"""' ORDER BY frame_number ASC""")
        self.cnx.query(selection)
        results = self.cnx.use_result()
        resulty = results.fetchall()
        return resulty

    def closeDatabase(self):
        cnx.close()
