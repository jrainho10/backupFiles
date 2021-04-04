# backupFiles

backupFiles is a small python script that compresses every file in given directory and saves it to a remote server.
It's pretty rudementary, but it does it's job, I am planning to improve this small code as I get more familiar with Python and Git.

## Usage

Currently, the script just compresses everything in a given path `$HOME/backup`.
This means everything you want to be saved need to be moved over that path.
```
python3 backupFiles.py
```

The settings placed in the script are for my particular **EC2 Instance** in AWS, however, feel free to modify to any specific scenario.

## Roadmap

- Add checks in the code for path locations
- Add functions to make the code cleaner
- Add feature to compress multiple paths

## Project Status

**Ongoing**