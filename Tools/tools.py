import subprocess # used to excecute external processes 
import config # import config.py variables

# Function calling theHarvester
def theHarvester(domain):
    subprocess.run([config.path_to_theHarvester, '-b', "all", '-d', domain, "-f", config.results_theHarvester],
                capture_output=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)

# Function calling theHarvester
def emailHarvester(domain):
    subprocess.run(['python3', config.path_to_emailHarvester, '-d', domain, '-s', config.results_emailHarvester],
                capture_output=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)

# Function calling h8mail
def h8mail():
    f = open(config.raw_h8mail_output, "w")
    subprocess.run([config.path_to_h8mail, '-t', config.results_All_Emails, '-lb', config.path_to_local_breach],
                capture_output=False,
                stdout=f,
                stderr=subprocess.STDOUT)

# Function calling h8mail with user input
def h8mail_user_input(target):
    f = open(config.raw_h8mail_output, "w")
    subprocess.run([config.path_to_h8mail, '-t', target, '-lb', config.path_to_local_breach],
                capture_output=True,
                stdout=f,
                stderr=subprocess.STDOUT)
