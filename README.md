## Instagram User Scraper 

### Prerequisites
- Python3 (https://www.python.org/downloads/)
- Pip3
  - Once python is installed run the following command in your terminal:
    `python -m ensurepip`

### Overview
This script takes in an Excel file with a list of Instgram user names and links to their accounts, scrapes their account data, and outputs an Excel file with a list of each users number of followers, number of followees, and number of posts. 

Users can enter a name for the excel file.

### Usage
1. Clone the directory to a location of your choice. Run the following command in your terminal:

  `git clone https://github.com/moraesc/instagram-user-scraper.git`
  
2. Cd to the root directory of the app. Run the following command in your terminal:

  `cd Desktop/instagram-scraper`
  
3. Install dependencies. Run the following command in your terminal:

  `pip3 install -r requirements.txt`
  
4. Drag an Excel file with the list of names and links to users instagram accounts into the directory

  The Excel file should have all users names in the first column and all links in the second column. Both columns should have a header (wording of the header does not matter)
  
  Download a sample file here:
  
  [SampleFile.xlsx](https://github.com/moraesc/instagram-user-scraper/files/10333890/SampleFile.xlsx)

  
5. Run `python3 insta-scraper.py` and follow the command line instructions

6. The following stats will be outputted into a .xlsx file stored in the projects root directory:
  - Username
  - Followers
  - Folowees
  - Number of Posts

