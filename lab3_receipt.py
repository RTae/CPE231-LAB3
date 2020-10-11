from helper_functions import *
from Invoice import *
from Product import *
from Customer import *
from PaymentMedthod import *
from Receipt import *
from API import *

def main():
    try:

        invoices = Invoice()
        receipts=Receipt()
        create_receipt(receipts, "RCT1002/20", "Sam", "2020-02-05", "CC", "Master Card, Citibank","Partially paid on IN101/20",
                       [{"invoice_no": "INT100/20", "aph":8560.00},{"invoice_no": "INT101/20", "aph":1440.00}])
        report_list_all_receipt()
        waitKeyPress("Results after create receipt")

        read_receipt(receipts,"RCT1002/20")
        waitKeyPress("Results read receipt")

        update_receipt(receipts, "RCT1002/20", "Sam", "2020-02-05", "PP", "Master Card, Citibank","Partially paid on IN101/20",
                       [{"invoice_no": "INT100/20", "aph":8560.00},{"invoice_no": "INT101/20", "aph":1440.00}])
        report_list_all_receipt()
        waitKeyPress("Results update receipt")

        update_receipt_line(receipts, "RCT1002/20", "INT100/20", 2000.00)
        report_list_all_receipt()
        waitKeyPress("Results update receipt line item")

        delete_receipt_line(receipts, "RCT1002/20", "INT100/20")
        report_list_all_receipt()
        waitKeyPress("Results delete receipt line item")

        delete_receipt(receipts, "RCT1002/20")
        report_list_all_receipt()
        waitKeyPress("Results delete receipt")

        create_receipt(receipts, "RCT1002/20", "Sam", "2020-02-05", "CC", "Master Card, Citibank","Partially paid on IN101/20",
                       [{"invoice_no": "INT100/20", "aph":8560.00},{"invoice_no": "INT101/20", "aph":1440.00}])
        report_list_all_receipt()
        waitKeyPress("Results after create receipt")

        report_unpaid_invoices()
        waitKeyPress("Results after report unpaid invoice")

    except: 
        print ("Unexpected error:", sys.exc_info()[0])
        raise 
    else:
        print("Normal Termination.   Goodbye!")

if __name__ == "__main__":
    main()