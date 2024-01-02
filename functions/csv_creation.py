import os
import csv
import time
import datetime


def new_csv()->None:
    '''This function creates the recap CSV file if it does not exist'''
    # Current folder
    folder = os.getcwd()

    # File path
    file_path = folder + "/data_recap/recap.csv"
    
    # Create recap.csv file in the data_recap folder, if doesn't exist
    if os.path.isfile(file_path) == True:
        pass
    else:
    # Create settings file
        with open(file_path, "w", newline='') as recap_file:
            # Write headers of the CSW
            writer = csv.DictWriter(recap_file, fieldnames=["crypto", "value", "currency", "data"])
            writer.writeheader()
            # Gives time to write and closes the file
            time.sleep(2)
            recap_file.close()

def write_data(crypto:str, data:str, currency:str)->None:
    '''This function writes the crypto selected by the user, its value in the currency selected by the user, the currency, and today's date in the recap CSV.\n

    The crypto and currency variables are selected by the user in the main.py file./n

    **NOTE**: crypto, data, and currency are created in the `price.py` module.
    '''
    # Current folder
    folder = os.getcwd()

    # File path
    file_path = folder + "/data_recap/recap.csv"
    
    with open(file_path, "a") as csv_recap:
        # Defines today in the format "d-m-y"
        today = datetime.datetime.now().strftime("%d-%m-%y")
        # Appends crypto, crypto's value in a currency, currency, and today's date in the CSV file
        writer = csv.writer(csv_recap)
        writer.writerow([crypto, f"{data[crypto][currency]: .1f}", currency, today])
        # Gives time to write and closes the file
        time.sleep(2)
        csv_recap.close()