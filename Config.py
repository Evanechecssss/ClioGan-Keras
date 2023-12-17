from typing import Final

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from environs import Env
from StableDiffusionProxy import StableDiffusionProxy


class Config:
    __instance = None

    def __init__(self, *args):
        env: Final[Env] = Env()
        env.read_env()

        self.BOT_TOKEN: Final[str] = env('BOT_TOKEN')
        self.SD_TOKEN: Final[str] = env('SD_TOKEN')
        self.LOGO_URL: Final[str] = env('LOGO_URL')

        self.bot: Final[Bot] = Bot(self.BOT_TOKEN)
        self.sd: Final[StableDiffusionProxy] = StableDiffusionProxy(self.SD_TOKEN)
        self.storage: MemoryStorage = MemoryStorage()
        self.dp: Final[Dispatcher] = Dispatcher(self.bot, storage=self.storage)

    @staticmethod
    def get(*args):
        if Config.__instance is None:
            Config.__instance = Config(*args)
        return Config.__instance
