import requests
import json

#Written by Robin

# Function to check if a game is uncopylocked
def is_uncopylocked(game_id, cookie):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Cookie": cookie
    }

    # Make a request to the API to get game info
    response = requests.get(f'https://games.roblox.com/v1/games/{game_id}/settings', headers=headers)

    # If the request fails, return False
    if response.status_code != 200:
        print(f"[ERROR] Failed to get game info: {response.text}")
        return False

    # Get the response JSON
    response_json = response.json()

    # Check if the game is uncopylocked
    is_copyable = response_json.get("IsCopyable", False)
    if is_copyable:
        print(f"[SUCCESS] Game {game_id} is uncopylocked")
        return True
    else:
        print(f"[ERROR] Game {game_id} is not uncopylocked")
        return False

# Example usage of the function
cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_91E4CFDFC956E5329EB72CDABAEB7FFEA442B2395EB05E413700950694C8884BEE89040DFF569F0F08741F099DC8760F64823F9F9787AFB25A3241EF68602A309066DBDEF11DB7597763E803753CE39A1C0B91C113398417643436E006AB2B3D0B2704BC26C19AB22F74B554F6544E2CBB479DAD4C849B57ABCB517A43B596211B09892A8AE0EFF672E70FB7D63EA2104B684282B22CCB4FA6AD1DB325517F0BE82B1A6D2FDC12AC255EE303D36617A7DCEAEE45751A44B0C88205216E727D559EBE05C88240755472687E804A389B2757D7E796AF7D5A51C2F1767918F9ADA173F9D29241FEB22C5AA5238163ED57D872B74ED03C131D57D563D48F7662D0A74FE5BD74254BA9D895E99BEED0D538B244E255A48FF2F988411E92456A25666A89F5FF9391CE71C71128ABB0C9E7BE775ADC83F1C072195342C57FD1AF3B6DB4D22B502EB4BB5AD70810F8E93018383E019CE09BAD9633801A8D9AAB746FE529C35E897C574108FFD6A56BCDE136D29FE3F0C7FA9A8D0FC4DA7EFD344904B01DCE127258"
for game_id in range(7251891812, 9251891812):
    if is_uncopylocked(game_id, cookie):
        # Write to "Allowed" file
        with open("Allowed.txt", "a") as file:
            file.write(f"{game_id}\n")
            print(f"[SUCCESS] Wrote game id {game_id} to Allowed.txt")

            # Write game information to file
            game_info = requests.get(f"https://games.roblox.com/v1/games/{game_id}", headers=headers).json()
            file.write(f"Name: {game_info['name']}\n")
            file.write(f"Visits: {game_info['visits']}\n")
            file.write(f"Created: {game_info['created']}\n")
            file.write(f"Last Updated: {game_info['lastUpdated']}\n")
            print(f"[SUCCESS] Wrote game information for game id {game_id} to Allowed.txt")
