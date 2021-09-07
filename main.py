import logging
from aiogram import Bot, Dispatcher, executor, types
from getDefinition import getDefinition
from googletrans import Translator

translator = Translator()

API_TOKEN = 'YOUR_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("Hello everybody, this is Translator bot!")

@dp.message_handler(commands=['help'])
async def about(message: types.Message):
    
    await message.reply("Ushbu bot orqali siz matn kiritsangiz uni tarjima qilib olishingiz, yoki so'z kiritsangiz u\
    haqida to\'liq ma\'lumot olishingiz mumkin!")

@dp.message_handler()
async def echo(message: types.Message):
    lang = translator.detect(message.text).lang
    word = ''
    if lang == 'en':
        word = message.text
    else:
        word = translator.translate(message.text, src=lang, dest='en').text

    if (len(word.split()) >= 2):
        des = 'uz' if lang == 'en' else 'en'
        await message.answer(translator.translate(message.text, des).text)
    else:
        ans = ''
        out = getDefinition(word)
        if out:
            ans += f"🇬🇧 Word : {out['word']} \n\n"
            ans += f"🇬🇧 Transcription : {out['transcription']} \n\n"
            ans += f"🇬🇧 Definitions of '{word}': \n{out['definition']} \n\n"
            if out['synonyms']:
                ans += f"🇬🇧 Synonyms : {out['synonyms']}"
            await message.answer(ans)
            if out['audio']:
                await message.reply_voice(out['audio'])
        else:
            await message.answer('afsuski bunday ma\'lumot topilmadi :(')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
