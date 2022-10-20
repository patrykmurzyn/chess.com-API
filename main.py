import os
from tokenize import String
import requests
import datetime
import json
from os import listdir
from os.path import isfile, join

class Page:
    activePage = 0

    def __init__(self, title, menu):
        self.title = title
        self.menu = menu

    def print_menu(self):
        os.system('cls')
        print(self.title)
        for key in self.menu.keys():
            print(key, '-', self.menu[key])

        print('')

title = 'Chess.com API'
menu = {
    1: 'Search',
    2: 'Leaderboards',
    3: 'Exit',
}

mainPage = Page(title, menu)

title = 'Leaderboards:'
menu = {
    1: 'Daily',
    2: 'Daily960',
    3: 'Rapid',
    4: 'Blitz',
    5: 'Bullet',
    6: 'Bughouse',
    7: 'Blitz960',
    8: 'Threecheck',
    9: 'Crazyhouse',
    10: 'Kingofthehill',
    11: 'Tactics',
    12: 'Save data',
    13: 'Open data',
    14: 'Back',
}

leaderboardsPage = Page(title, menu)

def mainOptions(choice):
    match choice:
        case 1:
            print('Wybrano 1')
        case 2:
            leaderboardsPage.print_menu()
            response = requests.get("https://api.chess.com/pub/leaderboards").json()
            choice = int(input('Choice: '))
            os.system('cls')
            leaderboardsOptions(choice, response)
        case 3:
            exit()
        case _:
            print('Inne')

def leaderboardsOptions(choice, response):

    if choice >=3 and choice <=10:
        for i in reversed(range(50)):
            print(i+1, '-', response['live_' + (leaderboardsPage.menu[choice]).lower()][i]['username'], '-', response['live_' + (leaderboardsPage.menu[choice]).lower()][i]['score'], '-', response['live_' + (leaderboardsPage.menu[choice].lower())][i]['url'])
        input('Click any key to go back')
        leaderboardsPage.print_menu()
        choice = int(input('Choice: '))
        os.system('cls')
        leaderboardsOptions(choice, response)
    elif choice >= 1 and choice <=11:
        for i in reversed(range(50)):
            print(i+1, '-', response[(leaderboardsPage.menu[choice]).lower()][i]['username'], '-', response[(leaderboardsPage.menu[choice]).lower()][i]['score'], '-', response[(leaderboardsPage.menu[choice].lower())][i]['url'])
        input('Click any key to go back')
        leaderboardsPage.print_menu()
        choice = int(input('Choice: '))
        os.system('cls')
        leaderboardsOptions(choice, response)
    elif choice == 12:
        filePath = './Saved/' + str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day) + '-' + str(datetime.datetime.now().hour) + '-' + str(datetime.datetime.now().minute) + '.json'
        file = open(str(filePath), "w")
        file.write(json.dumps(response))
        file.close()
        input("File saved: " + filePath)
        os.system('cls')
        mainPage.print_menu()
        choice = int(input('Choice: '))
        mainOptions(choice)
    elif choice == 13:
        f = []
        mypath = './Saved/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        if len(onlyfiles) == 0 :
            print('No files')
        else:
            print('Chose File: ')
            for i in range(len(onlyfiles)):
                print(i + 1, '- ' + onlyfiles[i])
            choiceResponse = int(input('Choice: '))
            file = open('./Saved/' + onlyfiles[choiceResponse - 1])
            dataResponse = json.load(file)
            file.close()
            leaderboardsPage.print_menu()
            choice = int(input('Choice: '))
            os.system('cls')
            leaderboardsOptions(choice, dataResponse)
            input('Click any key to go back')
    elif choice == 14:
        mainPage.print_menu()
        choice = int(input('Choice: '))
        mainOptions(choice)


#---------------------------------------------

mainPage.print_menu()

match Page.activePage:
    #mainPage
    case 0:
        choice = int(input('Choice: '))
        mainOptions(choice)
    #leaderboardsPage
    case 1:
        print('Wybrano 1')
    case 2:
        print('Wybrano 2')
