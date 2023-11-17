import os
import csv
import time
import datetime


def new_csv():
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
            # Write headers
            writer = csv.DictWriter(recap_file, fieldnames=["crypto", "value", "currency", "data"])
            writer.writeheader()
            # Give time to write before closing
            time.sleep(2)
            recap_file.close()

def write_data(crypto:str, data:str, currency:str)->None:
    # Current folder
    folder = os.getcwd()

    # File path
    file_path = folder + "/data_recap/recap.csv"
    
    with open(file_path, "a") as csv_recap:
        today = datetime.datetime.now().strftime("%d-%m-%y")
        writer = csv.writer(csv_recap)
        writer.writerow([crypto, f"{data[crypto][currency]: .1f}", [currency], today])
        time.sleep(2)
        csv_recap.close()