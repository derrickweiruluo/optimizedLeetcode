import collections, os
import pandas as pd
import re

path = 'senderFolderPath'

# Change the directory
os.chdir(path)
  
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return(str(f), f.read())
  

wordsList = []
suspiciousWords = set(wordsList)
pattern = re.compile(r'^A1.8301$')

wordSet = collections.defaultdict(set)
wordCounter = collections.defaultdict(list)
suspiciousWordsCounter = collections.defaultdict(set)

# iterate through all file
# Assuming email data has been parsed into
# sender1.txt, containing list of receivers and content of each
# email sent by sender1


for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        sender, curSenderFile = read_text_file(file_path)
        for word in curSenderFile.split():
            word = pattern.match(word)
            if word in suspiciousWords:
                wordSet[sender].add(word)
                wordCounter[sender].append(word)
                suspiciousWordsCounter[word].add(sender)


symbols = '!@#$%^&*|\??><~_+'

curSenderFile.strip(symbols).split()



## Assuming email data has been parsed into
## sender1.txt, containing list of receivers and content of each
## email sent by sender1


