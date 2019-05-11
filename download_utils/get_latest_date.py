"""get the date of the latest game and save it to a file"""
import pickle
from datetime import datetime

with open("./data/games.pickle", "rb") as f:
	games = pickle.load(f)

date_arr = []
has_key = lambda key: key in game.keys()
has_keys = lambda keys: all([has_key(key) for key in keys])
for game in games:
	if has_keys(["UTCDate","UTCTime","White","Black","WhiteElo","BlackElo","Event"]):
		date_str = game["UTCDate"] + " " + game["UTCTime"]
		date = datetime.strptime(date_str,'%Y.%m.%d %H:%M:%S')
        date_arr.append(date)

min_date = min(date_arr)
min_date_epoch = min_date.strftime("%s")

max_date = max(date_arr)
max_date_epoch = max_date.strftime("%s")

print "data from " + str(min_date) + ", " + str(min_date_epoch)
print "data to " + str(max_date) + ", " + str(max_date_epoch)

with open("./data/latest_game_epoch.pickle", "wb") as f:
    f.write(str(int(str(max_date_epoch))*1000))
