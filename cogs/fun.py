import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
from discord.ext import commands


class fun:
    def __init__(self, bot):
       self.bot = bot
       
       
    @commands.command()
    async def hack(self, ctx, user: discord.Member):
        """Hack someone's account! Try it!"""
        msg = await ctx.send(f"Hacking! Target: {user}")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓    ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓▓   ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓▓▓▓ ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files COMPLETE! [▓▓▓▓▓▓]")
        await asyncio.sleep(2)
        await msg.edit(content="Retrieving Login Info... [▓▓▓    ]")
        await asyncio.sleep(3)
        await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓ ]")
        await asyncio.sleep(3)
        await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓▓ ]")
        await asyncio.sleep(4)
        await msg.edit(content=f"An error has occurred hacking {user}'s account. Please try again later. ❌")   
   
    
    @commands.command(aliases=['animation', 'a'])
    async def anim(self, ctx, Type):
        """Animations! Usage: *anim [type]. For a list, use *anim list."""
        if Type is None:
            await ctx.send('Probably a really cool animation, but we have not added them yet! But hang in there! You never know... For a current list, type *anim list')
        else:
            if Type.lower() == 'wtf':
              msg = await ctx.send("```W```")
              await asyncio.sleep(1)
              await msg.edit(content="```WO```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT D```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA F```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA FU```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA FUK```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA FUK!```")
              await asyncio.sleep(1)
              await msg.edit(content="WOT DA FUK!")
            elif Type.lower() == 'mom':
              msg = await ctx.send("```Y```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO M```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO MO```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO MOM```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO MOM!```")
              await asyncio.sleep(1)
              await msg.edit(content="YO MOM!")
            elif Type.lower() == 'gethelp':
              msg = await ctx.send("```STOP!```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! G```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Ge```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get s```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get so```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get som```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get some```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get some HELP```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get some HELP!!!```")
              await asyncio.sleep(1)
              await msg.edit(content="STOP! Get some HELP!!!")
            elif Type.lower() == 'sike':
              msg = await ctx.send("```W```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wa```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wai```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait.```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait..```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait...```")
              await asyncio.sleep(1)
              await msg.edit(content="```SIKE!```")
              await asyncio.sleep(1)
              await msg.edit(content="SIKE!")
            elif Type.lower() == 'gitgud':
              msg = await ctx.send("```G```")
              await asyncio.sleep(1)
              await msg.edit(content="```Gi```")
              await asyncio.sleep(1)
              await msg.edit(content="```Git```")
              await asyncio.sleep(1)
              await msg.edit(content="```Git GUD!```")
              await asyncio.sleep(1)
              await msg.edit(content="Git GUD!")
            elif Type.lower() == 'clock':
              msg = await ctx.send(":clock12:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock1230:") 
              await asyncio.sleep(1)
              await msg.edit(content=":clock1:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock130:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock2:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock230:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock3:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock330:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock4:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock430:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock5:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock530:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock6:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock630:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock7:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock730:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock8:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock830:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock9:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock930:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock10:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock1030:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock11:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock1130:")
              await asyncio.sleep(1)
              await msg.edit(content=":clock12:")
            elif Type.lower() == 'mate':
              msg = await ctx.send("```Y```")
              await asyncio.sleep(1)
              await msg.edit(content="```Ye```")
              await asyncio.sleep(1)
              await msg.edit(content="```Ye W```")
              await asyncio.sleep(1)
              await msg.edit(content="```Ye WO```")
              await asyncio.sleep(1)
              await msg.edit(content="```Ye WOT```")
              await asyncio.sleep(1)
              await msg.edit(content="```Ye WOT M8```")
              await asyncio.sleep(1)
              await msg.edit(content="```Ye WOT M8?!?!?!")
              await asyncio.sleep(1)
              await msg.edit(content="Ye WOT M8?!?!?!")
            elif Type.lower() == 'oj':
              msg = await ctx.send("```M```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mm```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm i```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm it```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm it'```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm it's```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm it's a```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm it's a ORANGE```")
              await asyncio.sleep(1)
              await msg.edit(content="```Mmm it's a ORANGE JUICE```")
              await asyncio.sleep(1)
              await msg.edit(content="Mmm it's a ORANGE JUICE")             
            elif Type.lower() == 'list':
              color = discord.Color(value=0x00ff00)
              em=discord.Embed(color=color, title="Current List of Awesome Animations:")
              em.description = "wtf (anim wtf), mom (anim mom), gethelp (anim gethelp), sike (anim sike), gitgud (anim gitgud), clock (anim clock), mate (anim mate), oj (anim oj)."
              em.set_footer(text="We will always be adding new animations!")
              await ctx.send(embed=em)
            else:
              await ctx.send('Probably a really cool animation, but we have not added them yet! But hang in there! You never know... For a current list, type *anim list')             
              
   
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, message:str):
        """Really desperate? Ask the 8ball for advice. Only yes/no questions!"""
        try:
            choices = ['It is certain. :white_check_mark:', 'It is decidedly so. :white_check_mark:', 'Without a doubt. :white_check_mark:', 'Yes, definitely. :white_check_mark:', 'You may rely on it. :white_check_mark:', 'As I see it, yes. :white_check_mark:', 'Most likely. :white_check_mark:', ' Outlook good. :white_check_mark:', 'Yes. :white_check_mark:', 'Signs point to yes. :white_check_mark:', 'Reply hazy, try again. :large_orange_diamond: ', 'Ask again later. :large_orange_diamond: ', 'Better not tell you now. :large_orange_diamond: ', 'Cannot predict now. :large_orange_diamond: ', 'Concentrate and ask again. :large_orange_diamond: ', 'Do not count on it. :x:', 'My reply is no. :x:', 'My sources say no. :x:', 'Outlook not so good. :x:', 'Very doubtful. :x:']
            color = discord.Color(value=0x00ff00)
            em = discord.Embed(color=color, title=f"{message}")
            em.description = random.choice(choices) 
            em.set_author(name="The Mighty 8 ball", icon_url="https://vignette.wikia.nocookie.net/battlefordreamislandfanfiction/images/5/53/8-ball_my_friend.png/revision/latest?cb=20161109021012")
            em.set_footer(text=f"Sent by {ctx.message.author.name}")
            await ctx.message.delete()
            await ctx.send(embed=em)
        except Forbidden:
            color = discord.Color(value=0xf44242)
            em = discord.Embed(color=color, title='Error ')
            em.description = 'Error code **{e.code}**: {e.error}'
            return await ctx.send(embed=em)



    @commands.command(aliases=['lf'])
    async def lifehack(self, ctx):
        """Learn a new way to hack life, one at a time."""
        choices = ["If you want to buy the cheapest airline tickets online, use your browser's incognito mode. Prices go up if you visit a site multiple times.", "An iPad charger will charge your iPhone much faster.", "Changing the font size of periods from 12 to 14 makes a paper look significantly longer.", "The harder you concentrate on falling asleep, the harder it is to actually fall asleep.", "Trucks drivers are always communicating with each other on the road. If you see one slow down for no reason, there's probably a cop ahead.", "Restaurant are required to give you free water.", "By peeing in the shower, you can save about 1157 gallons of water a year!", "Lick your wrist and smell it. This is what your breath smells like to others."]
        color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title="Life Hack")
        em.description = random.choice(choices) 
        em.set_footer(text="Source: Crumblyy")
        await ctx.send(embed=em)

        
    
def setup(bot): 
    bot.add_cog(fun(bot))   

