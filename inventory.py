import numpy as np 
import pandas as pd 


pd.set_option('display.width',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)


PRODUCT_DATA = {'Product': 'ProductImportTemplate.csv',
                    'Barcode': 'StockBarcodeImportTemplate.csv',
                    'Stock': 'StockImportTemplate.csv'}

def select_data():
    while True:
        user_choice = input('1. Product\n2. Barcode\n3. Stock\n')
        if len(user_choice) > 1 and (user_choice < '1' and user_choice >= '3'):
            print("Input 1-3")
        else:
            if int(user_choice) == 1:
                df = pd.read_csv(PRODUCT_DATA['Product'])
                return df
            elif int(user_choice) == 2:
                df = pd.read_csv(PRODUCT_DATA['Barcode'])
                return df
            elif int(user_choice) == 3:
                df = pd.read_csv(PRODUCT_DATA['Stock'])
                return df
            else:
                print('Something went wrong')
            
def explore_data(df):
    while True:
        line = 0
        print(df[line:line+5])
        print('Y/N')
        if input().lower() == 'n':
            break
        line +=5


def find_null(df):
    return 0



def main():
    df = select_data()
    explore_data(df)
    find_null(df)

if __name__ == "__main__":
    main()