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
cookie = "Enter your cookie here"
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
