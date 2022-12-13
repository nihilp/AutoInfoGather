import re # used for regular expressions
import os # used to delete files
import csv # used for csv conversion


# Function removing special caharacters present in h8mail terminal output

def remove_special_char():
    f = open("raw_h8mail_output.txt")
    o = open("clean_raw_h8mail_output.txt", "w")
    document = f.read() 
    output = re.sub(r'[^ \nA-Za-z0-9/@:.]+', '', document) #Remove special characters
    clean = re.sub(r'(?sm)(0m)','', output) # Remove 0m from end of line
    o.write(clean)
    f.close()
    o.close()

# Function locating credentials found in h8mail output

def find_creds():

    # Put emails into list
    e = open("All_Emails.txt", "r")
    emails = e.read()
    data_into_list = emails.split("\n")
    data_into_list = data_into_list[:-1] # Remove last entry because it is empty
    e.close()

    pattern = r'[0-9A-Za-z.@]+:[0-z]+' # Regex pattern for email:password format of h8mail credentials found
    o = open("credentials_found.txt", "w")
    with open("clean_raw_h8mail_output.txt", "r") as file:
        lst = []
        for line in file:
            match = re.findall(pattern, line) # Find credentials following the aforementioned pattern          
            lst.append(match)
        result = [ele for ele in lst if ele != []] # Remove empty lists
        s = str(result)
        chars = ('"',"'",'[',']') 
        for c in chars:
            s = "".join(s.split(c)).replace(', ','\n') # Clean results
        o.write(str(s))
        o.close()

        # Convert file from txt to csv
        with open("credentials_found.txt", 'r') as infile, open("credentials_found1.csv", 'w') as outfile:
            stripped = (line.strip() for line in infile)
            lines = (line.split(",") for line in stripped if line)
            writer = csv.writer(outfile)
            writer.writerows(lines)

        # Remove duplicates from csv
        with open('credentials_found1.csv', 'r') as in_file, open('credentials_found.csv', 'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)

    # Delete unecessary results
    os.remove("raw_h8mail_output.txt")
    os.remove("clean_raw_h8mail_output.txt")
    os.remove("credentials_found.txt")
    os.remove("credentials_found1.csv")


