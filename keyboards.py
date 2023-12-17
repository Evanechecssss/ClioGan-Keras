from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon import lex

SetButton = tuple[tuple[str, ...], ...]


def keyboard_lobby() -> ReplyKeyboardMarkup:
    buttons_text: SetButton = (('button_bot_info', 'button_send_cat',),
                               ('button_face_gen',))
    return keyboard_builder(buttons_text)


def button_builder(name: str) -> KeyboardButton:
    return KeyboardButton(text=lex[name])


def keyboard_builder(buttons_text: SetButton) -> ReplyKeyboardMarkup:
    buttons: list[list[KeyboardButton]] = []
    for array in buttons_text:
        line: list[KeyboardButton] = []
        for text in array:
            line.append(button_builder(text))
        buttons.append(line)
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
