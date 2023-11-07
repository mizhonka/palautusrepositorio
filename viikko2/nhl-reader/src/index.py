import requests
from player import Player

def sort_by_points(player):
    return player.points

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    players.sort(key=sort_by_points)

    print("Players from FIN:")

    for player in players:
        if player.nationality=='FIN':
            print(player)

if __name__ == "__main__":
    main()
