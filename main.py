import discord
import sqlite3
from dotenv import load_dotenv
import os

client = discord.Client()
db = sqlite3.connect('data.db')
cur = db.cursor()

Flen4tag = "<@!414374860849020939>"
load_dotenv()
TOKEN = os.getenv('TOKEN')

class Bot(discord.Client):

    def QueryCounterTable(self, keyword):
        if keyword == "all":
            cur.execute("SELECT * FROM Counter")
            return cur.fetchall()
        else:
            cur.execute("SELECT * FROM Counter WHERE `Action` = '{0}'".format(keyword))
            result = cur.fetchall()
            return result[0]

    def IncreaseCounterField(self, keyword):
            cur.execute("UPDATE `Counter` SET `Count` = `Count` + 1 WHERE `Action` = '{0}'".format(keyword))
            db.commit()
            return print("increased successfully")


    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        ##        ####        ####        ####        ####        ####        ####        ####        ####
        #СТАТИСТИКА
        ##        ####        ####        ####        ####        ####        ####        ####        ####
        if message.content == "TAI скока":
            result = self.QueryCounterTable("all")
            for elem in result:
                await message.channel.send("{2} заебал нас {0} всего {1} раз".format(elem[0], elem[1], Flen4tag))

        if message.content == "TAI скока bloodhunt":
            result = self.QueryCounterTable("Bloodhunt")
            await message.channel.send("{2} заебал нас {0} всего {1} раз".format(result[0], result[1],Flen4tag))

        if message.content == "TAI скока youtube":
            result = self.QueryCounterTable("Youtube")
            await message.channel.send("{2} заебал нас {0} всего {1} раз".format(result[0], result[1],Flen4tag))

        ##        ####        ####        ####        ####        ####        ####        ####        ####
        # МОДИФИЦИРУЕМ ЗНАЧЕНИЯ
        ##        ####        ####        ####        ####        ####        ####        ####        ####

        if message.content == "TAI +1 bloodhunt":
            self.IncreaseCounterField("Bloodhunt")
            result = self.QueryCounterTable("Bloodhunt")
            await message.channel.send("Защитали +1 мудиле, всего в {0} {1} раз уже сука!!!".format(result[0], result[1]))

        if message.content == "TAI +1 youtube":
            self.IncreaseCounterField("Youtube")
            result = self.QueryCounterTable("Youtube")
            await message.channel.send("Защитали +1 мудиле, всего в {0} {1} раз уже сука!!!".format(result[0], result[1]))

client = Bot()
client.run(TOKEN)


client.run(TOKEN)