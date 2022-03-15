import datetime
import pytz 
import utils.utils as utils
from decouple import config
from discord.ext import commands, tasks


# Constants
PETIANES = config("PETIANES_ID")
RETRO_CHANNEL = config("RETRO_CHANNEL")


flag = 1
retro_day = utils.initialize_date(datetime.date(2022, 1, 28), 14)


class Retrospective(commands.Cog):
    """Commands about the biweekly retrospective on discord"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.is_retrospective_eve.start()

    # Command: Retrospectiva
    @commands.command(name="retro")
    async def retrospective(self, ctx):
        days_to_retro = retro_day - datetime.date.today()
        if days_to_retro.days < 2:
            if days_to_retro.days == 1: 
                await ctx.reply(f'falta {days_to_retro.days} dia até a próxima retrospectiva, que será no dia {retro_day.day:02d}/{retro_day.month:02d}.')
            elif days_to_retro.days == 0:
                await ctx.reply("hoje é o dia da retro! vai lá escrever seu texto que ainda da tempo.")    
            else:
                await ctx.send("erro na data da retrospectiva")
        else:
            await ctx.reply(f'faltam {days_to_retro.days} dias até a próxima retrospectiva, que será no dia {retro_day.day:02d}/{retro_day.month:02d}.')

    # Command: Retrospectiva Manual
    @commands.command(name="retro_manual")
    async def set_retrospective(self, ctx, arg):
        day, month = arg.split('/')
        if int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12:
            await ctx.reply("informe uma data válida.")
        elif (datetime.date(int(datetime.date.today().year), int(month), int(day)) - datetime.date.today()).days < 0:
            await ctx.reply("informe uma data válida.")
        else:
            global flag
            if flag == 1:
                flag = 0
                await self.turn_off_retrospective.start()
                await self.set_retrospective(ctx, arg)
            else:    
                global retro_day
                retro_day = datetime.date(int(datetime.date.today().year), int(month), int(day))
                self.is_retrospective_eve.start()
                flag = 1
                await ctx.send(f'retrospectiva manualmente ajustada para a data {retro_day.day:02d}/{retro_day.month:02d}')

    # Command: Retrospectiva Ferias
    @commands.command(name="retro_ferias")
    async def set_retrospective_vacation(self, ctx):
        self.turn_off_retrospective.start()
        await ctx.reply("bot entrando de férias das retrospectivas! sem mais avisos ou afins.")

    # Internal Task: Desliga retro
    @tasks.loop(count=1)
    async def turn_off_retrospective(self):
        self.is_retrospective_eve.cancel()

    # Task: check if today is retrospective eve
    @tasks.loop(hours=1)
    async def is_retrospective_eve(self):
        global retro_day
        now = datetime.datetime.now(pytz.timezone('Brazil/East'))
        if retro_day == datetime.date.today() + datetime.timedelta(days=1):
            if now.hour == 15:
                self.remember_retrospective.start()
        if retro_day == datetime.date.today():
            if now.hour == 23:
                self.update_retro_day.start()

    # Task: send the warning to every petiane
    @tasks.loop(count=1)
    async def remember_retrospective(self):
        global RETRO_CHANNEL
        channel = self.bot.get_channel(RETRO_CHANNEL)
        await channel.send(f'atenção, {PETIANES}!\nlembrando que amanhã é dia de retrospectiva, já aproveitem pra escrever o textos de vocês.')

    # Task: set the retrospective day to 2 weeks later
    @tasks.loop(count=1)
    async def update_retro_day(self):
        global retro_day
        retro_day += datetime.timedelta(days=14)
        channel = self.bot.get_channel(RETRO_CHANNEL)
        await channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Retrospective(bot))
