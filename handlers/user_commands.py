from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from keyboards import main_builder
from Callbacks.callback import MyCallback
from aiogram.enums import ParseMode


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(   "Привет! Добро пожаловать!\n"
                            "Я — бот для расчёта аннуитетного платежа по кредиту.\nЧтобы "
                                "воспользоваться моими услугами, следуйте инструкциям ниже:\n"
                                "1. Введите сумму кредита (принципал), годовую процентную "
                                "ставку и количество месяцев.\n"
                                "2. Я автоматически рассчитаю ежемесячный аннуитетный платеж "
                                "по вашему кредиту.\n"
                                "3. Вы получите график аннуитетных платежей, который поможет "
                                "вам понять динамику погашения кредита.\n"
                                "Готовы начать? Введите необходимые данные для расчёта!\n\n"
                                "Воспользуйтесь командой /calculate или кнопками ниже",
                                reply_markup=main_builder.as_markup())

@router.message(Command("help"))
@router.message(F.text.lower() == "помощь")
async def msg(message: Message):
    await message.answer(""""Привет! Я бот для расчета аннуитетных платежей по кредиту. Вот что я могу:

/calсulate - рассчитать аннуитетный платеж по кредиту
/help - показать это сообщение

Аннуитетный платеж - это фиксированный ежемесячный платеж по кредиту, который включает как выплату процентов, так и часть основного долга.

Формула для расчета аннуитетного платежа выглядит следующим образом:
```Формула
PMT = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

Где:
PMT - размер аннуитетного платежа,
P - сумма кредита,
r - месячная процентная ставка (годовая ставка, деленная на 12 месяцев),
n - общее количество платежей (срок кредита в годах, умноженный на 12 месяцев).```

Для расчета аннуитетного платежа мне необходима следующая информация:
- Сумма кредита
- Годовая процентная ставка
- Срок кредита в месяцах

Просто нажмите кнопку кнопки ниже и следуйте инструкциям.""", parse_mode=ParseMode.MARKDOWN, reply_markup=main_builder.as_markup())


# @router.message(Command("help"))
# async def msg(message: Message):
#     await message.answer("Тут значт будет объяснение что да как")

@router.callback_query(MyCallback.filter(F.foo == "help"))
async def help_query(query: CallbackQuery, callback_data: MyCallback):
    await query.message.answer(""""Привет! Я бот для расчета аннуитетных платежей по кредиту. Вот что я могу:

/calculate - рассчитать аннуитетный платеж по кредиту 
/help - показать это сообщение

Аннуитетный платеж - это фиксированный ежемесячный платеж по кредиту, который включает как выплату процентов, так и часть основного долга.

Формула для расчета аннуитетного платежа выглядит следующим образом:
```Формула
PMT = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

Где:
PMT - размер аннуитетного платежа,
P - сумма кредита,
r - месячная процентная ставка (годовая ставка, деленная на 12 месяцев),
n - общее количество платежей (срок кредита в годах, умноженный на 12 месяцев).```

Для расчета аннуитетного платежа мне необходима следующая информация:
- Сумма кредита
- Годовая процентная ставка
- Срок кредита в месяцах

Просто нажмите кнопку кнопки ниже и следуйте инструкциям.""", parse_mode=ParseMode.MARKDOWN, reply_markup=main_builder.as_markup())