# September 2024 Lisa Karaseva @Aglamorousfortuneteller
#



import random
import telebot
from telebot import types

bot = telebot.TeleBot('7754340937:AAH08IEbm3lCS2kaZdEy210hrFhaJjRZGlw')




# Language dictionaries for different languages
translations = {
    'English': {
        'start_msg': 'Hello! 👋 Choose Rock 🪨, Scissors ✂️, or Paper 📄.',
        'rock': 'Rock 🪨',
        'scissors': 'Scissors ✂️',
        'paper': 'Paper 📄',
        'choose_msg': 'I choose: ',
        'win_msg': 'You won! 😊',
        'lose_msg': 'You lost. 😔',
        'tie_msg': 'Tie! 🤝',
        'invalid_msg': 'Invalid input. Please, choose Rock 🪨, Scissors ✂️, or Paper 📄.'
    },
    'Russian': {
        'start_msg': 'Привет! 👋 Выберите Камень 🪨, Ножницы ✂️ или Бумагу 📄.',
        'rock': 'Камень 🪨',
        'scissors': 'Ножницы ✂️',
        'paper': 'Бумага 📄',
        'choose_msg': 'Я выбираю: ',
        'win_msg': 'Вы выиграли! 😊',
        'lose_msg': 'Вы проиграли. 😔',
        'tie_msg': 'Ничья! 🤝',
        'invalid_msg': 'Неверный ввод. Пожалуйста, выберите Камень 🪨, Ножницы ✂️ или Бумагу 📄.'
    },
    'French': {
        'start_msg': 'Bonjour! 👋 Choisissez Pierre 🪨, Ciseaux ✂️ ou Papier 📄.',
        'rock': 'Pierre 🪨',
        'scissors': 'Ciseaux ✂️',
        'paper': 'Papier 📄',
        'choose_msg': 'Je choisis: ',
        'win_msg': 'Vous avez gagné! 😊',
        'lose_msg': 'Vous avez perdu. 😔',
        'tie_msg': 'Égalité! 🤝',
        'invalid_msg': 'Entrée non valide. Veuillez choisir Pierre 🪨, Ciseaux ✂️ ou Papier 📄.'
    },
    'Swedish': {
        'start_msg': 'Hej! 👋 Välj Sten 🪨, Sax ✂️ eller Papper 📄.',
        'rock': 'Sten 🪨',
        'scissors': 'Sax ✂️',
        'paper': 'Papper 📄',
        'choose_msg': 'Jag väljer: ',
        'win_msg': 'Du vann! 😊',
        'lose_msg': 'Du förlorade. 😔',
        'tie_msg': 'Oavgjort! 🤝',
        'invalid_msg': 'Ogiltigt val. Välj Sten 🪨, Sax ✂️ eller Papper 📄.'
    },
    'Dutch': {
        'start_msg': 'Hallo! 👋 Kies Steen 🪨, Schaar ✂️, of Papier 📄.',
        'rock': 'Steen 🪨',
        'scissors': 'Schaar ✂️',
        'paper': 'Papier 📄',
        'choose_msg': 'Ik kies: ',
        'win_msg': 'Je hebt gewonnen! 😊',
        'lose_msg': 'Je hebt verloren. 😔',
        'tie_msg': 'Gelijkspel! 🤝',
        'invalid_msg': 'Ongeldige invoer. Kies alsjeblieft Steen 🪨, Schaar ✂️, of Papier 📄.'
    }
}

# Store user language choices
user_languages = {}

# Function to create language selection keyboard
def language_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("English"), types.KeyboardButton("Russian"))
    keyboard.add(types.KeyboardButton("French"), types.KeyboardButton("Swedish"))
    keyboard.add(types.KeyboardButton("Dutch"))
    return keyboard

# Function to add the custom keyboard based on the language
def add_keyboard(language):
    trans = translations[language]

    # Create buttons based on language
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rock_bttn = types.KeyboardButton(trans['rock'])
    scissors_bttn = types.KeyboardButton(trans['scissors'])
    paper_bttn = types.KeyboardButton(trans['paper'])
    keyboard.add(rock_bttn, scissors_bttn, paper_bttn)

    return keyboard


# Bot command to start the game and select language
@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = language_keyboard()
    bot.send_message(message.chat.id, 'Please choose your language:', reply_markup=keyboard)

# Bot message handler for language selection
@bot.message_handler(func=lambda message: message.text in translations.keys())
def set_language(message):
    user_languages[message.chat.id] = message.text
    language = user_languages[message.chat.id]
    keyboard = add_keyboard(language)
    bot.send_message(message.chat.id, translations[language]['start_msg'], reply_markup=keyboard)

# Function to simulate the bot's move in Rock-Paper-Scissors
def rock_paper_scissors(language):
    trans = translations[language]
    moves = [trans['rock'], trans['scissors'], trans['paper']]
    return random.choice(moves)

# Main message handler for game logic
@bot.message_handler(func=lambda message: message.chat.id in user_languages and message.text in [
    translations[user_languages[message.chat.id]]['rock'], 
    translations[user_languages[message.chat.id]]['scissors'], 
    translations[user_languages[message.chat.id]]['paper']])
def get_user_message(message):
    language = user_languages[message.chat.id]
    trans = translations[language]
    user_input = message.text

    # Get bot's random move
    bot_move = rock_paper_scissors(language)

    # Define winning, losing, and tie combinations
    user_win_combs = {
        (trans['rock'], trans['scissors']), 
        (trans['paper'], trans['rock']),
        (trans['scissors'], trans['paper'])
    }

    user_fail_combs = {
        (trans['paper'], trans['scissors']), 
        (trans['rock'], trans['paper']),
        (trans['scissors'], trans['rock'])
    }

    # Send bot's move to the user
    bot.send_message(message.chat.id, f"{trans['choose_msg']}{bot_move}")

    # Check the result using tuples
    if (user_input, bot_move) in user_win_combs:
        bot.send_message(message.chat.id, trans['win_msg'])
    elif (user_input, bot_move) in user_fail_combs:
        bot.send_message(message.chat.id, trans['lose_msg'])
    elif user_input == bot_move:
        bot.send_message(message.chat.id, trans['tie_msg'])

# Polling with reduced interval
bot.polling(none_stop=True, interval=0.5)
