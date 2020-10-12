from DBHelper import DBHelper
from helper_functions import *
#This file will contain all API functions calls exposed to outside world for users to use

# function about Product
def create_product(products, code, name, units):
    result = products.create(code, name, units)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Create Success.')
    return result #send result for caller program to use

def read_product(products, code):
    result = products.read(code) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_product(products, code, newName, newUnits):
    result = products.update(code, newName, newUnits) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Update Success.')
    return result #send result for caller program to use

def delete_product(products, code):
    result = products.delete(code)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Delete Success.')
    return result #send result for caller program to use

def report_list_products(products):
    result = products.dump()
    #printDictInCSVFormat(result, ('Code',), ('Name', 'Units'))
    print (result)
    return result #send result for caller program to use

# function about Customer 
def create_customer(customers, customerCode, customerName, address, creditLimit, country):
    result = customers.create(customerCode, customerName, address, creditLimit, country)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Create Success.')
    return result #send result for caller program to use

def read_customer(customers, customerCode):
    result = customers.read(customerCode) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_customer(customers, customerCode, newCustomerName, newAddress, newCreditLimit, newCountry):
    result = customers.update(customerCode, newCustomerName, newAddress, newCreditLimit, newCountry) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Update Success.')
    return result #send result for caller program to use

def delete_customer(customers, customerCode):
    result = customers.delete(customerCode)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Delete Success.')
    return result #send result for caller program to use

def report_list_all_customers(customers):
    result = customers.dump()
    printDictInCSVFormat(result, ('Customer Code',), ('Name', 'Address','Credit Limit', 'Country'))
    return result #send result for caller program to use

