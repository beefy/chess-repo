import pickle
from datetime import datetime

fin = "./data/games.pgn"
fout = "./data/games.pickle"

games = []
rec= {}
keys = [
	"[Event ","[Site ","[Date ","[Round ","[White ","[Black ",
	"[Result ","[UTCDate ","[UTCTime ","[WhiteElo ","[BlackElo ",
	"[Variant ","[TimeControl ","[ECO ","[Termination ",
	"[WhiteRatingDiff ","[BlackRatingDiff "
]

# parse pgn data into dict
parse = lambda key, line: line.replace(key,"").replace('"',"").replace("]","").replace("\n","")
for line in open(fin,"rb"):
	for key in keys:
		if key in line:
			rec[key.replace("[","").replace(" ","")] = parse(key,line)
	if not any([key in line for key in keys]) and len(rec.keys()) > 0:
		games.append(rec)
		rec = {}

has_key = lambda key: key in game.keys()
has_keys = lambda keys: all([has_key(key) for key in keys])
for game in games:
	if has_keys(["UTCDate","UTCTime","White","Black","WhiteElo","BlackElo","Event"]):
		date_str = game["UTCDate"] + " " + game["UTCTime"]
		date = datetime.strptime(date_str,'%Y.%m.%d %H:%M:%S')
		game["Datetime"] = date
	else:
		game["Datetime"] = datetime.now()

ret = sorted(games, key=lambda k:k["Datetime"])
with open("./data/games.pickle", "wb") as f:
	pickle.dump(ret, f)
