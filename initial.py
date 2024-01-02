import os

def generate_settings():
    '''This function asks the user to insert their email and API token.\n

    Then, it stores these data in the `settings.py` file.\n
    
    If the `settings.py`  doesn't exists, it creates it.
    '''
    # Insert user email
    email = input(f"\nPlease, insert your email:\n")
    # Insert user API token
    token = input(f"\nPlease, insert your API token:\n")

    # Current folder
    folder = os.getcwd()

    # File path
    file_path = folder + "/settings/settings.py"

    # Create settings.py file in the settings folder, if doesn't exist
    if os.path.isfile(file_path) == True:
        print(f"\nThe settings.py file already exists.")
    else:
    # Create settings file
        with open(file_path, "w") as settings_file:
            settings_file.write(f'EMAIL = "{email}"\n')
            settings_file.write(f'API_TOKEN = "{token}"\n')
            settings_file.close()
            print(f"\nSuccesfully created your settings file!")
            settings_file.close()

if __name__ == "__main__":
    generate_settings()
