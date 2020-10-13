from DBHelper import DBHelper
from helper_functions import *
from Product import *
from Customer import *

class paymentMethod:
    def __init__(self):
        self.db = DBHelper()

    def create(self, paymentMedthodNo, name):
        data, columns = self.db.fetch ("SELECT * FROM paymentmethod WHERE code = '{}' ".format(paymentMedthodNo))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Payment No '{}' already exists. Cannot Create. ".format(paymentMedthodNo)}
        else:
            self.db.execute ("INSERT INTO paymentmethod (code, name) VALUES ('{}' ,{})".format(paymentMedthodNo,name))

        return {'Is Error': False, 'Error Message': ""}

    def read(self, paymentMedthodNo): 
        data, columns = self.db.fetch ("SELECT code, name FROM paymentmethod WHERE code = '{}' ".format(paymentMedthodNo))
        if len(data) > 0:
            retInvoice = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Payment No '{}' not found. Cannot Read.".format(paymentMedthodNo)},{})

        return ({'Is Error': False, 'Error Message': ""},retInvoice)

    def update(self, paymentMedthodNo, newName):
        data, columns = self.db.fetch ("SELECT * FROM paymentmethod WHERE code = '{}' ".format(paymentMedthodNo))
        if len(data) > 0:
            self.db.execute ("UPDATE paymentmethod SET name = {} WHERE code = '{}'".format(newName,paymentMedthodNo))
        else:
            return {'Is Error': True, 'Error Message': "Payment No '{}' not found. Cannot Update.".format(paymentMedthodNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, paymentMedthodNo):
        # Finds the invoice number invoices object and removes it from the dictionary. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.
        data, columns = self.db.fetch ("SELECT * FROM paymentmethod WHERE code = '{}' ".format(paymentMedthodNo))
        if len(data) > 0:
            self.db.execute ("DELETE FROM paymentmethod WHERE code = '{}' ".format(paymentMedthodNo))
        else:
            return {'Is Error': True, 'Error Message': "Payment No '{}' not found. Cannot Delete".format(paymentMedthodNo)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all invoice data by returning 1 dictionary as output.
        
        data, columns = self.db.fetch ("SELECT * FROM paymentmethod")
        return row_as_dict(data, columns)