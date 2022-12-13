import csv
import os
from pathlib import Path

# This function converts theHarvester email results to txt format
def csv_to_txt():
    csv_file = "EMAILS.csv"
    txt_file = "EMAILS.txt"
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            my_output_file.writelines(my_input_file.readlines()[1:]) # Remove header from output file after csv to txt conversion
        my_output_file.close()
        my_input_file.close()

# This function combines the results from theHarvester and EmailHarvester into one txt file
def all_emails():
    path_to_file1 = 'EMAILS.txt'
    path1 = Path(path_to_file1)
    path_to_file2 = 'results_emailHarvester.txt'
    path2 = Path(path_to_file2)

    if path1.is_file() and path2.is_file(): # If both theHarvester and EmailHarvester produced results
        filenames = ['EMAILS.txt', 'results_emailHarvester.txt']
        with open('All_Emails.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

    elif path1.is_file(): # If only theHarvester produced results
        filenames = ['EMAILS.txt.txt']
        with open('All_Emails.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
    
    elif path2.is_file(): # If only EmailHarvester produced results
        filenames = ['results_emailHarvester.txt']
        with open('All_Emails.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
    
    else: # If neither theHarvester and EmailHarvester produced results
        os.system('clear')
        print("No emails found!")
