# Story thread source code generator

Primarily for https://forum.gamer.com.tw/Co.php?bsn=34173&sn=59026.

## To add/edit

1. Head to `res/chara.csv` or `res/dragon.csv`

2. Add entries corresponding to the header in the notes.

## Notes

Element Code

- **`F`** lame

- **`W`** ater

- Wi**`N`** d

- **`L`** ight

- Sha **`D`** ow

-----

Convention of the header for both `res/chara.csv` and `res/dragon.csv`

Name | Element Code | Image URL | Video URL
:---: | :---: | :---: | :---:

-----

Convention of the data order

#### Dragon

Element `F, W, N, L, D`, Max Might `High to Low`

#### Character

Element `F, W, N, L, D`, In-Game Weapon Type Order `(Check the game)`

-----

Below configurations can be found in `data.py`

- Null sentinel image

- Playlist link for both character and dragon stories

-----

Below configurations can be found in `config.py`

- Width of the icon to be rendered
