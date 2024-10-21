# CSCE35103-Photon

## Team 6
| Github Name  | Name |
| ------------- | ------------- |
| CodingGuy1337  | Anthony Johnson  |
| Stepty  | Stephen Ni  |
| WesleySiharath/Yechamo  | Wesley Siharth |
| NathanWojo  | Nathan Wojtowicz  |

# Getting Started
## 1. Install git and tkinter
```
sudo apt-get install git
```

```
sudo apt-get install python3-tk
```
## 2. Fork git repository
```
git clone https://github.com/Stepty/CSCE35103-Photon.git
```

## 3. Open project directory in console
```
cd CSCE35103-Photon
```

## 4. Start virtual environment
```
sudo apt-get install python3-venv
```

```
python3 -m venv photon
```

```
. ./photon/bin/activate
```

## 5. Install dependencies

```
pip install --upgrade pip
```

Run `pip install -r requirements.txt` in root directory to install needed dependencies.

```
pip install -r requirements.txt
```

## 6. Run script to run program (opens two terminals for udp server and client)
```
./script.sh
```

## Altenatively manually run programs

## 1. Open another terminal and reactivate venv (if needed) 
In other terminal, make sure you are in the root directory of the repository to reactivate venv. Then, cd back into src directory.

```
. ./photon/bin/activate
```
## 2. cd into src directory for both terminals
```
cd src
```
## 3. Run Udp Server First
```
python3 python_udpserver.py
```
## 4. Run main.py in other terminal for program
```
python3 main.py
```

# Program Instructions
## Player Entry Screen
To get player name (ie. Opus) from database, input the corresponding player id (ie. 1) into one of the teams and click the submit button for the corresponding team.
To add a new player, input new player id and its codename and click submit.
After putting the player id and codename, user must input the equipment id for the corresponding hardware next to the correct player. Then, user clicks submit, which locks the entry. The user can press F12 or the "Clear Entries" button to clear all locked and unlocked entries. (The user has to click submit multiple times if there are multiple different equipment id connections in order to lock the player to a team).
After correctly submitting atleast 1 player onto each team, the user can press F5 or the "Start Game" button to go to the countdown screen, which leads to the play action screen after reaching 0.

