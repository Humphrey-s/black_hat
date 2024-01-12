#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


def epl_table():
    """returns a dictionary representation of the epl table"""

    r = requests.get("https://www.premierleague.com/tables")

    if r.status_code == 200:
        print("Successful...\nhere goes the results ")

        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title.text)
        table_headers = soup.find('thead')

        column = []

        for word in table_headers.find_all('tr'):

            header = word.find('th', class_ = 'league-table__team-header')
            column.append(header.text)

            for i in  word.find_all('div', class_ = 'league-table__thShort thShort'):
                column.append(i.text)

        team = soup.find('tbody')

        club_names = []
        i = 1
        table = {}

        for rows in team.find_all('tr', attrs={'data-filtered-entry-size':'20'}):

            club = rows.get('data-filtered-table-row-name')
            table_dic_t = {}

            if club is not None:
                team_dic_t = {}

                club_names.append(club)

                details = rows.find_all('td')

                team_dic_t["Pl"] = details[2].text
                team_dic_t["W"] = details[3].text
                team_dic_t["D"] = details[4].text
                team_dic_t["L"] = details[5].text
                team_dic_t["GD"] = str(int(details[8].text))
                team_dic_t["Pts"] = details[9].text
                table_dic_t[club] = team_dic_t

                table[i] = table_dic_t

                i = i + 1
        print(table)
    else:
        print("fatal")

if __name__ == "__main__":
    epl_table()
