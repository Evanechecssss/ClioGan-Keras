from random import choice

lex: dict[str, str] = {
    'draw_word': 'нарисуй',
    'help_main': "Здравствуй, {}!",
    'button_bot_info': 'Информация о боте',
    'button_send_cat': 'Можно кота?',
    'button_face_gen': 'Нарисуй лицо',
    'bot_info': "Мы команда Клио и это наш чат-бот со встроенной нейросетью. Мы считаем, что нейронные сети не "
                "должны заменять художников, а наоборот - помогать им. \nНаш бот генерирует мини-урок по рисованию "
                "человеческой головы. \nЧтобы начать работу просто напиши боту \"сгенерируй\" и он нарисует для тебе "
                "пошаговый урок по рисованию человеческой головы! ",
    'waiting': "Подождите, я думаю.....",
    'weberror': "Возник нюанс...",
    'source_image_notification': 'Исходное. Ожидайте',
    'end_gen_notification': "Готово! Я своё отработал...",
    'gen_notification': "Этап {}!"
}

no_command_answers: list[str] = ['С Вами приятно общаться, но я не на столько умный, чтобы дать Вам ответ:(',
                                 'Мне стоит на это что-то отвечать...?',
                                 'Мне очень жаль, но общение с пользователями - не моя компетенция:(',
                                 'Я не умею осознано общаться с пользователем, но, надеюсь, мои создатели работают (нет) над этим....',
                                 'Я могу отправить Вам картинку кота....', 'Вы сейчас серьёзно это написали, {}..',
                                 '{}, не хотите поддержать нашу команду?', 'Ваня, Катя, Аня - во всех этих слова 2 буквы а и я...',
                                 'Я бот, меня создала Аня, а потом Ваня меня у неё забрал.. (памагите..)']


def answer_format(*args) -> str:
    return choice(no_command_answers).format(*args)


def lex_format(key: str, *args) -> str:
    return lex[key].format(*args)
