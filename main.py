# import os

# for i in range (366):
#     d = str(i) + ' day ago'
#     with open('bot.txt', 'a') as file:
#         file.write(d+'\n')
#     os.system('git add bot.txt')    
#     os.system('git commit --date="'+d+'" -m "hack-commit"')

# os.system('git push -u originm  master')    
import os

## Number of days you want to make commits
for i in range(1,365*2 + 1):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add bot.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')