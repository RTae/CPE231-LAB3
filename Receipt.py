from DBHelper import DBHelper
from helper_functions import *
from Product import *
from Customer import *

class Receipt:
    def __init__(self):
        self.db = DBHelper()
    
    def __updateInvoiceTotal (self, receiptNo):
        sql = ("UPDATE receipt SET "
              " total_received = line_item.total_received "
              " FROM (SELECT receipt_no, SUM(aph) as total_received FROM receipt_line_item GROUP BY receipt_no) AS line_item "
              " WHERE receipt.receipt_no = line_item.receipt_no "
              " AND receipt.receipt_no = {} ".format(receiptNo))
        self.db.execute (sql)

    def __updateLineItem (self, receiptNo, invoiceLineTuplesList):
        self.db.execute ("DELETE FROM receipt_line_item WHERE receipt_no = {} ".format(receiptNo))
        for lineItem in invoiceLineTuplesList:
            self.db.execute ("INSERT INTO receipt_line_item (receipt_no, invoice_no, aph) VALUES ({} , '{}', {})".format(receiptNo,lineItem["Invoice No"],lineItem["Amount Paid Here"]))
        self.__updateInvoiceTotal(receiptNo)

    def create(self, receiptNo, customer_code, date, payment_code, payment_ref, remark, receiptNoLineTuplesList):
        # Adds the new invoice record to invoices object (dictionary).
        # Note that the function will calculate Total, VAT, and Amount Due
        #  from the data in the invoiceLineDictList parameter.  
        # The invoiceLineDictList data will be a list of dictionary,
        #  where each dictionary item of the list is in this example
        #  format: {'Product Code': 'HD01',  'Quantity': 2,  'Unit Price': 3000.00}.  
        # Note that for each line item the Extended Price will be calculated by the function using Quantity * Unit Price. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.

        data, columns = self.db.fetch ("SELECT * FROM receipt WHERE receipt_no = {} ".format(receiptNo))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Receipt No {} already exists. Cannot Create. ".format(receiptNo)}
        else:
            self.db.execute("INSERT INTO receipt (receipt_no, customer_code, date, payment_code, payment_ref, remark) VALUES ({} ,{}, {}, {}, {}, {})".format(receiptNo,customer_code, date, payment_code,payment_ref,remark))
            self.__updateLineItem(receiptNo, receiptNoLineTuplesList)

        return {'Is Error': False, 'Error Message': ""}

    def read(self, receiptNo):
        # Finds the invoice number in invoices object and returns 1invoice  record in dictionary form. 
        # Returns tuple dictionary, one for error, one for the data.
          
        data, columns = self.db.fetch ("SELECT * FROM receipt WHERE receipt_no = '{}' ".format(receiptNo))
        if len(data) > 0:
            retInvoice = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Read.".format(receiptNo)},{})

        return ({'Is Error': False, 'Error Message': ""},retInvoice)

    def update(self, receiptNo, new_customer_code, new_date, new_payment_code, new_payment_ref, new_remark,  new_receiptNoLineTuplesList):
        # Finds the invoice number in invoices object and then changes the values to the new ones. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.
        data, columns = self.db.fetch ("SELECT * FROM receipt WHERE receipt_no = {} ".format(receiptNo))
        if len(data) > 0:
            self.db.execute ("UPDATE receipt SET customer_code = {}, date = {}, payment_code = {}, payment_ref = {}, remark = {} WHERE receipt_no = {} ".format(new_customer_code,new_date,new_payment_code,new_payment_ref,new_remark,receiptNo))
            self.__updateLineItem(receiptNo, new_receiptNoLineTuplesList)
        else:
            return {'Is Error': True, 'Error Message': "Receipt No '{}' not found. Cannot Update.".format(receiptNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, receiptNo):
        # Finds the invoice number invoices object and removes it from the dictionary. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}.
        data, columns = self.db.fetch ("SELECT * FROM receipt WHERE receipt_no = '{}' ".format(receiptNo))
        if len(data) > 0:
            self.db.execute ("DELETE FROM receipt WHERE receipt_no = '{}' ".format(receiptNo))
            self.db.execute ("DELETE FROM receipt_line_item WHERE receipt_no = '{}' ".format(receiptNo))
        else:
            return {'Is Error': True, 'Error Message': "Invoice No '{}' not found. Cannot Delete".format(receiptNo)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all invoice data by returning 1 dictionary as output.
        data, columns = self.db.fetch ('SELECT * FROM receipt_no')
        return data, columns

    def update_receipt_line(self, receiptNo, invoiceNo, newAPH):
        # The line item of this receipt number is updated for this invoice code.  
        # Note that the extended price must also be recalculated, 
        #  after which all the related data in the receipt must be updated such as aph. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}. 
        data, columns = self.db.fetch ("SELECT * FROM receipt_line_item WHERE receipt_no = '{}' AND invoice_no = '{}' ".format(receiptNo, invoiceNo))
        if len(data) > 0:
            self.db.execute ("UPDATE receipt_line_item SET aph = {}  WHERE receipt_no = '{}' AND invoice_no = '{}' ".format(newAPH, receiptNo, invoiceNo))
            receiptNo = "'"+receiptNo+"'"
            self.__updateInvoiceTotal(receiptNo)
        else:
            return {'Is Error': True, 'Error Message': "Invocie Code '{}' not found in Receipt No '{}'. Cannot Update.".format(invoiceNo, receiptNo)}

        return {'Is Error': False, 'Error Message': ""}

    def delete_receipt_line(self, receiptNo, invoiceNo):
        # The line item of this invoice number is updated to delete this product code.  
        # Note that all the related data in the invoice must be updated such as Total, VAT, and Amount Due. 
        # Returns dictionary {‘Is Error’: ___, ‘Error Message’: _____}
        data, columns = self.db.fetch ("SELECT * FROM receipt_line_item WHERE receipt_no = '{}' AND invoice_no = '{}' ".format(receiptNo, invoiceNo))
        if len(data) > 0:
            self.db.execute ("DELETE FROM receipt_line_item WHERE receipt_no = '{}' AND invoice_no = '{}' ".format(receiptNo, invoiceNo))
            receiptNo = "'"+receiptNo+"'"
            self.__updateInvoiceTotal(receiptNo)

        else:
            return {'Is Error': True, 'Error Message': "Product Code '{}' not found in Invoice No '{}'. Cannot Delete.".format(invoiceNo, receiptNo)}

        return {'Is Error': False, 'Error Message': ""}

