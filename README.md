# Base `aiogram` bot template

# Setup
- `python3.12`
- `sqlalchemy`
- `psycopg2`
- `logtail-python` for logging in [Better Stack](https://betterstack.com/telemetry)(optional, default for local logs)
- `poetry`


# How to use?
1. Clone repository
```bash
git clone https://github.com/IvanIsak2000/AiogramTemplateBot.git
```

2. Activate `poetry` and install dependencies
```bash
poetry install && poetry shell
```

3. Fill `.env` file by your data
```bash
BOT_KEY=''  # required
LOG_TOKEN=''
MODERATOR_ID=''  # required

POSTGRESQL_HOST=''
POSTGRESQL_PORT=''
POSTGRESQL_USER=''
POSTGRESQL_PASSWORD=''
POSTGRESQL_DBNAME=''
```

4. Change folder
```bash
cd src/
```

5. Add your code!

6. Run bot
```bash
python3 bot.py
```

# How use with database?
1. Fill `.env` file with postgresql data
```bash
BOT_KEY=''  
LOG_TOKEN=''
MODERATOR_ID='' 

POSTGRESQL_HOST=''
POSTGRESQL_PORT=''
POSTGRESQL_USER=''
POSTGRESQL_PASSWORD=''
POSTGRESQL_DBNAME=''
```
2. Uncomment the database initialization in the `bot.py` file
3. Uncomment `models` import in `handlers/__init__.py`
4. Uncomment middleware import in `bot.py` and middleware connect
