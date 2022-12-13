import pandas as pd
from pathlib import Path
import json
import os

# Converts the json output of theHarvester into different, more easily readable and seperate csv files
def cleanResults():
    # specify path
    p = Path(r'/home/kali/python/Capstone/AutoInfoGather/Results/results_theHarvester.json')

    # read json
    with p.open('r', encoding='utf-8') as f:
        data = json.loads(f.read())

    # create dataframe
    df = pd.json_normalize(data)

    # pandas dataframe object to string
    if "asns" in data:
        asns = df['asns'].astype('string') 
        asns.to_csv('test_asns.csv', index=False, encoding='utf-8')

        # cleaning ASNS results
        s = open('test_asns.csv','r').read()
        chars = ('"',"'",'[',']') 
        for c in chars:
            s = "".join(s.split(c)).replace(', ','\n')
        out_file = open('ASNS.csv','w')
        out_file.write(s)
        out_file.close()

        os.remove("test_asns.csv")

    if "emails" in data:
        emails = df['emails'].astype('string') 
        emails.to_csv('test_emails.csv', index=False, encoding='utf-8')

        # cleaning EMAIL results
        s = open('test_emails.csv','r').read()
        chars = ('"',"'",'[',']') 
        for c in chars:
            s = "".join(s.split(c)).replace(', ','\n')
        out_file = open('EMAILS.csv','w')
        out_file.write(s)
        out_file.close()

        os.remove("test_emails.csv")

    if "hosts" in data:
        hosts = df['hosts'].astype('string')
        hosts.to_csv('test_hosts.csv', index=False, encoding='utf-8') 

        # cleaning HOST results
        s = open('test_hosts.csv','r').read()
        chars = ('"',"'",'[',']') 
        for c in chars:
            s = "".join(s.split(c)).replace(', ','\n')
        out_file = open('HOSTS.csv','w')
        out_file.write(s)
        out_file.close()

        os.remove("test_hosts.csv")
    
    # 
    if "interesting_urls" in data:
        hosts = df['interesting_urls'].astype('string')
        hosts.to_csv('test_interesting_urls.csv', index=False, encoding='utf-8') 

        # cleaning HOST results
        s = open('test_interesting_urls.csv','r').read()
        chars = ('"',"'",'[',']') 
        for c in chars:
            s = "".join(s.split(c)).replace(', ','\n')
        out_file = open('interesting_URLs.csv','w')
        out_file.write(s)
        out_file.close()

        os.remove("test_interesting_urls.csv")

    if "ips" in data:
        ips = df['ips'].astype('string')
        ips.to_csv('test_ips.csv', index=False, encoding='utf-8') 

        # cleaning IP results
        s = open('test_ips.csv','r').read()
        chars = ('"',"'",'[',']') 
        for c in chars:
            s = "".join(s.split(c)).replace(', ','\n')
        out_file = open('IPs.csv','w')
        out_file.write(s)
        out_file.close()

        os.remove("test_ips.csv")
    
    else:
        os.system('clear')
        print("error processing json file")

    

