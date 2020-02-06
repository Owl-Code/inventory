import pandas as pd 


pd.set_option('display.width',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)


PRODUCT_DATA = {1: 'ProductImportTemplate.csv',
                    2: 'StockBarcodeImportTemplate.csv',
                    3: 'StockImportTemplate.csv'}

def select_data():
    """
        Ask user for a csv filename 

        ARGS: 
            None
        RETURN:
            df - Pandas data frame loaded from a csv
    """
    while True:
        user_choice = input('Name of csv\n')
        try:
            df = pd.read_csv(user_choice)
            return df
        except:
            print('Something went wrong\nYou Entered {}\n'.format(user_choice))
            
def explore_data(df):
    """
        Lets user look through five rows of the data frame and prompts i
        if they would like to continue.
        ARGS:
            (pandas.DataFrame) df
        RETURNS:
            None
    """
    
    line = 0
    while True:
        print(df[line:line+5])
        print('5 more lines?(Y/N)')
        if input().lower() == 'n':
            break
        line += 5


def find_null(df):
    """
        Find null barcode columns in data frame
        found at https://chartio.com/resources/tutorials/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe/
        ARGS: 
            (pandas.DataFrame) df
        RETURNS:
            null_df - pandas dataframe of rows with a null barcode

    """
    if 'Barcode' in df:
        null_df = df[df['Barcode'].isnull()]
        print('null barcode found')
        null_df = null_df[['Product Name', 'Barcode']]
        return null_df
    return df

def find_inventory(df):
    """
        Find products with more inventory than a user defined 
        input. Return a data frame of products with inventory 
        over max value
        ARGS:
            (pandas.DataFrame) df
        RETURN:
            inventory_df - pandas dataframe with Product over max_inventory
    """
    while True:
        max_inventory = input('How much for max inventory?\n')
        try:
            max_inventory = int(max_inventory)
            break
        except:
            print('Not a number')
    if 'Current Stock' in df:
        print('Stock found')
        total_stock = int(df['Current Stock'].sum())
        df = df[df['Current Stock']> max_inventory]
        df = df[['Product Name', 'Current Stock']]
        print('Total Stock count: ', total_stock)
        print('Stock over {} count: '.format(max_inventory), int(df['Current Stock'].sum()))
        print('Approximate real count: ', total_stock - int(df['Current Stock'].sum()) + int(df['Current Stock'].count()*100))

        return df
    return df 


def main():
    df = select_data()
    explore_data(df)
    null_df = find_null(df)
    explore_data(null_df)
    inventory_df = find_inventory(df)
    explore_data(inventory_df)

if __name__ == "__main__":
    main()