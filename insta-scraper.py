import instaloader
import pandas as pd

bot = instaloader.Instaloader()

getUsernames = input('Enter instagram usernames (add a comma between each name): ')

allUsernames = getUsernames.split(',')

# Data arrays
usernames = []
followers = []
followees = []
posts = []

# Excel columns
col1 = 'Username'
col2 = 'Followers'
col3 = 'Followees'
col4 = 'Number of Posts'

for user in allUsernames:
  profile = instaloader.Profile.from_username(bot.context, user.strip())

  usernames.append(profile.username)
  followers.append(profile.followers)
  followees.append(profile.followees)
  posts.append(profile.mediacount)

data = pd.DataFrame({col1: usernames, col2: followers, col3: followees, col4: posts})

fileName = input('Enter a file name for the excel file you wish to output data to (no need to include the .xlsx suffix): ')

sheetName = input('Enter a name of the excel sheet: ')

data.to_excel(f'{fileName}.xlsx', sheet_name=sheetName)
