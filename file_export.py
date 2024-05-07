import pandas as pd

def export_to_excel(data, phrase):
    df = pd.DataFrame(data)
    excel_filename = f'Top 10 of {phrase}.xlsx'
    df.to_excel(excel_filename, index=False)
