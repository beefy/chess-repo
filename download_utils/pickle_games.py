import pickle

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

with open("./data/games.pickle", "wb") as f:
	pickle.dump(games, f)
