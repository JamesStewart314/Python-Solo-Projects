# /----------------------------------------------------------------------------------------------------\
#            This code is a Responsive Telegram Chatbot with basic learning capabilities 
#              created in Python language - version 3.12 or higher - with dependencies 
#                  on the "python-telegram-bot", "aiofiles" and "uvloop" libraries.
#              
#              note: uvloop is not available in Windows systems. Download this library  
#                      only if you are running the code on a Linux distribution!
#
#          For the code to work correctly, it is essential to provide confidential information,
#   such as the associated TOKEN. However, due to the sensitive nature of this data, I cannot share it
#                      publicly. Unfortunately, without this crucial information, 
#                       the code will be unable to run properly on your machine.
#
#                                   Code Created in ~ 03/09/2024 ~
# \----------------------------------------------------------------------------------------------------/


from confidential_information import CHATBOT_TOKEN

import os
import csv
import asyncio
from difflib import get_close_matches

import aiofiles

if os.name == 'posix':
    # Changing the Event loop Policy in Asyncio 
    # if Running on a Linux Distribution :
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)

from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.ext import MessageHandler, filters, ContextTypes

from typing import Any, Final, Generator


# -----------------------------------  Constants  ----------------------------------- #
TOKEN: Final[str] = CHATBOT_TOKEN
BOT_USERNAME: Final[str] = '@tychobrahe7_bot'
HERE_PATH: Final[str] = os.path.abspath(os.path.dirname(__file__))
FILE_PATH: Final[str] = os.path.abspath(os.path.join(HERE_PATH, "knowledge_base.csv"))
# ----------------------------------------------------------------------------------- #


new_response: str = ""


def find_best_match(user_question: str) -> str | None:

    #  Search for possible matches of the user's question in a 
    # CSV dataset and returns the corresponding answer.

    # Getting the Best Possible Match :
    matches = get_close_matches(user_question,
                                load_knowledge_base(FILE_PATH),
                                n=1, cutoff=0.95)

    return matches[0] if matches else None


def load_knowledge_base(file_path: str, /) -> Generator[str, None, None]:
    
    # Loads the Knowledge Base from a CSV file.

    with open(file_path, mode='r', newline="") as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        for line in csv_reader:
            yield line[0]


def get_answer_for_question(file_path: str, match: str, /) -> str | None:

    #  Searches for the answer corresponding 
    # to a given entry present in the dataset.

    with open(file_path, mode='r', newline="") as file:
        csv_reader = csv.reader(file, delimiter=';')
        
        for line in csv_reader:
            if line[0] == match:
                return line[1]


def handle_response(text: str, /) -> str | None:
    
    processed_text: str = text.lower().strip()

    best_match: str | None = find_best_match(processed_text)

    if best_match is not None:
        response: str | None = get_answer_for_question(FILE_PATH, best_match)

        return response


async def save_new_base_knowledge(file_path: str, new_data: list[str]) -> None:
    
    #  Saves the New Knowledge Base Provided by 
    # the User During the Chat to a CSV file.

    async with aiofiles.open(file_path, mode='a', newline="") as file:
        csv_writer = csv.writer(file, delimiter=";")

        await asyncio.create_task(csv_writer.writerow(new_data))


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE, /) -> None:
    await update.message.reply_text("Hello there! Nice to meet you!!! ~ 🍁✨\n"\
                                    "My name is TychoBrahe, an experimental "\
                                    "Chatbot created by Allber Fellype, Let\'s talk!")
    
    kitty_ascii: str = """
 ╱|、
(˚ˎ 。7  
|、˜〵          
じしˍ,)ノ"""

    await update.message.reply_text(kitty_ascii)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE, /) -> None:
    await update.message.reply_text("Unfortunately, for now, my lazy creator chose not to "\
                                    "implement specific features and "\
                                    "functionalities for me... But who knows, "\
                                    "maybe this scenario will be reversed in "\
                                    "the near future, I hope..."\
                                    "\n\n\t⋆.ೃ࿔*:･‧₊˚ ☁️⋅𓂃 ࣪ ִֶָ☾.🌧️.𖥔 ݁ ˖༄"\
                                    "\n   ✨ ( ｡ •̀ ᴖ •́ ｡) ~ 🫧༘⋆𓇢𓆸  ✨")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE, /) -> None:
    await update.message.reply_text("Nope, no Custom Commands, at least for now.\n\n(˵ •̀ ᴗ - ˵ ) 💻✨")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    global new_response
    
    message_type: str = update.message.chat.type
    text: str = update.message.text.strip()

    # Log :
    print(f'User ({update.message.chat.id}) in {message_type}: \"{text}\"')

    if not new_response:
        # Handle Message Type :
        if message_type == 'group':
            if BOT_USERNAME in text:
                new_text: str = text.replace(BOT_USERNAME, '').strip()
                response: str = handle_response(new_text)

            else:
                return None
            
        else:
            response: str = handle_response(text)

        if response is not None:
            # Reply :
            print('Bot: ', response)
            await update.message.reply_text(response.title())
        
        else:
            mismatch_response: str = "Sorry, I don\'t know the answer to this question... "\
                                    "Please, can you teach me the answer?\n\nType the answer "\
                                    "below or type \'skip\' to skip."
            await update.message.reply_text(mismatch_response)

            new_response = text
    else:
        if text.lower() != 'skip':
            await save_new_base_knowledge(FILE_PATH, [new_response.lower(), text.lower()])
        
        new_response = ""

        await update.message.reply_text("Thanks for the learning! I will remember this!!!"\
                                        "\n\n⋆.ೃ࿔*:･ ᕙ( •̀ ᗜ •́ )ᕗ ࿐ ࿔*:･ﾟ")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE, /) -> None:
    
    global new_response

    new_response = ""

    await update.message.reply_text("Oh... i\'m sorry, some characters or symbols "\
                                    "in your message is invalid... \n(｡ • ᴖ • )~.𖥔 ݁ ˖")
    print(f'Update {update} caused error {context.error}.')


def _main(args: Any = None) -> None:

    print('Starting up Bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages :
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors :
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    _main()
