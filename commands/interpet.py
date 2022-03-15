import datetime
import pytz
import utils.utils as utils
from dateutil.relativedelta import relativedelta
from decouple import config
from discord.ext import commands, tasks


# Constants
PETIANES = config("PETIANES_ID")
INTERPET_CHANNEL = config("INTERPET_CHANNEL")


flag = 1
interpet_day = utils.initialize_date(datetime.date(2022, 2, 19), 30)


class Interpet(commands.Cog):
    """Commands about the monthly interpet meeting"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.is_interpet_eve.start()

    # Command: Interpet
    @commands.command(name="inter")
    async def interpet(self, ctx):
        days_to_interpet = interpet_day - datetime.date.today()   
        if days_to_interpet.days < 2:
            if days_to_interpet.days == 1:
                await ctx.reply(f'falta {days_to_interpet.days} dia até o próximo interpet, que será no dia {interpet_day.day:02d}/{interpet_day.month:02d}.')
            if days_to_interpet.days == 0:
                await ctx.reply("hoje é o dia do interpet! corre pra não perder a reunião.")
            else:
                await ctx.send("erro na data do interpet")
        else:
            await ctx.reply(f'faltam {days_to_interpet.days} dias até o próximo interpet, que será no dia {interpet_day.day:02d}/{interpet_day.month:02d}.')

    # Command: Interpet Manual    
    @commands.command(name="inter_manual")
    async def set_interpet(self, ctx, arg):
        day, month = arg.split('/')
        if int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12:
            await ctx.reply("informe uma data válida.")
        elif (datetime.date(int(datetime.date.today().year), int(month), int(day)) - datetime.date.today()).days < 0:
            await ctx.reply("informe uma data válida.")        
        else:
            global flag
            if flag == 1:
                flag = 0
                await self.turn_off_interpet.start()
                await self.set_interpet(ctx, arg)
            else:    
                global interpet_day
                interpet_day = datetime.date(int(datetime.date.today().year), int(month), int(day))
                self.is_interpet_eve.start()
                flag = 1
                await ctx.send(f'interpet manualmente ajustado para a data {interpet_day.day:02d}/{interpet_day.month:02d}')

    # Command: Interpet Ferias
    @commands.command(name="inter_ferias")
    async def set_interpet_vacation(self, ctx):
        self.turn_off_interpet.start()
        await ctx.reply("bot entrando de férias do interpet! sem mais avisos ou afins.")   

    # Internal Task: Desliga interpet
    @tasks.loop(count=1)
    async def turn_off_interpet(self):
        self.is_interpet_eve.cancel()
    
    # Task: check if today is interpet eve
    @tasks.loop(hours=1)
    async def is_interpet_eve(self):
        global interpet_day
        now = datetime.datetime.now(pytz.timezone('Brazil/East'))
        if interpet_day == datetime.date.today() + datetime.timedelta(days=1):
            if now.hour == 13:
                self.remember_interpet.start()
        if interpet_day == datetime.date.today():
            if now.hour == 23:
                self.update_interpet_day.start()

    # Task: send the warning to every petiane
    @tasks.loop(count=1)
    async def remember_interpet(self):
        global interpet_day
        channel = self.bot.get_channel(int(INTERPET_CHANNEL))
        await channel.send(f'atenção, {PETIANES}!\nlembrando que amanhã é dia de interpet, estejam acordados amanhã de manhã!')         

    # Task: set the interpet day to 1 month later
    @tasks.loop(count=1)
    async def update_interpet_day(self):
        global interpet_day
        interpet_day += relativedelta(months=1)
        channel = self.bot.get_channel(int(INTERPET_CHANNEL))
        await channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Interpet(bot))
