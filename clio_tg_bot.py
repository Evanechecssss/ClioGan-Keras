from typing import Final

from aiogram import executor
from aiogram.types import Message, ContentType
from aiogram.dispatcher.filters import Command
from magic_filter import F
from tqdm import keras

from cliogan.model_service import load_image_url, image_to_image, load_model
from lexicon import lex, lex_format, answer_format
from modules_import import *
from keyboards import keyboard_lobby


class ClioTelegramBotHandler:
    def __init__(self, *args):
        config: Final[Config] = Config.get(*args)

        self.sd = config.sd
        self.bot = config.bot
        self.dp = config.dp
        self.run()

        executor.start_polling(self.dp, skip_updates=False)

    def run(self):
        @self.dp.message_handler(Command(commands=['start']))
        async def start_command(message: Message):
            await message.answer(lex_format('help_main', message.from_user.first_name), reply_markup=keyboard_lobby())

        @self.dp.message_handler(F.content_type == ContentType.TEXT)
        async def text_message(message: Message):
            text = message.text
            if text == lex['button_bot_info']:
                await message.answer(lex["bot_info"])
            elif text == lex['button_send_cat']:
                await message.answer(Config.get().LOGO_URL)
            elif text.startswith(lex['draw_word']) or text == lex['button_face_gen']:
                await message.answer(lex['waiting'])
                url = await self.sd.text_to_image(message.text.lower())
                if url:
                    await self.bot.send_photo(message.chat.id, photo=url, caption=lex['source_image_notification'])
                    src_image = load_image_url(url, remove_bg=True)
                    for i in range(4):
                        to_send = keras.utils.array_to_img(image_to_image(load_model(i), src_image)[0, :, :, :])
                        await self.bot.send_photo(message.chat.id, photo=to_send,
                                            caption=lex['end_gen_notification'] if i == 3 else lex_format('gen_notification', i))
                else:
                    await message.answer(lex['weberror'])
            else:
                await message.answer(answer_format(message.from_user.first_name))


def run_clio_telegram_bot(*args):
    return ClioTelegramBotHandler(*args)
