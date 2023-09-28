import urllib3
import json

# List of players
players = ["wdfsf","BABU_69", "hamidullahnizamani", "Zararnizamani", "muhammadnizamani", "salmannizamani7",
        "UmAr212212", "Alinizamani101", "inamullahniz6", "GUMNAM_69", "sarwan920"]

for player in players:
    print(player)

    # Make an HTTP GET request to the Chess.com API
    url =  f"https://api.chess.com/pub/player/{player}"

    try:
        http = urllib3.PoolManager()
        response = http.request("GET", url)

        if response.status == 200:
            data = json.loads(response.data.decode("utf-8"))

            # Extract rating data
            # rapid_rating = data["chess_rapid"]["last"]["rating"]
            # # bullet_rating = data["chess_bullet"]["last"]["rating"]
            # blitz_rating = data["chess_blitz"]["last"]["rating"]

            # print(f"Rapid Rating for {player}: {rapid_rating}")
            # # print(f"Bullet Rating for {player}: {bullet_rating}")
            # print(f"Blitz Rating for {player}: {blitz_rating}")
            print(data)

            # You can use these rating values to update your HTML elements as needed
        else:
            print(f"Error fetching data. Status code: {response.status}")

    except Exception as error:
        print('Error fetching data:', error)

