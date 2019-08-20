from bs4 import BeautifulSoup
import requests
import csv

url_list = ["https://en.wikipedia.org/wiki/List_of_PC_games",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(B)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(C)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(D)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(E)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(F)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(G)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(H)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(I)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(J)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(K)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(L)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(M)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(N)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(O)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(P)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(Q)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(R)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(S)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(T)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(U)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(V)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(W)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(X)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(Y)",
            "https://en.wikipedia.org/wiki/List_of_PC_games_(Z)",
            ]

csvfile = "output/game_data.csv"

myData = [["Game", "Month", "Day", "Year"]]

for url in url_list:
    page = requests.get(url)

    # Find first table on the page
    soup = BeautifulSoup(page.content, 'html.parser')
    temp = soup.find('div', class_="mw-parser-output")
    table = temp.findAll('table')[0]
    rows = table.find('tbody').findAll('tr')

    count = 1
    data_list = []

    # For each row in table, find name/month/day/year
    for tr in rows:
        try:
            table_body = table.findAll('tr')[count]
        except IndexError:
            continue

        try:
            game = table_body.findAll('i')[0]
        except IndexError:
            pass

        try:
            date = table_body.findAll('td')[5].findAll('span')[0]
        except IndexError:
            pass

        try:
            month, day, year = date.text.split(' ')
        except ValueError:
            pass

        try:
            data_list = [game.string, month, day[:-1], year]
        except AttributeError:
            pass

        myData.append(data_list)
        count += 1

    myFile = open(csvfile, 'w')
    with myFile:
        write = csv.writer(myFile)
        for game in myData:
            write.writerow(game)