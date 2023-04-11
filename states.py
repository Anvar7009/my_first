from aiogram.dispatcher.filters.state import State,StatesGroup


#процессы для регистрации
class Registration(StatesGroup):
    getting_name_state = State()
    getting_phone_number = State()
    getting_location = State()
    getting_gender = State()

#процессы для выбора определенного товара
class GetProduct(StatesGroup):
    getting_pr_name = State()
    getting_pr_count = State()


# процессы при работе с корзиной
class Cart(StatesGroup):
    waiting_for_product = State()
    waiting_new_count = State()


# процессы при офрмления заказа
class Order(StatesGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accept = State()