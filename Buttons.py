from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# кнопка для отправки номера телефона
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("поделится конктом", request_contact=True)

    kb.add(button)

    return kb


# кнопка для отправки локации
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("поделится локации", request_location=True)

    kb.add(button)

    return kb


# кнопка для выбора пола
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("мужчина")
    button2 = KeyboardButton("женшина")

    kb.add(button, button2)

    return kb


# кнопки для выбора количества
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]

    back = KeyboardButton("назад")

    kb.add(*buttons, back)

    return kb


# кнопки для корзины
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("очистить")
    button2 = KeyboardButton("оформления заказа")
    button3 = KeyboardButton("Редактировать")
    button4 = KeyboardButton("назад")

    kb.add(button, button2, button3, button4)

    return kb


# кнопки при выборе способ оплаты
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("наличные")
    button2 = KeyboardButton("картой")
    button3 = KeyboardButton("назад")

    kb.add(button, button2, button3)

    return kb


# Кнопки для потверждения заказа
def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("потвердить")
    button2 = KeyboardButton("отменить")
    button3 = KeyboardButton("назад")

    kb.add(button, button2, button3)

    return kb


# кнопки с названием товара
def products_kb():
    pass
