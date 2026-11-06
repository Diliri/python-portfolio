# Python Портфоліо

Збірник навчальних вправ з Python, курсових проєктів та Telegram-бот для перегляду розкладу. Цей репозиторій демонструє процес навчання: від основ Python до об'єктно-орієнтованого програмування, обробки помилок і створення невеликого застосунку, який отримує розклад із Google Tables (Google Sheets).

> **Статус проєкту:** Навчальне портфоліо. Більшість файлів є автономними вправами, а не модулями єдиної програми. Деякі скрипти навмисно зроблені демонстраційними, інтерактивними або незавершеними.

## Структура репозиторію

```text
python-portfolio-main/
├── learning/
│   ├── Automate the boring stuff/
│   │   └── ...                       # Пронумеровані вправи з Python
│   └── udemy/
│       ├── section_1/               # Основи Python та колекції
│       ├── section_2/               # Керування потоком, цикли, функції
│       ├── section_3/               # Міні-проєкти "Колекція фільмів"
│       ├── section_4/               # Об'єктно-орієнтоване програмування
│       └── section_5/               # Винятки та власні помилки
└── schedule-telegram-bot/
    └── bot.py                       # Telegram-бот для розкладу
```


# Python Portfolio

A collection of Python practice exercises, course projects, and a Telegram schedule bot. This repository documents the progression from Python fundamentals to object-oriented programming, error handling, and a small application that retrieves a timetable from Google Sheets.

> **Project status:** Learning portfolio. Most files are independent exercises, not modules of a single application. Some scripts are intentionally illustrative, interactive, or incomplete.

## Repository structure

```text
python-portfolio-main/
├── learning/
│   ├── Automate the boring stuff/
│   │   └── ...                       # Numbered Python exercises
│   └── udemy/
│       ├── section_1/               # Python basics and collections
│       ├── section_2/               # Control flow, loops, functions
│       ├── section_3/               # Movie collection mini-projects
│       ├── section_4/               # Object-oriented programming
│       └── section_5/               # Exceptions and custom errors
└── schedule-telegram-bot/
    └── bot.py                       # Telegram timetable bot
```

### Learning exercises

**`learning/Automate the boring stuff/`** contains introductory Python scripts practicing user input, conditionals, loops, functions, variable scope, exceptions, lists, tuples, dictionaries, string operations, and simple games. Examples include a number guessing game (`24_guessTheNumber.py`), the Collatz sequence (`25_collatz_function.py`), and a tic-tac-toe example (`39_ticTacToe.py`).

**`learning/udemy/`** organizes coursework by section:

| Section | Topics |
| --- | --- |
| `section_1` | Variables, numbers, strings, input, Boolean logic, lists, tuples, sets, dictionaries |
| `section_2` | Conditionals, loops, comprehensions, `zip`, `enumerate`, functions, lambdas |
| `section_3` | Interactive movie collection mini-projects |
| `section_4` | Classes, objects, special methods, inheritance, class/static methods |
| `section_5` | Exceptions, raising errors, custom exception types |

The section 3 exercises implement console-based movie collections with actions such as adding, displaying, and searching for movies. They store data in memory, so entries are not retained after the script exits.

## Requirements

