## Instagram User Scraper 

### Prerequisites
- Python3 (https://www.python.org/downloads/)
- Pip3
  - Once python is installed run the following command in your terminal:
    `python3 -m ensurepip`

### Overview
This script takes in an Excel file with a list of Instgram user names and links to their accounts, scrapes their account data, and outputs an Excel file with a list of each users name, username, link to their profile, and number of followers. 

Users can enter a name for the excel file.

### Usage
1. Clone the directory to a location of your choice. Run the following command in your terminal:

  `git clone https://github.com/moraesc/instagram-user-scraper.git`
  
2. Cd to the root directory of the app. Run the following command in your terminal:

  `cd <PATH_TO_DIRECTORY>/instagram-user-scraper`
  
3. Drag an Excel file with the list of names and links to users instagram accounts into the directory

  The Excel file should have all users names in the first column and all links in the second column. Both columns should have a header (wording of the header does not matter)
  
  Download a sample file here (file is included in repository as well):
  
  [SampleFile.xlsx](https://github.com/moraesc/instagram-user-scraper/files/10333890/SampleFile.xlsx)

  
4. Run `python3 scraper.py` and follow the command line instructions

5. The following stats will be outputted into a .xlsx file stored in the projects root directory:
  - Name
  - Username
  - Profile URL
  - Follower Count
  
  Sample output file:
  
  [SampleFileWithFollowersData.xlsx](https://github.com/moraesc/instagram-user-scraper/files/10348872/SampleFileWithFollowersData.xlsx)
