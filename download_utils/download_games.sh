lichessAccount=beefybeefy
wget --content-disposition https://lichess.org/api/games/user/$lichessAccount?since=$1
mv ./data/games.pgn ./data/games_old.pgn
mv ./*.pgn ./data/games_new.pgn
cat ./data/games_old.pgn ./data/games_new.pgn > ./data/games.pgn
rm ./data/games_old.pgn
rm ./data/games_new.pgn
