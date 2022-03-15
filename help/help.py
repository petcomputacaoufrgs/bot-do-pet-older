import discord
from decouple import config
from discord.ext import commands


# CONSTANTS
BOT_RECOMMENDATIONS_CHANNEL = config("BOT_RECOMMENDATIONS_CHANNEL")

class Help(commands.Cog):
    """Reworked help commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title="**Bem-vinde ao Bot do PET!**",
            url="https://github.com/petcomputacaoufrgs/bot-do-pet",
            description="Use `pet.help <comando>` para ter mais informações sobre seu uso.",
            color=0xFFFFFF
        )
        em.add_field(
            name="**Xingue o Matheus:**",
            value="""
                *pet.xingar_matheus*
                *pet.add_xingamento*
                *pet.rem_xingamento*
                *pet.xingamentos*
                """,
            inline=True
        )
        em.add_field(
            name="**Demonstre seu carinho:**",
            value="""
                *pet.elogiar*
                *pet.add_elogio*
                *pet.rem_elogio*
                *pet.elogios*
                *pet.hug*
                """,
            inline=True
        )
        em.add_field(
            name="**Retrospectiva:**",
            value="""
                *pet.retro*
                *pet.retro_manual*
                *pet.retro_ferias*
                """,
            inline=True
        )
        em.add_field(
            name="⠀",
            value="⠀",
            inline=False
        )
        em.add_field(
            name="**Interpet:**",
            value="""
                *pet.inter*
                *pet.inter_manual*
                *pet.inter_ferias*
                """,
            inline=True
        )
        em.add_field(
            name="**Liderança:**",
            value="""
                *pet.lideres*
                """,
            inline=True
        )
        em.add_field(
            name="**Evento:**",
            value="""
                *pet.aviso*
                *pet.aviso_atual*
                """,
            inline=True
        )
        em.add_field(
            name="⠀",
            value="⠀",
            inline=False
        )
        em.add_field(
            name="**Tem alguma outra sugestão para o bot?**",
            value=f'Escreva pra gente no chat <#{BOT_RECOMMENDATIONS_CHANNEL}>! Toda ajuda é sempre bem-vinda  🥰',
            inline=False
        )
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/938858934259822685/945718556732039219/LogoPET_oficial.png")
        await ctx.send(embed = em)

    @help.command()
    async def xingar_matheus(self, ctx):  
        em = discord.Embed(
            title="**Comando: xingar o Matheus**",
            description="Não é necessário gastar sua saliva xingando o Matheus, o bot faz isso por você.",
            color=0xFF6347
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.xingar_matheus```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def add_xingamento(self, ctx):  
        em = discord.Embed(
            title="**Comando: adicionar xingamento**",
            description="Adicione uma nova forma de ofender o Matheus!",
            color=0xFF6347
        )
        em.add_field(
            name="**Argumentos:**",
            value="O xingamento a ser adicionado na lista, sem aspas.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.add_xingamento <xingamento goes here>```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def rem_xingamento(self, ctx):  
        em = discord.Embed(
            title="**Comando: remover xingamento**",
            description="Não gostou de algum xingamento? Ele nunca mais será usado!",
            color=0xFF6347
        )
        em.add_field(
            name="**Argumentos:**",
            value="O xingamento a ser removido da lista, sem aspas.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.rem_xingamento <xingamento goes here>```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def xingamentos(self, ctx):  
        em = discord.Embed(
            title="**Comando: listar xingamentos**",
            description="Lista todas as formas possíveis de ofender o Matheus.",
            color=0xFF6347
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.xingamentos```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def elogiar(self, ctx):  
        em = discord.Embed(
            title="**Comando: elogiar**",
            description="Elogie alguém que fez um bom trabalho recentemente!",
            color=0x9370DB
        )
        em.add_field(
            name="**Argumentos:**",
            value="Escreva o @ da pessoa a ser elogiada.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.elogiar @someone```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def add_elogio(self, ctx):  
        em = discord.Embed(
            title="**Comando: adicionar elogio**",
            description="Adicione mais uma forma de reconhecermos o bom trabalho dos nossos coleguinhas.",
            color=0x9370DB
        )
        em.add_field(
            name="**Argumentos:**",
            value="O elogio a ser adicionado na lista, sem aspas.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.add_elogio <elogio goes here>```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def rem_elogio(self, ctx):  
        em = discord.Embed(
            title="**Comando: remover elogio**",
            description="Não gostou de algum elogio? Não usaremos mais.",
            color=0x9370DB
        )
        em.add_field(
            name="**Argumentos:**",
            value="O elogio a ser removido da lista, sem aspas.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.rem_elogio <elogio goes here>```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def elogios(self, ctx):  
        em = discord.Embed(
            title="**Comando: listar elogios**",
            description="Lista todas as formas de elogiar os outros.",
            color=0x9370DB
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.elogios```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def hug(self, ctx):  
        em = discord.Embed(
            title="**Comando: abraçar**",
            description="Demonstre seu carinho por alguém.",
            color=0x9370DB
        )
        em.add_field(
            name="**Argumentos:**",
            value="Escreva o @ da pessoa a ser abraçada.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.hug @someone```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def retro(self, ctx):  
        em = discord.Embed(
            title="**Comando: mostrar próxima retrospectiva**",
            description="Avisa quantos dias faltam pra retrospectiva.",
            color=0xF0E68C
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.retro```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def retro_manual(self, ctx):  
        em = discord.Embed(
            title="**Comando: settar a próxima retrospectiva**",
            description="Seta a nova data para a retrospectiva.",
            color=0xF0E68C
        )
        em.add_field(
            name="**Argumentos:**",
            value="A data no formato dd/mm.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.retro_manual <dia/mes>```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def retro_ferias(self, ctx):  
        em = discord.Embed(
            title="**Comando: férias da retrospectiva**",
            description="Desliga os avisos de retrospectiva.",
            color=0xF0E68C
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.retro_ferias```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def inter(self, ctx):  
        em = discord.Embed(
            title="**Comando: mostrar próximo interpet**",
            description="Avisa quantos dias faltam pra interpet.",
            color=0x98FB98
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.inter```",
            inline=False
        )
        await ctx.send(embed = em)


    @help.command()
    async def inter_manual(self, ctx):  
        em = discord.Embed(
            title="**Comando: settar o próximo interpet**",
            description="Seta a nova data para o interpet.",
            color=0x98FB98
        )
        em.add_field(
            name="**Argumentos:**",
            value="A data no formato dd/mm.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.inter_manual <dia/mes>```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def inter_ferias(self, ctx):  
        em = discord.Embed(
            title="**Comando: férias do interpet**",
            description="Desliga os avisos do interpet.",
            color=0x98FB98
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.inter_ferias```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def lideres(self, ctx):  
        em = discord.Embed(
            title="**Comando: líderes**",
            description="Saiba quem manda no PET nesse mês.",
            color=0xFDFD96
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.lideres```",
            inline=False
        )
        await ctx.send(embed = em)

    @help.command()
    async def aviso(self, ctx):  
        em = discord.Embed(
            title="**Comando: aviso**",
            description="Use para criar um aviso 100% personalizável.",
            color=0xBDECB6
        )
        em.add_field(
            name="**Argumentos:**",
            value="Serão 4 etapas para a criação do aviso e cada uma tem seus próprios argumentos, sendo eles: o nome, quando, quem pingar e onde mandar.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="1ª chamada: ```pet.aviso```\n2ª chamada: ```pet.aviso <nome do aviso>```\n3ª chamada: ```pet.aviso <tempo até o aviso acontecer> ou <dd/mm/aaaa>```\n4ª chamada: ```pet.aviso <@pessoa 1> <@pessoa 2> ... <@pessoa n>```\n5ª chamada: ```pet.aviso <#nome do canal>```",
            inline=False
        )
        await ctx.send(embed = em)
    
    @help.command()
    async def aviso_atual(self, ctx):
        em = discord.Embed(
            title="**Comando: aviso atual**",
            description="Use para checar se há um aviso já criado e, caso haja, use para obter um resumo sobre ele.",
            color=0xBDECB6
        )
        em.add_field(
            name="**Argumentos:**",
            value="Nenhum, use apenas a chamada para o comando.",
            inline=False
        )
        em.add_field(
            name="**Exemplo de uso:**",
            value="```pet.aviso_atual```",
            inline=False
        )
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Help(bot))
