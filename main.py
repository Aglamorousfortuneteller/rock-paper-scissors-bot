import random
import telebot
from telebot import types

bot = telebot.TeleBot('YUOR TOKEN GOES HERE')

# Define the user_languages globally before any handlers
user_languages = {}  # This will store user language preferences

# Language dictionaries for different languages (polite responses)
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

# Offensive Replies for all languages
offensive_replies = {
    'English': {
        'lose': [
            "You lost. Loser, huh?",
            "Wow, another loss! Surprised? You shouldn’t be.",
            "Seems like you're getting used to losing.",
            "Missed it again? Some people are just born losers."
        ],
        'win': [
            "Congrats... on something totally insignificant.",
            "You got lucky. Don't let it go to your head.",
            "Feeling good? Wait till the next round.",
            "One win doesn't make you a champion."
        ],
        'tie': [
            "Oh, a tie. What an achievement!",
            "Tie? That's what weaklings do.",
            "No score, just like your life."
        ]
    },
    'Russian': {
        'lose': [
            "Проиграл. Лох получается.",
            "Ну вот, опять лох.",
            "Не твой день, да? Хотя, когда он был?",
            "Опять мимо. Видимо, это твое призвание."
        ],
        'win': [
            "Ну выиграл, че сразу герой?",
            "Поздравляю с чем-то абсолютно незначительным.",
            "Чувствуешь себя крутым? Посмотри на свою жизнь.",
            "Одна победа ничего не значит."
        ],
        'tie': [
            "Ничья — это для слабаков.",
            "По нулям, как твоя удача."
        ]
    },
    'French': {
        'lose': [
            "Perdu. Encore un perdant.",
            "Une autre défaite! Quelle surprise... non?",
            "Tu commences à t'habituer à perdre, non?",
            "La chance n'est définitivement pas de ton côté.",
            "Encore raté? Ça doit être ton destin."
        ],
        'win': [
            "Gagné? Ne te prends pas pour un héros.",
            "Félicitations... pour quelque chose d'insignifiant.",
            "Juste un coup de chance, ne t'emballe pas.",
            "Tu te sens puissant? Attends la prochaine manche.",
            "Une victoire, mais t'es pas encore champion."
        ],
        'tie': [
            "Égalité, c'est ce que font les faibles.",
            "Égalité. Zéro comme ta chance."
        ]
    },
    'Swedish': {
        'lose': [
            "Förlorade du? Släng dig i backen.",
            "Förlorade du? Gå och dra något gammalt över dig.",
            "En till förlust, vad förvånad... eller inte.",
            "En till förlust, yxskaft",
            "Tur verkar inte vara din grej.",
            "Missade igen? Det är kanske din grej att förlora."
        ],
        'win': [
            "Jaha, du vann. Ska du ha en medalj?",
            "Grattis… på ett sätt, antar jag.",
            "Det var bara tur, tro inte att du är något.",
            "En seger, men det betyder inte att du är bäst."
        ],
        'tie': [
            "Oavgjort igen. Gå och dra något gammalt över dig.",
            "Oavgjort igen. Grattis… antar jag?",
            "Oavgjort? Dra åt skogen.",
            "Inga poäng, precis som din tur."
        ]
    },
    'Dutch': {
        'lose': [
            "Verloren? Wat een verrassing... niet dus.",
            "Alweer verloren! Wordt een gewoonte, hè?",
            "Misschien moet je gewoon wennen aan verliezen.",
            "Je hebt echt geen geluk vandaag, of ooit eigenlijk.",
            "Mis weer? Dit lijkt jouw ding te zijn."
        ],
        'win': [
            "Gewonnen? Niet naast je schoenen gaan lopen, hoor.",
            "Gefeliciteerd... met iets totaal onbelangrijks.",
            "Voel je je goed? Wacht maar op de volgende ronde.",
            "Eén keer winnen betekent niet dat je een kampioen bent."
        ],
        'tie': [
            "Gelijkspel? Saai hoor.",
            "Nog een gelijkspel? Wat wil je daarmee?",
            "Gelijkspel alweer? Beetje moeite doen, graag.",
            "Gelijkspel? Dat doen alleen zwakkelingen.",
            "Geen punten, net als je geluk."
        ]
    }
}

# Function to select either polite or offensive replies based on probability
def select_reply(trans, offensive, key):
    # 60% chance for polite, 40% chance for offensive
    if random.random() < 0.4:
        return random.choice(offensive[key])
    else:
        return trans[key + '_msg']

# Function to create language selection keyboard
def language_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("English"), types.KeyboardButton("Russian"))
    keyboard.add(types.KeyboardButton("French"), types.KeyboardButton("Swedish"))
    keyboard.add(types.KeyboardButton("Dutch"))
    return keyboard

# Function to create custom game keyboard with restart/stop options
def game_keyboard(language):
    trans = translations[language]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rock_bttn = types.KeyboardButton(trans['rock'])
    scissors_bttn = types.KeyboardButton(trans['scissors'])
    paper_bttn = types.KeyboardButton(trans['paper'])
    keyboard.add(rock_bttn, scissors_bttn, paper_bttn)
    keyboard.add(types.KeyboardButton("Change Language"), types.KeyboardButton("Restart"))
    keyboard.add(types.KeyboardButton("Stop"))
    return keyboard

# Bot command to start the game and select language
@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = language_keyboard()
    bot.send_message(message.chat.id, 'Please choose your language. You can also type /start anytime to begin.', reply_markup=keyboard)

# Change Language button handler
@bot.message_handler(func=lambda message: message.text == "Change Language")
def handle_choose_language(message):
    keyboard = language_keyboard()
    bot.send_message(message.chat.id, 'Please choose your language:', reply_markup=keyboard)

# Restart button handler
@bot.message_handler(func=lambda message: message.text == "Restart")
def handle_restart(message):
    chat_id = message.chat.id
    if chat_id in user_languages:
        language = user_languages[chat_id]
        trans = translations[language]
        bot.send_message(chat_id, trans['start_msg'], reply_markup=game_keyboard(language))
    else:
        bot.send_message(chat_id, translations['English']['start_msg'], reply_markup=language_keyboard())

# Stop button handler
@bot.message_handler(func=lambda message: message.text == "Stop")
def handle_stop(message):
    bot.send_message(message.chat.id, 'The game has been stopped. Type /start to play again.')

# Bot message handler for language selection
@bot.message_handler(func=lambda message: message.text in translations.keys())
def set_language(message):
    user_languages[message.chat.id] = message.text
    language = user_languages[message.chat.id]
    keyboard = game_keyboard(language)
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
    offensive = offensive_replies[language]
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
        reply = select_reply(trans, offensive, 'win')
    elif (user_input, bot_move) in user_fail_combs:
        reply = select_reply(trans, offensive, 'lose')
    elif user_input == bot_move:
        reply = select_reply(trans, offensive, 'tie')

    bot.send_message(message.chat.id, reply)

# Fallback handler to catch all other messages
@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    chat_id = message.chat.id
    if chat_id not in user_languages:
        keyboard = language_keyboard()
        bot.send_message(chat_id, 'Please choose your language. You can also type /start anytime to begin.', reply_markup=keyboard)

# Polling with reduced interval
bot.polling(none_stop=True, interval=0.5)
