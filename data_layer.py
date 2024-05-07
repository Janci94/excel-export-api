import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv("DB_CONNECTION_STRING")

def fetch_data_from_db(phrase):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        query = f'''
            SELECT TOP 10 
                I.InvoiceID, 
                C.CustomerName, 
                CT.AmountExcludingTax, 
                CT.TaxAmount, 
                CT.TransactionAmount
            FROM 
                Sales.CustomerTransactions AS CT
            LEFT JOIN 
                Sales.Invoices AS I ON CT.InvoiceID = I.InvoiceID
            LEFT JOIN 
                Sales.Customers AS C ON I.CustomerID = C.CustomerID
            WHERE
                C.CustomerName LIKE '%{phrase}%'
            ORDER BY 
                CT.TransactionAmount DESC
        '''

        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()

        # Convert rows to list of dictionaries
        result = []
        for row in data:
            result.append({
                'InvoiceID': row.InvoiceID,
                'CustomerName': row.CustomerName,
                'AmountExcludingTax': row.AmountExcludingTax,
                'TaxAmount': row.TaxAmount,
                'TransactionAmount': row.TransactionAmount
            })

        return result

    except Exception as e:
        raise e
