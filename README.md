# RobloxUncopylockedScraper


This script is checking if Roblox games are uncopylocked and writes the uncopylocked games' information to a text file. The is_uncopylocked function makes an API request to the Roblox games endpoint to get information about a game, given its game ID and a cookie. The function returns True if the game is uncopylocked and False otherwise. In the example usage of the function, the cookie is hardcoded, and the function is run for a range of game IDs, from 7251891812 to 9251891812. If the game is uncopylocked, the game ID and the game information (name, visits, creation date, and last update date) are written to a file called "Allowed.txt." The requests library is used to make the API requests, and the JSON library is used to parse the response JSON.
