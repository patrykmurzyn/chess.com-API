import os
from turtle import title
import requests

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
    11: 'Lessons',
    12: 'Tactics',
    13: 'Back',
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
        for i in range(50):
            print(i+1, '-', response['live_' + (leaderboardsPage.menu[choice]).lower()][i]['username'], '-', response['live_' + (leaderboardsPage.menu[choice]).lower()][i]['score'], '-', response['live_' + (leaderboardsPage.menu[choice].lower())][i]['url'])
    else:
        for i in range(50):
            print(i+1, '-', response[(leaderboardsPage.menu[choice]).lower()][i]['username'], '-', response[(leaderboardsPage.menu[choice]).lower()][i]['score'], '-', response[(leaderboardsPage.menu[choice].lower())][i]['url'])
    
    


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
