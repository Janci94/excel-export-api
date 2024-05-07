import decimal

def calculate_sum(data):
    decimal_columns = [col for col in data[0] if isinstance(data[0][col], decimal.Decimal)]
    sum_data = {'NazovStlpca': decimal_columns, 'Suma': []}
    for col in decimal_columns:
        sum_data['Suma'].append(sum(row[col] for row in data))
    return sum_data



'''def calculate_sum(data):
    sum_data = {
        'NazovStlpca': ['AmountExcludingTax', 'TaxAmount', 'TransactionAmount'],
        'Suma': [
            sum(row['AmountExcludingTax'] for row in data),
            sum(row['TaxAmount'] for row in data),
            sum(row['TransactionAmount'] for row in data)
        ]
    }
    return sum_data'''
