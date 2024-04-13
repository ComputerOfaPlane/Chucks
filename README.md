# 🏏Chucks 🦆

Chucks is a simple hand cricket game we(me & my friends) used to play while commuting back from school. It required 10 different hand gestures to make runs and bowl. There were two teams, one would bowl the other would bat. The game was divided into two innings. Just like the original cricket game.

There are two modes :-

1. Simple
2. Crazy
#### General Rules:-
Numbers in the range ```0-10``` are allowed, both inclusive.
#### Rules for Simple Mode:-
If the baller and batter plays the same number, the batter is declared as OUT
#### Rules for Crazy Mode:-
If the batter and baller plays the same number, the batting team can add runs to their existing score which will be equal to ```existing_score + (batter_move**2)```. In order to OUT the batsmen, baller will need to play moves such that ```abs(batter_move-baller_move)==1```. In case of ```(0,10) or (10,0)``` from either side, batter will be given OUT. In case both batter and baller chooses move ```0```, batting team will add 200 runs.


## Installation
```bash
git clone https://github.com/ComputerOfaPlane/Chucks.git
```

## Usage
make sure to note the directory, you cloned the repository into
```bash
cd Chucks
python3 bot.py
```

## Contributing
If you encounter any bug, please report it into Issues of the repository.
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

##### *Future:* will add a GUI and make it multiplayer (for the bois)