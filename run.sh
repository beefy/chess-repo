mkdir -p data
python download_utils/get_latest_date.py
./download_utils/download_games.sh `cat ./data/latest_game_epoch.pickle`
python download_utils/pickle_games.py
python analysis/plot_games.py
