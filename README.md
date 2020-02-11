# Simple Russian game "Durak"
## Support mode:
    - Player VS Bot
## Translations:
    - English
    - Russian
    - Other (can be extended)
## Require:
    - Python 3+ version
    - Colorama (python package, for colored console output)
## How to run a game
1. Install depedency -> pip install colorama
2. Run script -> python durak.py
## Hot to run in docker
1. Build image from Docker file `docker build . -t durak:v1`
2. Create container from *durak* image `docker create --name durak -it durak:v1`
3. Start container *durak* `docker start durak -i`
