## Instagram User Scraper 

### Prerequisites
- Python3 (https://www.python.org/downloads/)

### Overview
This script allows users to enter a list of instagram usernames and outputs 
their # of followers, # of followees, and # of posts in an excel file. 

Input: 
- The list of usernames inputted must be comma separated (e.g. billeelish, justinbieber, mileycyrus)
- Whether there are spaces between commas or not does not matter 
  (e.g. billieelish,justinbieber and billieelish, justinbieber are both valid)

Output:
The following stats will be outputted into an excel file stored in the root directory of this project:
- Username
- Followers
- Folowees
- Number of Posts

Users can enter a name for the excel file.

### Usage
1. Clone the directory to a location of your choice

  `git clone https://github.com/moraesc/instagram-user-scraper.git`

2. Cd to the root directory of the app

  `cd Desktop/instagram-scraper`
  
3. Run `python3 insta-scraper.py` and follow command line instructions

5. View .xlsx file in project root directory 
