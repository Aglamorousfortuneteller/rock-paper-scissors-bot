
# Rock-Paper-Scissors Telegram Bot

This project is a multilingual Rock-Paper-Scissors game bot for Telegram, developed using Python and the `pyTelegramBotAPI` library. Users can play the classic game in their preferred language, including English, Russian, French, Swedish, and Dutch.

## Features
- Multilingual support: English, Russian, French, Swedish, and Dutch.
- Simple and interactive interface with custom keyboards for easy game play.
- Randomized bot responses to simulate playing against an opponent.

## Prerequisites
- Python 3.7 or above.
- `pyTelegramBotAPI` library.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/username/rock-paper-scissors-bot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd rock-paper-scissors-bot
   ```
3. Install the required dependencies:
   ```sh
   pip install pyTelegramBotAPI
   ```

## Usage
1. Update the `bot.py` file with your Telegram bot token:
   ```python
   bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
   ```
2. Run the bot:
   ```sh
   python bot.py
   ```
3. Start a conversation with your bot on Telegram using the `/start` command, select your language, and begin playing Rock-Paper-Scissors.

## Game Flow
- The user starts by selecting a language.
- The bot presents options for Rock, Paper, or Scissors using a custom keyboard.
- The bot randomly selects its move and sends the result to the user.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Developed using the `pyTelegramBotAPI` library.
- Inspired by the classic Rock-Paper-Scissors game.
