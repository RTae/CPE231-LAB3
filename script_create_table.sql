CREATE TABLE product (
    code character varying(10), 
    name character varying(100), 
    units character varying(10),
    PRIMARY KEY (code)
);
        
CREATE TABLE customer (
    customer_code character varying(10), 
    name character varying(100), 
    address character varying(100), 
    credit_limit numeric, 
    country character varying(20),
    PRIMARY KEY (customer_code)
); 
        
CREATE TABLE invoice (
    invoice_no character varying(10), 
    date date, 
    customer_code character varying(10), 
    due_date date, total numeric(18,2), 
    vat numeric(18,2), 
    amount_due numeric(18,2),
    PRIMARY KEY (invoice_no),
    CONSTRAINT invoice_customer_customer_code_fkey FOREIGN KEY (customer_code)
        REFERENCES customer (customer_code) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
);  

CREATE TABLE invoice_line_item (
    invoice_no character varying(10), 
    product_code character varying(10), 
    quantity integer, 
    unit_price numeric(18,2), 
    extended_price numeric(18,2),
    PRIMARY KEY (invoice_no,product_code),
    CONSTRAINT invoice_line_item_product_product_code_fkey FOREIGN KEY (product_code)
        REFERENCES product (code) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
);  

CREATE TABLE receipt (
    receipt_no character varying(10), 
    customer_code character varying(10),
	date date,
	payment_code character varying(10), 
	payment_ref character varying(50),
	total_received numeric(8,2),
	remark character varying(100),
    PRIMARY KEY (receipt_no),
    CONSTRAINT receipt_customer_customer_code_fkey FOREIGN KEY (customer_code)
        REFERENCES customer (customer_code) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT receipt_payment_payment_code_fkey FOREIGN KEY (payment_code)
        REFERENCES paymentmethod (code) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE receipt_line_item (
    receipt_no character varying(10), 
    invoice_no character varying(10), 
    aph numeric(18,2),
    PRIMARY KEY (receipt_no,invoice_no),
    CONSTRAINT receipt_line_item_invoice_invoice_code_fkey FOREIGN KEY (invoice_no)
        REFERENCES invoice (invoice_no) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
); 