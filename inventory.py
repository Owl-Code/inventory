import pandas as pd 


pd.set_option('display.width',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)


PRODUCT_DATA = {1: 'ProductImportTemplate.csv',
                    2: 'StockBarcodeImportTemplate.csv',
                    3: 'StockImportTemplate.csv'}

def select_data():
    """
        Ask user for a csv filename(s)

        ARGS: 
            None
        RETURN:
            product_df - Pandas data frame loaded from a product csv
            stock_df - Pandas data frame loaded from stock csv
    """
    while True:
        user_choice = list(input('Name of csv\n').split(', '))
        df = []
        try:
            for choice in user_choice:
                print(choice)
                df.append(pd.read_csv(choice))
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
        #need to add a check for end of dataframe
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

def find_sell_value(df):
    """
        Find the the value of the store by multiplying 
        the current held stock by the sell price. 
        ARGS:
            (pandas.DataFrame) df
        RETURNS: 
            sum() - the sum of all current stock rows * sale price rows
    """
    sale_price_idx = ''
    if 'Sale Price' in df:
        sale_price_idx = 'Sale Price'
    elif 'Selling Price' in df:
        sale_price_idx = 'Selling Price'

    if 'Current Stock' in df:
        return (df['Current Stock'] * df[sale_price_idx]).sum()


def main():
    df = select_data()
    df_join = df[0].merge(df[1], on='Product Name')
    explore_data(df_join)
    null_df = find_null(df_join)
    explore_data(null_df)
    inventory_df = find_inventory(df_join)
    explore_data(inventory_df)
    full_inventory_value = find_sell_value(df_join)
    overstocked_value = find_sell_value(inventory_df.merge(df[0]))
    print('Full inventory value: {}\nOverstocked Value: {}\nApproximate Real Value: {}'.format(full_inventory_value, overstocked_value, full_inventory_value-overstocked_value))

if __name__ == "__main__":
    main()