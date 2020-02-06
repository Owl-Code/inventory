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
    while True:
        line = 0
        print(df[line:line+5])
        print('5 more lines?(Y/N)')
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