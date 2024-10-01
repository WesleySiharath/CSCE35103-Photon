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

## 6. cd into src directory
```
cd src
```

## 7. Open another terminal and reactivate venv (if needed) 
In other terminal, make sure you are in the root directory of the repository to reactivate venv. Then, cd back into src directory.

## 8. Run Udp Server First
```
python3 python_udpserver.py
```
## 8. Run main.py in other terminal for splash screen and database connection
```
python3 main.py
```

### Altenatively run server.py for just database connection
```
python3 server.py
```


