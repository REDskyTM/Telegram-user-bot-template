from pyrogram import Client, filters
import os

plugins = dict(root="plugins") #Даём pyrogram понять какая папка является модулей

app = Client(
    "my_account",
    api_id="", #Ваш ID, о том как его получить опишу ниже :3
		api_hash = "", #С HASH такая же история :)
    plugins = plugins #Объявляем Client что мы используем плагины то есть модули
)


@app.on_message(filters.me & filters.command("test", ".")) #Создаём нашу команду test название, . префикс получается команда .test
async def modules(app, msg): #Передаём сюда msg для того что бы работать с сообщениями
    await msg.reply("Привет, мир!") #Выводим наше сообщение reply методом


app.run() #Запуск нашего UserBot'a
