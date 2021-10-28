import webbrowser
import os
import git
import urllib.parse
import dateutil
import pyperclip

def dateConv(date):
    #convert DDMMYYYY to "Month Date, Year" e.g.: "January 01, 2021"
    date = (date)
    day = (date[:2])
    month = (date[2:4])
    year = (date[4:])

    months = {'01':'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'}
    
    export = "{0} {1}, {2}".format(months[month], day, year)
    return export

# def getText():
#     # Get input text
#     day = input("Enter Day Number: ")

#     date = input("\nEnter Date (DDMMYYYY): ")
#     if (len(str(date))!=8):
#         return print("Enter Valid Date!")
#     date = dateConv(date)
    
#     progress = input("\nEnter Progress: ")
    
#     thoughts = input("\nEnter Thoughts/Comments: ")
    
#     link = input("\nEnter Link: ")
#     if link=="":
#         link="N/A"
    
#     return day, dateConv(date), progress, thoughts, link

def getText():
    # Get text input
    # Implement character counter for tweets
    # Make decent UI
    
    # return day, dateConv(date), progress, thoughts, link

def txtGen():
    tweet_txt = """#100DaysOfCode
    🗓 DAY REPLACE_day of 100: REPLACE_date

    ✔ Progress: REPLACE_

    🧠 Thoughts:

    🔗 Link: N/A"""

    git_txt = """## DAY REPLACE_day: REPLACE_date

    **Today's Progress**: REPLACE_prog

    **Thoughts**: REPLACE_thoughts

    **Link to work**: REPLACE_links"""

def tweet(tweet_txt):
    txt = urllib.parse.quote(txt)
    pre="https://twitter.com/intent/tweet?text="
    webbrowser.open(twt)

# tweet_txt, git_txt= getText()
# tweet(tweet_txt)
# pyperclip.copy(git_txt)
# print("\nCopied Git Text to Clipboard!")

datevar = input("Enter Date to Parse: ")
print(dateConv(datevar))