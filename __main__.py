#!/bin/python3

"""
A tool to automate OSINT tasks related to emails by combining popular industry favorite tools.
Find emails -> search local database for results

GitHub repository: https://github.com/nihilp/AutoInfoGather

Note:
------- 
If you see the error "/home/kali/python/Capstone/AutoInfoGather/__main__.py" is overriding the stdlib module "__main__"PylancereportShadowedImports
while examining __main__.py in VS Code, it is because of pylance version "v2022.11.40", and it is a false possitive and does not influence usage or execution
https://pullanswer.com/questions/reportshadowedimports-triggers-on-__main 
"""

__author__ = "nihilp"
__copyright__ = "Copyright (c) 2022 @nihilp"
__credits__ = ["nihilp", "maldevel", "Christian Martorella", "khast3x"]
__licence__ = "MIT"
__version__ = "v1"
__maintainer__ = "nihilp"

import os
import sys
import getch 
import config # Contains all user defined paths
from Tools.tools import * # Contains all tools used
from Utilities.combine_results import * # Used to combine theHarvester & EmailHarvester results
from Utilities.json_to_csv import * # Used to convert theHarvester json output to multiple csv files
from Utilities.filter_h8mail import * # Contains tools that process h8mail terminal output

# Function for waiting for key press
def wait():
    getch.getche()

# Function for clearing Linux terminal
def clear():
    os.system('clear') 

def main():
    ans=True
    while ans:
        print("""
        AutoInfoGather:
        ---------------

        1. Collect information related to a specific domain 
        2. Check if emails found are present in local databreach
        3. Exit/Quit
        """)
        ans=input("What would you like to do? ")

        if ans=="1": # Target lookup by domain   
            arg=True
            while arg:
                arg=input("Please type a domain (ex: nihilp.com): ")
                print("\nGetting information on domain... (this may take a while)")
                os.chdir(config.path_to_results_file) # Change working directory to Results file
                theHarvester(arg) # Run theHarvester tool using user defined domain
                cleanResults() # Convert the json output of theHarvester into different, more easily readable and seperate csv files
                emailHarvester(arg)
                if os.path.exists("Results/EMAILS.csv"): # Check if theHarvester found emails
                    csv_to_txt() # Convert theHarvester emails to txt
                all_emails() # Combine the results from theHarvester and EmailHarvester into one txt file
                clear() 
                print("\nFinished, view results under Results/All_Emails.txt file")
                arg=False # Go back to main menu
                
        elif ans=="2": # Looking for matches in local database 
            clear()
            os.chdir(config.path_to_results_file)
            choice=True
            while choice:
                
                print("""
                    1. Default - Use results of part 1 
                    2. Define target for local breach search
                    3. Go back
                    """)

                choice=input("What would you like to do? ")
                
                if choice=="1":     
                    clear()              
                    print("\nSearching if emails are present in local breach using results from part 1... (this may take a while depending on how large the local breach is)")
                    if os.path.exists("All_Emails.txt"):
                            h8mail() # Run h8mail tool using results from part 1
                            remove_special_char() # Remove special caharacters present in h8mail terminal output
                            find_creds() # Locate credentials found in h8mail output
                            print("\nFinished, view results under /Results/credentials_found.csv file")
                            choice=False
                    else: 
                        print("\nNo credentials found in local breach using results from part 1")
                
                elif choice=="2":
                    clear()
                    arg=True
                    while arg:
                        clear()
                        arg=input("\nPlease specify a target email or file containing emails (.txt or .csv) \n(ex: nihilp@test.com or /home/kali/python/Capstone/AutoInfoGather/Results/All_Emails.txt) \nor press enter to go back: ")  
                        
                        path_pattern = re.compile(r"^((?:~?\/)|(?:(?:\\\\\?\\)?[a-zA-Z]+\:))(?:\/?(.*))?$") # Regural expression for paths
                        email_pattern = re.compile(r"^[\w.-]+@[\w.-]+\.\w+$") # Regural expression for emails

                        if (path_pattern.match(arg) and arg.endswith(".txt")) or (path_pattern.match(arg) and arg.endswith(".csv")): # Check if user defined file is txt or csv
                            if os.path.isfile(arg):
                                clear()
                                print("\nSearching if emails are present in local breach using specified file... (this may take a while depending on how large the local breach is)")
                                h8mail_user_input(arg) # Run h8mail tool using user defined file containing emails
                                with open(arg,'r') as firstfile, open('All_Emails.txt','a') as secondfile:
                                    for line in firstfile:
                                        secondfile.write(line)
                                remove_special_char()
                                find_creds()
                                choice=False

                        elif email_pattern.match(arg): # Check if user defined an email
                            clear()
                            print("\nSearching if emails are present in local breach using specified email... (this may take a while depending on how large the local breach is)")
                            email_file = open("All_Emails.txt", "w")
                            email_file.write(arg)
                            email_file.close()
                            h8mail_user_input(arg) # Run h8mail tool using user defined email
                            remove_special_char()
                            find_creds()
                            choice=False

                        else:
                            clear()
                            print("\nInput does not match existing file nor email ")
                            choice=False

                elif choice=="3":
                    clear()
                    choice=False # go back to main menu

                else:
                    clear()
                    print("\nNot a valid choice, try again")
                    choice = True # go back to 2nd menu
                    
        elif ans=="3":
            clear()
            print("\nThank you for using AutoInfoGather!")
            ans = None # go back to main menu

        else:
            clear()
            print("\nNot a valid choice, try again")
            ans = True # go back to main menu

clear() # Clear screen before showing menu

# Check whether python version is greater than 3.10
if sys.version_info.major < 3 or sys.version_info.minor < 10:
    print('Make sure you have Python 3.10+ installed, quitting script.')
    sys.exit(1)

# Enable execution of the tool from parent folder in terminal (ex: python3 AutoInfoGather)
if __name__ == '__main__':
    main()
