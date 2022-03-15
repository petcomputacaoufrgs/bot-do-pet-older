import utils.utils as utils
import datetime
import discord
from decouple import config
from discord.ext import commands, tasks


#Constants
PETIANES = config("PETIANES_ID")
LEADERSHIP_CHANNEL = config("LEADERSHIP_CHANNEL")
leadership = utils.read_file("data/leadership.json")
months_names = {
  "1": "Janeiro",
  "2": "Fevereiro",
  "3": "Março",
  "4": "Abril",
  "5": "Maio",
  "6": "Junho",
  "7": "Julho",
  "8": "Agosto",
  "9": "Setembro",
  "10": "Outubro",
  "11": "Novembro",
  "12": "Dezembro",
}


class Leadership(commands.Cog):
    """PET Computação leadership commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.is_first_day_of_month.start()

    @commands.command(name="lideres")
    async def month_leadership(self, ctx):
        global leadership
        current_month = datetime.date.today().month
        current_leadership = leadership[f'{current_month}']
        em = discord.Embed(
            title=f"**Liderança:**",
            description=f"Neste mês de {months_names[f'{current_month}'].lower()}, o líder é **{current_leadership[0]}** e o vice é **{current_leadership[1]}**.\n\nPara os próximos meses:",
            color=0xFDFD96
        )
        for month in leadership:
            if int(month) > int(datetime.date.today().month):
                next_leadership = leadership[f'{month}']
                em.add_field(
                    name=f"**{months_names[month]}**",
                    value=f"Líder: {next_leadership[0]}\nVice: {next_leadership[1]}",
                    inline=False
                )
        await ctx.reply(embed = em)

    @tasks.loop(hours=24)
    async def is_first_day_of_month(self):
        if datetime.date.today().day == 1:
            self.disclose_leadership.start()

    @tasks.loop(count=1)
    async def disclose_leadership(self):
        channel = self.bot.get_channel(int(LEADERSHIP_CHANNEL))
        data = utils.read_file("data.leadership.json")
        leadership = data[f'{datetime.date.today().month}']
        await channel.send(f'atenção, {PETIANES}!\nesse mês nosso ditador e vice ditador passam a ser {leadership[0]} e {leadership[1]}')

def setup(bot):
    bot.add_cog(Leadership(bot))
