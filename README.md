# chess-repo

The lichess account insights are great but I wanted more customization. This repo downloads my games, keeps an up to date record of them, and plots them. 

- download games from lichess
- download new games since latest game on file
- organize chess pgn format into python dictionary
- plot games with matplotlib

### Dependencies

- linux
- python 2.7
- `pip install matplotlib`
- `pip install numpy`
- `pip install pickle`

### Usage

- update `lichessAccount` param in `download_utils/download_games.sh`
- `chmod u+x download_utils/download_games.sh`
- `chmod u+x download_utils/run.sh`
- `./run.sh`

### ToDo

- moving average or linear regression on rating plot
- subplot of volume of games per week
- tournament analysis / visualizations
- stockfish analysis?
- opening preferences over time
- store game data in mongodb for easier querries
- setup script
  - download requirements
  - prompt for "lichess Account:"
  - set sh files to be executable
- add code comments
- clean up code
