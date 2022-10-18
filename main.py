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

def mainOptions(choice):
    print('Choice: ', choice)
    match choice:
        case 1:
            print('Wybrano 1')
        case 2:
            print('Wybrano 2')
        case 3:
            exit()
        case _:
            print('Inne')

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

mainPage.print_menu()
choice = int(input('Choice: '))

match Page.activePage:
    #mainPage
    case 0:
        print('Wybrano 0')
        mainOptions(choice)
    #leaderboardsPage
    case 1:
        print('Wybrano 1')
    case 2:
        print('Wybrano 2')
