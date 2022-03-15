import utils.utils as utils
import discord
import random
from decouple import config
from discord.ext import commands


# Constants
MATHEUS = config("MATHEUS_ID")


# Get swearings from file
data = utils.read_file('data/data.json')
offense_list = data['offenses']
praise_list = data['praises']


class Offenses(commands.Cog):
    """Offense commands against Matheus"""

    def __init__(self, bot):
        self.bot = bot

    # Command: Xingar Matheus
    @commands.command(name="xingar_matheus", help="não é necessário gastar sua saliva xingando o Matheus, o bot faz isso por você")
    async def offend_matheus(self, ctx):
        num = random.randint(0, len(offense_list))
        await ctx.send(f'{offense_list[num]}, {MATHEUS}')   


    # Command: Adicionar xingamento
    @commands.command(name="add_xingamento", help="adicione uma nova forma de ofender o Matheus!")
    async def add_offense(self, ctx, *args):
        message = ' '.join(args).lower()
        if message == '':
            await ctx.reply("não esqueça de escrever o xingamento a ser adicionado!")
        else:
            if message in offense_list:
                await ctx.reply("esse xingamento já está na lista.")   
            else:
                offense_list.append(message)
                utils.add_new_item_to_dict(offense_list, praise_list)
                await ctx.send(f'"{message}" foi adicionado à lista!')


    # Command: Remover xingamento
    @commands.command(name="rem_xingamento", help="não gostou de algum xingamento? ele nunca mais será usado")
    async def remove_offense(self, ctx, *args):
        swear_to_be_removed = ' '.join(args).lower()
        if swear_to_be_removed in offense_list:
            offense_list.remove(swear_to_be_removed)
            utils.add_new_item_to_dict(offense_list, praise_list)
            await ctx.send(f'"{swear_to_be_removed}" foi removido da lista!')
        else:
            await ctx.send(f'esse xingamento não existe')


    # Command: Mostrar xingamentos
    @commands.command(name="xingamentos", help="lista todas as formas possíveis de ofender o Matheus")
    async def show_offenses(self, ctx):
        printable_offense_list = ', '.join(offense_list).lower()
        embed = discord.Embed(color=0xFF6347)
        embed.add_field(
            name="**Lista de xingamentos:**",
            value=f'{printable_offense_list}'
        )
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Offenses(bot))