- Python 3.10+ recommended (the exercises primarily use standard Python features).
- A terminal, or an IDE such as VS Code or PyCharm.
- For the Telegram bot only: internet access, a Telegram bot created with [BotFather](https://t.me/BotFather), and a reachable Google Sheets CSV export.

There is no dependency manifest (`requirements.txt` or `pyproject.toml`) in the supplied archive.

## Getting started

Clone the repository or download and extract its ZIP archive, then change to the project root:

```bash
git clone <your-repository-url>
cd python-portfolio-main
```

Optionally create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Run an individual learning exercise, for example:

```bash
python "learning/Automate the boring stuff/24_guessTheNumber.py"
python "learning/udemy/section_3/1_milestone_project_1.py"
```

Scripts that prompt for input should be run in an interactive terminal. The examples are standalone; there is no single portfolio-wide entry point.

> **Note:** Some educational scripts reference external files or modules not present in the archive (for example, `SecretPasswordFile.txt`, `spam`, or `config.py`), and some demonstrate infinite loops or exceptions deliberately. Those examples may need additional local setup or adjustment before they can run.

## Telegram schedule bot

**Location:** `schedule-telegram-bot/bot.py`

The bot reads a CSV timetable exported from Google Sheets and responds to commands with scheduled classes for the requested day.

### Available commands

| Command | Description |
| --- | --- |
| `/today` | Display today's classes |
| `/tomorrow` | Display tomorrow's classes |
| `/date YYYY-MM-DD` | Display classes for a selected date |

**Implementation note:** A `/start` handler is defined in a commented-out prototype at the top of the file, but **is not registered** by the currently active application. The active implementation registers only the three commands above.

### Install bot dependencies

Inside your Python environment, run:

```bash
python -m pip install pandas python-telegram-bot
```

The supplied source also imports `requests` (although it does not use it directly in the active implementation). If keeping that import, install it as well:

```bash
python -m pip install requests
```

### Configure credentials and data source

**Security warning:** The archived `bot.py` contains a Telegram bot token embedded directly in the source. **Revoke it through BotFather before sharing or deploying the repository**, issue a new token, and do not commit the replacement. If the token has previously been committed to Git, removing it from the current file does not remove it from Git history.

The current code reads the `TOKEN` and `CSV_URL` constants in `bot.py`. A safer configuration is to change those lines to:

```python
import os

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CSV_URL = os.environ["SCHEDULE_CSV_URL"]
```

This is a **recommended source-code change**, not functionality already implemented in the archived script.

Set the variables before launching the bot. On Windows PowerShell:

```powershell
$env:TELEGRAM_BOT_TOKEN = "<new-bot-token>"
$env:SCHEDULE_CSV_URL = "https://docs.google.com/spreadsheets/d/<sheet-id>/export?format=csv"
```

On macOS/Linux:

```bash
export TELEGRAM_BOT_TOKEN="<new-bot-token>"
export SCHEDULE_CSV_URL="https://docs.google.com/spreadsheets/d/<sheet-id>/export?format=csv"
```

Ensure the spreadsheet is accessible to the bot's HTTP client; an ordinary private Google Sheet URL may not work without authentication.

### Expected CSV layout

The active script expects column names **exactly** as follows:

```csv
Date,Start_time,End_time,Subject
2026-11-06,09:00,10:30,Mathematics
2026-11-06,11:00,12:30,Programming
2026-11-07,10:00,11:30,Physics
```

- `Date` uses the `YYYY-MM-DD` format.
- `Start_time` and `End_time` identify the time interval.
- `Subject` contains the class name.
- Dates are compared as strings to the local date of the machine running the bot; there is no explicit timezone setting.

### Run the bot

After installing dependencies and configuring `bot.py`:

```bash
python schedule-telegram-bot/bot.py
```

Open the bot in Telegram and send `/today`, `/tomorrow`, or `/date 2026-11-06`.

### Current limitations

- Timetable data is fetched each time a schedule command is used; there is no caching.
- The CSV download function suppresses exceptions and returns a generic failure message.
- Missing or malformed CSV columns and invalid `/date` values are not explicitly validated.
- A very long timetable may exceed Telegram's message length limit.
- The bot uses the host machine's local date rather than a configured schedule timezone.
- A `/start` command is not registered in the active bot implementation.

## Ideas for further development

- Extract shared bot configuration into environment variables and add a `.env.example` or deployment guide.
- Add input validation, explicit error logging, and graceful handling of inaccessible CSV data.
- Set an explicit timezone and improve timetable formatting.
- Add unit tests and a dependency manifest for the Telegram bot.
- Refactor the learning mini-projects into separate documented, testable applications where appropriate.

## Acknowledgments

The learning directories are organized around exercises from *Automate the Boring Stuff with Python* and Udemy-based Python coursework. They are educational practice materials rather than a redistributed copy of the original learning resources.

## License

No license file was included in the supplied archive. Add a license if you intend to define reuse and redistribution permissions for this repository.
