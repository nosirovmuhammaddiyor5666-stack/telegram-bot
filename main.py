import asyncio 
from  aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message ,BotCommand,FSInputFile,CallbackQuery
from bottons import main_buttons,school_buttons,it_buttons,coder_buttons

bot = Bot(token= "8795474224:AAF1HRrLpyrYBdqZHJrOlR8pqAssak6rVQQ")
dp = Dispatcher()

@dp.message(Command("start"))
async def handStart(message: Message):
    chat_id = message.chat.id
    print(chat_id)
    full_name = message.from_user.full_name
    await message.answer(f"Botga hush kelibsiz {full_name}",
                        reply_markup=await main_buttons())

@dp.message(F.text == "maktab darsliklari")  
async def rection_to_school_lessonI(messagae: Message):
    await messagae.answer("Sinfni tanlang",reply_markup= await school_buttons())


@dp.message(F.text == "IT kurslari")
async def ItCourse_lesson(message: Message):
    await message.answer("Tanlang! ",reply_markup= await it_buttons())

@dp.message(F.text == "Dasturlash boyicha qolanma")
async def qollanma(message: Message):   
    await message.answer("Qaysi tili boyicha qolanma kerak ?",reply_markup= await coder_buttons())


@dp.message(F.text == "Go Back")
async def rection_to_go_back(message: Message):
    await message.answer("Asosiy sahifa",reply_markup= await main_buttons())


@dp.message(Command("help"))
async def handHelp(message: Message):
    await message.answer("yordam uchun @MDlyor ga murojat qiling")

@dp.message(Command("admin"))
async def handAdmin(message: Message):
    await message.answer("1)Admin: @MDlyor")

@dp.message(Command("coder"))
async def handCoder(message: Message):
    await message.answer("@MDlyor")

@dp.message(Command("settings"))
async def handSettings(message: Message):
    await message.answer("⚙️ Sozlamalar bo'limi:\nTez orada bu yerda tillarni o'zgartirish imkoniyati qo'shiladi.")

@dp.message(F.text=="salom")
async def salomHand(message: Message):
    await message.answer("Valaykum salom nma yordam bera olaman")


@dp.message(F.text.endswith("-sinf darsliklari"))
async def rection_to_lesson(message: Message):
    if message.text == "1-sinf darsliklari":
        await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjoI0_E9fD5k5aKCb60tIgB4xBhsLhidBhNSJCvAvLbQ&s=10")
        loading = await message.answer("File yuklanmoqda...")
        file = FSInputFile("file/1-SinfMatematika.pdf")
        await message.answer_document(file)
        await loading.delete()
    elif message.text == "2-sinf darsliklari":
        await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlJE888tj9qYZ03XiJI0XW5w6F9IuiOTpvNDBB5-VQeA&s=10")
        file = FSInputFile("file/2-SinfMatematika.pdf")
        loading = await message.answer("File yuklanmoqda...")
        await message.answer_document(file)
        await loading.delete()
    elif message.text == "3-sinf darsliklari":
        await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTs22WCAz1J9h5s7dZ2VETpaK76JRUSZAchwIZidas5CA&s=10")
        file = FSInputFile("file/3-SinfMatematika.pdf")
        loading = await message.answer("File yuklanmoqda...")
        await message.answer_document(file)
        await loading.delete()
    elif message.text == "4-sinf darsliklari":
        await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3hxzYW8Ng-aLZAs78f73Rdo35MdfzjhDrzFmmFSuqtg&s=10")
        file = FSInputFile("file/4-SinfMatematika.pdf")
        loading = await message.answer("File yuklanmoqda...")
        await message.answer_document(file)
        await loading.delete()

@dp.callback_query(F.data == "C")
async def C_Course(callback: CallbackQuery):
    await callback.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2hzhiHaCZVnkAo4QpmfSQByrTzD-hz_ibVoZq2ept2Q&s=10")
    file = FSInputFile("dasturlash qolanmasi/C.txt")
    loading = await callback.message.answer("File yuklanmoqda...")
    await callback.message.answer_document(file)
    await loading.delete()

@dp.callback_query(F.data == "Python")
async def python_course(callback: CallbackQuery):
    await callback.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_b9VM0YaR0i5EjFImk2rl9x9AmObWO4wJeXTieqRwUQ&s=10")
    file = FSInputFile("dasturlash qolanmasi/Pyhton.txt")
    loading = await callback.message.answer("File yuklanmoqda...")
    await callback.message.answer_document(file)
    await loading.delete()

@dp.callback_query(F.data == "C++")
async def python_course(callback: CallbackQuery):
    await callback.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTygmEA8YGw-sseym7nmXA-rv5ekOc_f6H8ChDqkjqjCQ&s=10")
    file = FSInputFile("dasturlash qolanmasi/C++.txt")
    loading = await callback.message.answer("File yuklanmoqda...")
    await callback.message.answer_document(file)
    await loading.delete()

@dp.callback_query(F.data == "Java")
async def python_course(callback: CallbackQuery):
    await callback.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ42E9Zl6vBTuposp5mrZFIz34jjKn2BmcYl_lRx6Ugog&s=10")
    file = FSInputFile("dasturlash qolanmasi/Java.txt")
    loading = await callback.message.answer("File yuklanmoqda...")
    await callback.message.answer_document(file)
    await loading.delete()

@dp.message(F.contact)
async def contact(message: Message):
    user_name = message.chat.first_name
    user_phone = message.contact.phone_number
    await message.answer("Kontaktingiz qabul qilindi!")
    await message.answer(f"Ismingiz: {user_name}\nContact: {user_phone}")

@dp.message(F.location)
async def location(message: Message):
    user_name = message.chat.first_name
    await message.answer(f"Sizning Location qabul qilindi {user_name}")




@dp.message()
async def give(message: Message):
    await bot.send_message(chat_id=5891166251,text= f"Sizga habar yuborildi: {message.text}")
    await message.answer("Habaringiz qabul qilindi!")

    


@dp.message(F.contact)
@dp.message(F.location)
@dp.message(F.voice)
@dp.message(F.photo)
@dp.message(F.audio)
@dp.message(F.text)
async def get_text(message: Message):
    await message.answer("Habaringiz qabul qilindi!")


    

async def main():
    await bot.set_my_commands(commands=[BotCommand(command="start",description="botni ishga tushurish"),
                                        BotCommand(command= "help",description="Yordam murojati"),
                                        BotCommand(command= "admin",description="admin username"),
                                        BotCommand(command= "settings",description="sozlamalar"),
                                        BotCommand(command= "coder",description="@MDlyor")
                                        ])
    await dp.start_polling(bot)

asyncio.run(main())
