import os
from tokenize import String
import requests
import datetime
import json
from os import listdir
from os.path import isfile, join
from datetime import datetime, timedelta


class Page:
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
            os.system('cls')
            print('Find a player by nickname')
            nickname = input('Enter nickname: ')
            response = requests.get("https://api.chess.com/pub/player/" + nickname).json()
            responseStats = requests.get("https://api.chess.com/pub/player/" + nickname + "/stats").json()
            try:
                country = (requests.get(response['country']).json())['name']
            except KeyError:
                input('Can not find user!')
                mainOptions(1)
            dt = datetime.fromtimestamp(response['joined']).strftime("%Y-%m-%d, %H:%M")  # type: ignore
            os.system('cls')
            print('User info: \nName: ', response['name'], '\nCountry: ', country, '\nNickname: ', response['username'], '\nPlayer id: ', response['player_id'], '\nStatus: ', response['status'], '\nJoined: ', dt , '\nFollowers: ', response['followers'])
            print('\nStats:\nRapid: ', responseStats['chess_rapid']['last']['rating'], '\nBlitz: ', responseStats['chess_blitz']['last']['rating'], '\nBullet: ', responseStats['chess_bullet']['last']['rating'], '\nTactics: ', responseStats['tactics']['highest']['rating'])
            input()
            mainPage.print_menu()
            choice = int(input('Choice: '))
            mainOptions(choice)
        case 2:
            leaderboardsPage.print_menu()
            response = requests.get("https://api.chess.com/pub/leaderboards").json()
            choice = int(input('Choice: '))
            os.system('cls')
            leaderboardsOptions(choice, response)
        case 3:
            exit()

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
        filePath = './Saved/' + str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day) + '-' + str(datetime.now().hour) + '-' + str(datetime.now().minute) + '.json'
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
choice = int(input('Choice: '))
mainOptions(choice)
