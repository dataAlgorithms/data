#! coding=utf-8

class MongoDb:

    def __init__(self, db):
        self.db = db
    
    # Function to insert data into mongo db
    def insert(self):
        try:
            employeeId = raw_input('Enter Employee id :')
            employeeName = raw_input('Enter Name :')
            employeeAge = raw_input('Enter age :')
            employeeCountry = raw_input('Enter Country :')

            insertCmd = 'db.%s.insert_one' % self.db
            eval(insertCmd)(
              {
                "id": employeeId,
                "name":employeeName,
                "age":employeeAge,
                "country":employeeCountry
            })

            print '\nInserted data successfully\n'
        except Exception, e:
            print str(e)

    # function to read records from mongo db
    def read(self):
        try:
            readCmd = 'db.%s.find()' % self.db
            empCol = eval(readCmd)

            print '\n All data from EmployeeData Database \n'
            for emp in empCol:
                print emp

        except Exception, e:
            print str(e)

    # Function to update record to mongo db
    def update(self):
        try:
            criteria = raw_input('\nEnter id to update\n')
            name = raw_input('\nEnter name to update\n')
            age = raw_input('\nEnter age to update\n')
            country = raw_input('\nEnter country to update\n')

            updateCmd = 'db.%s.update_one' % self.db
            eval(updateCmd)(
               {"id": criteria},
               {
                    "$set": {
                        "name":name,
                        "age":age,
                        "country":country
                    }
                 }
            )
            print "\nRecords updated successfully\n"

        except Exception, e:
            print str(e)

    # Function to delete record from mongo db
    def delete(self):
        try:
            criteria = raw_input('\nEnter employee id to delete\n')
            deleteCmd = 'db.%s.delete_many' % self.db
            eval(deleteCmd)({"id":criteria})
            print '\nDeletion successful\n'
        except Exception, e:
            print str(e)
