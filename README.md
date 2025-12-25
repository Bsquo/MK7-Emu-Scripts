# Emulator scripts for Mario Kart 7

This repository contains emulator scripts to help reverse engineering Mario Kart 7. These scripts have only been tested in Citra, at the moment (specifically `Citra Nightly 2051 | HEAD 4d9eedd (2023-12-09)`)

## Installation
[Install the latest version of Python](https://www.python.org/downloads/).

Then, place the Python scripts from this repository in the scripting directory of the emulator.
For Citra, this is the `nightly-mingw/scripting/` directory in your Citra installation folder (ensure that the scripts are in the same directory as the `citra.py` file).

## Usage
Boot Mario Kart 7 in the emulator, then open a command line tool, and eexecute the scripts as follows:
`python <tool.py> <game_version>`

`<game_version>` is a number that represents the version of Mario Kart 7 that you've opened in the emulator. The valid values are as follows:
```
    "chn_dlp": 0,
    "chn_rev1": 1,
    "eur_dlp": 2,
    "eur_kiosk": 3,
    "eur_rev0": 4,
    "eur_rev0_v11": 5,
    "eur_rev1": 6,
    "eur_rev2": 7,
    "jpn_dlp": 8,
    "jpn_kiosk": 9,
    "jpn_rev0": 10,
    "jpn_rev0_v11": 11,
    "jpn_rev1": 12,
    "jpn_rev2": 13,
    "kor_dlp": 14,
    "kor_rev1": 15,
    "kor_rev2": 16,
    "twn_dlp": 17,
    "twn_rev1": 18,
    "twn_rev2": 19,
    "usa_dlp": 20,
    "usa_kiosk": 21,
    "usa_rev0": 22,
    "usa_rev0_v11": 23,
    "usa_rev1": 24,
    "usa_rev2": 25
```

For example, to run the script `CRaceInfo.py` while playing Mario Kart 7 (USA Rev1, aka USA prepatched v1.1), execute the script in the scripting directory as follows while the game is on:

```python CRaceInfo.py 24``

# Scripts
* `CRaceInfo.py`: Prints global information and parameters for the current race.
* `LapRankChecker.py`: Prints information on your player's "lap rank" checking information, including variables such as the current checkpoint ID, lap completion, etc.

NOTE: `common.py` is a helper script containing code and data used by the scripts above. This script isn't meant to be executed by the user.