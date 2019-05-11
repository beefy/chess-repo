import matplotlib.pyplot as plt
import datetime
import numpy as np
from datetime import datetime
import pickle

with open("./data/games.pickle", "rb") as f:
	games = pickle.load(f)

has_key = lambda key: key in game.keys()
has_keys = lambda keys: all([has_key(key) for key in keys])
# rating by date and variant
ret = {}
plots = {}
for game in games:
	if has_keys(["UTCDate","UTCTime","White","Black","WhiteElo","BlackElo","Event"]):
		if "Rated" in game["Event"] and "tournament" not in game["Event"]:
			if game["Event"] not in ret.keys():
				ret[game["Event"]] = {}
				plots[game["Event"]] = {"x":[],"y":[]}

			date_str = game["UTCDate"] + " " + game["UTCTime"]
			date = datetime.strptime(date_str,'%Y.%m.%d %H:%M:%S')

			if game["White"] == "beefybeefy":
				ret[game["Event"]][date] = game["WhiteElo"]
			else:
				ret[game["Event"]][date] = game["BlackElo"]

			# if date > datetime(2018,10,01,0,0) and date < datetime(2018,11,01):
			plots[game["Event"]]["x"].append(date)
			plots[game["Event"]]["y"].append(ret[game["Event"]][date])

for variant in plots.keys():
	x = np.array(plots[variant]["x"])
	y = np.array(plots[variant]["y"])

	ultrabullet = "UltraBullet" in variant
	bullet = "Bullet" in variant and not ultrabullet
	blitz = "Blitz" in variant
	rapid = "Rapid" in variant
	classical = "Classical" in variant
	correspondence = "Correspondence" in variant

	horde = "Horde" in variant
	crazyhouse = "Crazyhouse" in variant

	if any([bullet,blitz,rapid,classical]):
	    print str(variant).replace("game","")+", "+str(len(plots[variant]["x"]))+" games"
	    plt.plot(x,y)
	else:
		plots.pop(variant)

# add legend
legend = [key.replace("Rated ","").replace(" game","") for key in plots.keys()]
plt.legend(legend,loc="upper left")
# add grid lines
ax = plt.axes()
ax.yaxis.grid()
ax.xaxis.grid()
# size window
plt.gcf().set_size_inches(20, 10, forward=True)
plt.show()
