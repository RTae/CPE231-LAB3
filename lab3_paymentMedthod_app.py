from PaymentMedthod import *
from Receipt import *
from API import *

def main():
    try:

        paymentMethods = paymentMethod()
        create_paymentMedthod(paymentMethods, "CC", "Credit Card")
        create_paymentMedthod(paymentMethods, "DC", "Debit Card")
        create_paymentMedthod(paymentMethods, "PP", "Prompt Pay")
        create_paymentMedthod(paymentMethods, "C", "Cash")
        report_list_all_paymentMedthod()
        waitKeyPress("Results after create payment methods")

    except: 
        print ("Unexpected error:", sys.exc_info()[0])
        raise 
    else:
        print("Normal Termination.   Goodbye!")

if __name__ == "__main__":
    main()