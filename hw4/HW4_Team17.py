
"""
Write a program to open the file WorldSeriesWinners.txt,
read it line by line and store the team names in a dictionary [10 points].
Specifically, create a dictionary in which keys are the team names (e.g., Chicago White Sox’) and values
are a list of the wining years (e.g., [1906, 1917, 2005]) [10 points].
The year information is not available in the text file but you should be
able to create it based on the year information given above [10 points].
Don’t hardcode the values, but compute them on the fly.
"""


def wining_years(input_file):
    wining_dict = {}
    year = 1903
    for each_line in input_file:
        each_team = each_line.rstrip("\n")  # remove \n in each team
        if year == 1904 or year == 1994:  # we want to avoid 1904 and 1994
            year += 1
        if each_team not in wining_dict:  # if team name is not in the dictionary, create a new one with year
            wining_dict.update({each_team: [year]})
        else:
            wining_dict[each_team].append(year)  # if team name already exist, add new year number to the key
        year += 1

    print("\nDisplay the teams in the alphabetical order with years in brackets: \n")
    for i in sorted(wining_dict.keys()):
        print(i, ":", wining_dict[i])

    return wining_dict


def wins_per_team(wining_years_dict):
    wins = {}

    for key, value in wining_years_dict.items():
        wins.update({key: len(value)})
    print("Display the wins per team: \n")
    print("Teams:\t\t\tTotal Wins")
    for i in sorted(wins):
        print(i, ":", wins[i])
    print("=======================================\n")

    return wins


def bar_graph(wins_dict):
    bars = {}
    print("Sort the data by the number of wins and create a bar graph of the data: \n")

    for each_team in wins_dict:
        bars.update({each_team: int(wins_dict[each_team])})  # append each key and value to bars dictionary
    sorted_bars = sorted(bars.items(), key=lambda x: x[1], reverse=True)  # sort by value and reverse
    for each in sorted_bars:
        print("%s(%s)" % (each[0], each[1]), ":", "*" * each[1])

    return sorted_bars


def main():
    input_file = open(r"C:/Users/yingy/Desktop/52 python/hw4/WorldSeriesWinners.txt","r")
    wining_years_dict = {}
    wins_dict = {}
    wining_years_dict.update(wining_years(input_file))
    print("=======================================\n")

    wins_dict.update(wins_per_team(wining_years_dict))
    bar_graph(wins_dict)


if __name__ == '__main__':
    main()