# function about Invoice 
def create_invoice(invoices, invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList):
    if invoiceDate == None:
        invoiceDate = 'null'
    else:
        invoiceDate = "'" + invoiceDate + "'"
    if dueDate == None:
        dueDate = 'null'
    else:
        dueDate = "'" + dueDate + "'"
    result = invoices.create(invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Create Success.')
    return result #send result for caller program to use

def read_invoice(invoices, invoiceNo):
    result = invoices.read(invoiceNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_invoice(invoices, invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList):
    if newInvoiceDate == None:
        newInvoiceDate = 'null'
    else:
        newInvoiceDate = "'" + newInvoiceDate + "'"
    if newDueDate == None:
        newDueDate = 'null'
    else:
        newDueDate = "'" + newDueDate + "'"
    result = invoices.update(invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Update Success.')
    return result #send result for caller program to use

def delete_invoice(invoices, invoiceNo):
    result = invoices.delete(invoiceNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Delete Success.')
    return result #send result for caller program to use

def update_invoice_line(invoices, invoiceNo, productCode, newQuantity, newUnitPrice):
    result = invoices.update_invoice_line(invoiceNo, productCode, newQuantity, newUnitPrice) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Update Success.')
    return result #send result for caller program to use

def delete_invoice_line(invoices, invoiceNo, productCode):
    result = invoices.delete_invoice_line(invoiceNo, productCode) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Delete Success.')
    return result #send result for caller program to use

def report_list_all_invoices(invoices, customers, products):
    # Will dump all invoices data and return 1 dictionary as a result (with header and line item joined).  
    # Please show the customer name and product name also. 
    # A helper function such as def print_tabular_dictionary(tabularDictionary) can then be called to print this in a tabular (table-like) form with column headings and data. 

    db = DBHelper()
    data, columns = db.fetch ('SELECT i.invoice_no as "Invoice No", i.date as "Date" '
                              ' , i.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , i.due_date as "Due Date", i.total as "Total", i.vat as "VAT", i.amount_due as "Amount Due" '
                              ' , ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , ili.quantity as "Quantity", ili.unit_price as "Unit Price", ili.extended_price as "Extended Price" '
                              ' FROM invoice i JOIN customer c ON i.customer_code = c.customer_code '
                              '  JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '  JOIN product p ON ili.product_code = p.code '
                              ' ')
    #print (result)
    result = row_as_dict(data, columns)
    printDictInCSVFormat(result, ('Invoice No',), ('Date', 'Customer Code', 'Customer Name','Due Date','Total','VAT','Amount Due'
                                                , 'Product Code', 'Product Name', 'Quantity', 'Unit Price', 'Extended Price'))
    return result #send result for caller program to use

def report_products_sold(invoices, products, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list of in products sold in the given date range in tabular format of: Product Code, Product Name, Total Quantity Sold, Total Value Sold. Here, (product code) will be unique. 
    # And 2) a second dictionary of the footer will also be returned containing: t the end also show the sum of Total Value Sold.  
    db = DBHelper()
    data, columns = db.fetch ('SELECT p.code as "Code", ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' GROUP BY p.code, ili.product_code, p.name ')
    result = row_as_dict(data, columns)
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' ')
    result2 = row_as_dict(data, columns)

    printDictInCSVFormat(result, (None), ('Product Code','Product Name', 'Total Quantity Sold', 'Total Value Sold'))
    printDictInCSVFormat(result2, (None), ('Total Value Sold',))
    return result, result2

def report_customer_products_sold_list(invoices, products, customers, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list of customers and list the products sold to them in the given date range in this format:  Customer Code, Customer Name, Product Code,  Product Name, Invoice No, Invoice Date, Quantity Sold, Value Sold. Here, (customer code, product code, invoice no) will be unique.  
    # And 2) a second footer dictionary showing:  At the end also show the sum of Quantity Sold and sum of Value Sold.
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.customer_code, c.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , i.invoice_no as "Invoice No" '
                              ' , SUM(ili.quantity) as "Quantity Sold", SUM(ili.extended_price) as "Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' GROUP BY i.customer_code, c.customer_code, c.name, i.invoice_no, ili.product_code, p.name ')
    result = row_as_dict(data, columns)
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(ili.quantity) as "Quantity Sold", SUM(ili.extended_price) as "Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' ')
    result2 = row_as_dict(data, columns)

    printDictInCSVFormat(result, (None), ('Customer Code','Customer Name', 'Product Code', 'Product Name', 'Invoice No', 'Quantity Sold', 'Value Sold'))
    printDictInCSVFormat(result2, (None), ('Quantity Sold','Value Sold'))
    return result.values(), result2

def report_customer_products_sold_total(invoices, products, customers, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list customers and the total number and value of products sold to them in the given date range in this format:  Customer Code, Customer Name, Product Code,  Product Name, Total Quantity Sold, Total Value Sold. Here (customer code, product code) will be unique.
    # And 2) a second footer dictionary showing: t the end also show the sum of Total Quantity Sold, sum of Total Value Sold.
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.customer_code, c.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' GROUP BY i.customer_code, c.customer_code, c.name, i.invoice_no, ili.product_code, p.name ')
    result = row_as_dict(data, columns)
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' ')
    result2 = row_as_dict(data, columns)

    printDictInCSVFormat(result, (None), ('Customer Code','Customer Name', 'Product Code', 'Product Name', 'Total Quantity Sold', 'Total Value Sold'))
    printDictInCSVFormat(result2, (None), ('Total Quantity Sold','Total Value Sold'))
    return result.values(), result2


def create_paymentMedthod(paymentMedthod, paymentMedthodNo, name):
    if name == None:
        name = 'null'
    else:
        name = "'" + name + "'"
    result = paymentMedthod.create(paymentMedthodNo, name)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Payment Medthod Create Success.')
    return result #send result for caller program to use

def read_paymentMedthod(paymentMedthod, paymentMedthodNo):
    result = paymentMedthod.read(paymentMedthodNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_paymentMedthod(paymentMedthod, paymentMedthodNo, name):
    if name == None:
        name = 'null'
    else:
        name = "'" + name + "'"
    result = paymentMedthod.update(paymentMedthodNo, name) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Payment Medthod Update Success.')
    return result #send result for caller program to use

def delete_paymentMedthod(paymentMedthod, paymentMedthodNo):
    result = paymentMedthod.delete(paymentMedthodNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Payment Medthod Delete Success.')
    return result #send result for caller program to use

def report_list_all_paymentMedthod():
    db = DBHelper()
    data, columns = db.fetch ('SELECT pm.code as "Code", pm.name as "Name" '
                              ' FROM paymentmethod as pm')
    result = row_as_dict(data, columns)
    #print (result)
    printDictInCSVFormat(result, ('Code',), ('Name',))
    return result #send result for caller program to use

def create_receipt(receipt, receiptNo, date, customer_code, payment_code, payment_ref, remark, receiptNoLineTuplesList):
    if receiptNo == None:
        receiptNo = 'null'
    else:
        receiptNo = "'" + receiptNo + "'"
    if customer_code == None:
        customer_code = 'null'
    else:
        customer_code = "'" + customer_code + "'"
    if date == None:
        date = 'null'
    else:
        date = "'" + date + "'"
    if payment_code == None:
        payment_code = 'null'
    else:
        payment_code = "'" + payment_code + "'"
    if payment_ref == None:
        payment_ref = 'null'
    else:
        payment_ref = "'" + payment_ref + "'"
    if remark == None:
        remark = 'null'
    else:
        remark = "'" + remark + "'"
    result = receipt.create(receiptNo, customer_code, date, payment_code, payment_ref, remark, receiptNoLineTuplesList)
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Create Success.')
    return result #send result for caller program to use

def read_receipt(receipt, receiptNo):
    result = receipt.read(receiptNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_receipt(receipt, receiptNo, new_date, new_customer_code, new_payment_code, new_payment_ref, new_remark,  new_receiptNoLineTuplesList):
    if receiptNo == None:
        receiptNo = 'null'
    else:
        receiptNo = "'" + receiptNo + "'"

    if new_customer_code == None:
        new_customer_code = 'null'
    else:
        new_customer_code = "'" + new_customer_code + "'"
    if new_date == None:
        new_date = 'null'
    else:
        new_date = "'" + new_date + "'"
    if new_payment_code == None:
        new_payment_code = 'null'
    else:
        new_payment_code = "'" + new_payment_code + "'"
    if new_payment_ref == None:
        new_payment_ref = 'null'
    else:
        new_payment_ref = "'" + new_payment_ref + "'"
    if new_remark == None:
        new_remark = 'null'
    else:
        new_remark = "'" + new_remark + "'"
    result = receipt.update(receiptNo, new_customer_code, new_date, new_payment_code, new_payment_ref, new_remark,  new_receiptNoLineTuplesList) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Update Success.')
    return result #send result for caller program to use

def delete_receipt(receipt, receiptNo):
    result = receipt.delete(receiptNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Delete Success.')
    return result #send result for caller program to use

def update_receipt_line(receipt, receiptNo, invoiceNo, newAPH):
    result = receipt.update_receipt_line(receiptNo, invoiceNo, newAPH) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Update Success.')
    return result #send result for caller program to use

def delete_receipt_line(receipt, receiptNo, invoiceNo):
    result = receipt.delete_receipt_line(receiptNo, invoiceNo) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Delete Success.')
    return result #send result for caller program to use

def report_list_all_receipts():
    # Will dump all receipt data and return 1 dictionary as a result (with header and line item joined).  
    # Please show the customer name and product name also. 
    # A helper function such as def print_tabular_dictionary(tabularDictionary) can then be called to print this in a tabular (table-like) form with column headings and data. 

    db = DBHelper()
    data, columns = db.fetch (' SELECT r.receipt_no as "Receipt No", r.date as "Date" '
                              ' , r.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , pm.name as "Payment Medthod", r.payment_ref as "Paymet Refercence" '
                              ' , r.remark as "Remarks", r.total_received as "Total received" '
                              ' , rli.invoice_no as "Invoice No", i.date as "Date",rli.aph as "Amount Paid Here" '
                              ' FROM receipt as r'
                              ' INNER JOIN customer as c '
                              '     ON r.customer_code = c.customer_code '
                              ' INNER JOIN paymentmethod as pm'
                              '     ON r.payment_code = pm.code '
                              ' INNER JOIN receipt_line_item as rli'
                              '     ON r.receipt_no = rli.receipt_no'
                              ' INNER JOIN invoice as i'
                              '     ON rli.invoice_no = i.invoice_no'
                              )
    #print(data)
    printCSVLineItem(data, columns)
    #print(result)
    #printDictInCSVFormat(result, ('Invoice No',), ('Date', 'Customer Code', 'Customer Name','Due Date','Total','VAT','Amount Due'
    #                                           , 'Product Code', 'Product Name', 'Quantity', 'Unit Price', 'Extended Price'))
    return data #send result for caller program to use

def report_unpaid_invoices():
    db = DBHelper()
    data, columns = db.fetch (
                            'SELECT "Invoice No", i.date AS "Invoice Date", \
		                        c.name as "Customer Name", i.amount_due AS "Invoice Amount Due",\
		                        "Invoice Amount Received", i.amount_due - "Invoice Amount Received" AS "Invoice Amount Not piad"\
                            FROM(SELECT rli.invoice_no AS "Invoice No", SUM(rli.aph) as "Invoice Amount Received"\
	                            FROM receipt_line_item as rli \
	                            GROUP BY rli.invoice_no ) as li \
                            INNER JOIN invoice as i \
	                            ON li."Invoice No" = i.invoice_no \
                            INNER JOIN customer as c \
	                            ON i.customer_code = c.customer_code \
                            WHERE i.amount_due - "Invoice Amount Received" !=  0'
                            )
    data1, columns1 = db.fetch (
                            'SELECT SUM(i.amount_due - "Invoice Amount Received") AS "Total invoice amount not paid", COUNT(li) AS "Number of Invoice not paid" \
                            FROM(SELECT rli.invoice_no AS "Invoice No", SUM(rli.aph) as "Invoice Amount Received"\
	                            FROM receipt_line_item as rli\
	                            GROUP BY rli.invoice_no )as li\
                            INNER JOIN invoice as i\
	                            ON li."Invoice No" = i.invoice_no'
                            )

    result1 = row_as_dict(data, columns)
    printDictInCSVFormat(result1, ('Invoice No',), ('Invoice Date', 'Customer Name', 'Invoice Amount Due', 'Invoice Amount Received', 'Invoice Amount Not piad'))
    
    dict_footer = {
        columns1[0]: data1[0][0],
        columns1[1]: data1[0][1]
    }
    print(dict_footer)