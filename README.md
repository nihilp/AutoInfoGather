# AutoInfoGather
A tool to automate OSINT tasks related to emails by combining popular industry favorite tools

---
## Installation

#### Create a folder (if one doesn't exist) where all the tools are going to be stored:

* mkdir tools
* cd tools

#### How to install AutoInfoGather:

* git clone https://github.com/nihilp/AutoInfoGather.git
* cd AutoInfoGather

#### Install requirements:

* pip3 install -r requirements.txt

## Install other repositories needed:

#### Install theHarvester (Only needed if not using Kali Linux):

* git clone https://github.com/laramies/theHarvester 
* cd theHarvester
* pip3 install -r requirements.txt
* pip3 install theHarvester
* sudo python3 setup.py install 

#### Install EmailHarvester:

* git clone https://github.com/maldevel/EmailHarvester

#### Install h8mail:

* git clone https://github.com/khast3x/h8mail.git
* cd h8mail
* pip3 install h8mail
* sudo python3 setup.py install 

---
## Configuring AutoInfoGather:

### In config.py file:

* Change all values to your relative path locations (where everyting is located in your system) 
* If you want to use API keys within theHarvester tool, edit "/etc/theHarvester/api-keys.yaml" file

## Execution - Running AutoInfoGather:

* Navigate to installation folder (ex: if installed under /home/tools, cd /home/tools)
* python3 AutoInfoGather

---
## Usage Screenshots:

#### Running AutoInfoGather in the Kali Linux Terminal:
![Running AutoInfoGather in the Kali Linux Terminal](/Screenshots/001.png?raw=true "Running AutoInfoGather in the Kali Linux Terminal")

#### Main menu of AutoInfoGather:
![Main menu of AutoInfoGather](/Screenshots/002.png?raw=true "Main menu of AutoInfoGather")

#### First option and input of domain “myspace.com”:
![First option and input of domain myspace.com](/Screenshots/003.png?raw=true "First option and input of domain myspace.com")

#### Finished with part 1 message:
![Finished with part 1 message](/Screenshots/004.png?raw=true "Finished with part 1 message")

#### All_Emails.txt file with results obfuscated:
![All_Emails.txt file with results obfuscated](/Screenshots/005.png?raw=true "All_Emails.txt file with results obfuscated")

#### Second option sub-menu:
![Second option sub-menu](/Screenshots/006.png?raw=true "Second option sub-menu")

#### Sub-menu option 1:
![Sub-menu option 1](/Screenshots/007.png?raw=true "Sub-menu option 1")

#### Sub-menu option 1 finished:
![Sub-menu option 1 finished](/Screenshots/008.png?raw=true "Sub-menu option 1 finished")

#### Contents of credentials_found.csv obfuscated – they follow the “username:password” format:
![Contents of credentials_found.csv obfuscated – they follow the “username:password” format](/Screenshots/009.png?raw=true "Contents of credentials_found.csv obfuscated – they follow the “username:password” format")

---
## Tools Included
This project would not be possible without the following tools, so special thanks is due to their creators

* [theHarvester](https://github.com/laramies/theHarvester)
* [emailHarvester](https://github.com/maldevel/EmailHarvester)
* [h8mail](https://github.com/khast3x/h8mail)