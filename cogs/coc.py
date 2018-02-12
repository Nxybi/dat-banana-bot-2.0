import discord
import sys
import os
import io
import json
import aiohttp
import ezjson
from discord.ext import commands


class coc:
    def __init__(self, bot):
        self.bot = bot
        with open('data/apikeys.json') as f:
            lol = json.load(f)
            self.token = lol.get("cocapi")
        self.client = {'Authorization': self.token}



    @commands.command()
    async def cocsave(self, ctx, coctag=None):
        '''Saves a Clash of Clans tag to your Discord account.'''
        if coctag is None:
            return await ctx.send('Oops! Enter a tag to save! Usage: *cocsave [tag]')
        coctag = coctag.strip('#')
        for char in coctag:
            if char.upper() not in '0289PYLQGRJCUV':
                return await ctx.send(f'Oops again! Looks like your tag `#{coctag}` is not a valid tag!')
        ezjson.dump("data/coctags.json", ctx.author.id, coctag)
        await ctx.send("Success. :white_check_mark: Your tag is now saved to your account.")



    @commands.command()
    async def cocprofile(self, ctx, coctag=None):
        '''Gets a Clash of Clans profile! Yay!'''
        if coctag is None:
            try:
                with open('data/coctags.json') as f:
                    lol = json.load(f)
                    userid = str(ctx.author.id)
                    coctag = lol[userid]
            except KeyError:
                return await ctx.send("Oops, looks like you don't have a saved tag yet! Use `*cocsave [tag]` to save your tag to your Discord profile.")              
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.clashofclans.com/v1/players/%23{coctag}', headers=self.client) as resp:
                    resp = await resp.json()
                    color = discord.Color(value=0xe5f442)
                    em = discord.Embed(color=color, title=f"{resp['name']}, {resp['tag']}")
                    em.add_field(name='XP Level', value=resp['expLevel'])
                    em.add_field(name='Trophies', value=resp['trophies'])
                    try:
                        leaguename = resp['league']['name']
                    except KeyError:
                        leaguename = 'Unranked'
                    em.add_field(name='League', value=leaguename)
                    em.add_field(name='Best Trophies', value=resp['bestTrophies'])
                    em.add_field(name='Town Hall', value=resp['townHallLevel'])
                    em.add_field(name='Attack Wins', value=resp['attackWins'])
                    em.add_field(name='Defense Wins', value=resp['defenseWins'])
                    em.add_field(name='Donations', value=resp['donations'])
                    em.add_field(name='Donations Received', value=resp['donationsReceived'])
                    em.add_field(name='War Stars', value=resp['warStars'])
                    try:
                        em.set_thumbnail(url=resp['league']['iconUrls']['medium'])
                    except KeyError:
                        em.set_thumbnail(url='http://clash-wiki.com/images/progress/leagues/no_league.png')
                    em.set_author(name='Normal Base')
                    await ctx.send(embed=em)
                    try:
                        em = discord.Embed(color=discord.Color(value=0xe5f442))
                        em.add_field(name='Builder Hall', value=resp['builderHallLevel'])
                        em.add_field(name='Trophies', value=resp['versusTrophies'])
                        em.add_field(name='Personal Best', value=resp['bestVersusTrophies'])
                        em.add_field(name='Attack Wins', value=resp['versusBattleWins'])
                        em.set_author(name='Builder Base')
                        await ctx.send(embed=em)
                    except KeyError:
                        em = discord.Embed(color=discord.Color(value=0xe5f442))
                        em.description = 'Builder Base is not unlocked yet! Hit Town Hall 4 to unlock.'
                        em.set_author(name='Builder Base')
                        await ctx.send(embed=em)
                    color = discord.Color(value=0xe5f442)
                    try:
                        em = discord.Embed(color=color, title=f"{resp['clan']['name']}, {resp['clan']['tag']}")
                        em.add_field(name='Clan Level', value=resp['clan']['clanLevel'])                            
                        types = {
                            'member': 'Member',
                            'admin': 'Elder',
                            'coLeader': 'Co-Leader',
                            'leader': 'Leader'
                        }
                        em.add_field(name='Clan Role', value=types[resp['role']])
                        em.set_author(name='Clan Info')
                        em.set_thumbnail(url=resp['clan']['badgeUrls']['medium'])
                        await ctx.send(embed=em)
                    except KeyError:
                        em = discord.Embed(color=color, title="No Clan")
                        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/388146146029076480/405548101370380291/maxresdefault.jpg')
                        await ctx.send(embed=em)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.clashofclans.com/v1/players/%23{coctag}', headers=self.client) as resp:
                    resp = await resp.json()
                    color = discord.Color(value=0xe5f442)
                    em = discord.Embed(color=color, title=f"{resp['name']}, #{resp['tag']}")
                    em.add_field(name='XP Level', value=resp['expLevel'])
                    em.add_field(name='Trophies', value=resp['trophies'])
                    try:
                        leaguename = resp['league']['name']
                    except KeyError:
                        leaguename = 'Unranked'
                    em.add_field(name='League', value=leaguename)
                    em.add_field(name='Best Trophies', value=resp['bestTrophies'])
                    em.add_field(name='Town Hall', value=resp['townHallLevel'])
                    em.add_field(name='Attack Wins', value=resp['attackWins'])
                    em.add_field(name='Defense Wins', value=resp['defenseWins'])
                    em.add_field(name='Donations', value=resp['donations'])
                    em.add_field(name='Donations Received', value=resp['donationsReceived'])
                    em.add_field(name='War Stars', value=resp['warStars'])
                    try:
                        em.set_thumbnail(url=resp['league']['iconUrls']['medium'])
                    except KeyError:
                        em.set_thumbnail(url='http://clash-wiki.com/images/progress/leagues/no_league.png')
                    em.set_author(name='Normal Base')
                    await ctx.send(embed=em)
                    try:
                        em = discord.Embed(color=discord.Color(value=0xe5f442))
                        em.add_field(name='Builder Hall', value=resp['builderHallLevel'])
                        em.add_field(name='Trophies', value=resp['versusTrophies'])
                        em.add_field(name='Personal Best', value=resp['bestVersusTrophies'])
                        em.add_field(name='Attack Wins', value=resp['versusBattleWins'])
                        em.set_author(name='Builder Base')
                        await ctx.send(embed=em)
                    except KeyError:
                        em = discord.Embed(color=discord.Color(value=0xe5f442))
                        em.description = 'Builder Base is not unlocked yet! Hit Town Hall 4 to unlock.'
                        em.set_author(name='Builder Base')
                        await ctx.send(embed=em)
                    color = discord.Color(value=0xe5f442)
                    try:
                        em = discord.Embed(color=color, title=f"{resp['clan']['name']}, {resp['clan']['tag']}")
                        em.add_field(name='Clan Level', value=resp['clan']['clanLevel'])                            
                        types = {
                            'member': 'Member',
                            'admin': 'Elder',
                            'coLeader': 'Co-Leader',
                            'leader': 'Leader'
                        }
                        em.add_field(name='Clan Role', value=types[resp['role']])
                        em.set_author(name='Clan Info')
                        em.set_thumbnail(url=resp['clan']['badgeUrls']['medium'])
                        await ctx.send(embed=em)
                    except KeyError:
                        em = discord.Embed(color=color, title="No Clan")
                        em.set_thumbnail(url='http://i1253.photobucket.com/albums/hh599/bananaboy21/maxresdefault_zpseuid4jln.jpg')
                        await ctx.send(embed=em)


    @commands.command()
    async def cocclan(self, ctx, clantag=None):
        """Gets clan info for a Clash of Clans clan."""
        if clantag is None:
            try:
                with open('data/coctags.json') as f:
                    lol = json.load(f)
                    userid = str(ctx.author.id)
                    coctag = lol[userid]
            except KeyError:
                return await ctx.send("Oops, looks like you don't have a saved tag yet! Use `*cocsave [tag]` to save your tag to your Discord profile.")
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.clashofclans.com/v1/players/%23{coctag}', headers=self.client) as resp:
                    resp = await resp.json()
                    try:
                        clantag = resp['clan']['tag']
                        clantag = clantag.strip('#')
                    except KeyError:
                        return await ctx.send("Oops! You aren't in a clan yet. \nTo search for a clan by clan tag, use `*cocclan [clan tag]`.")
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.clashofclans.com/v1/clans/%23{clantag}', headers=self.client) as respclan:
                    clan = await respclan.json()
                    color = discord.Color(value=0xe5f442)
                    em = discord.Embed(color=color, title='Clan Info')
                    em.add_field(name='Location', value=clan.get('location', {}).get('name'))
                    em.add_field(name='Clan Level', value=clan.get('clanLevel', 0))
                    em.add_field(name='Clan Points - Home Base', value=clan.get('clanPoints', 0))
                    em.add_field(name='Clan Points - Builder Base', value=clan.get('clanVersusPoints', 0))
                    clanmembers = clan.get('members', 0)
                    em.add_field(name='Members', value=f'{clanmembers}/50')
                    em.add_field(name='Required Trophies', value=clan.get('requiredTrophies', 0))
                    em.add_field(name='War Frequency', value=clan.get('warFrequency', 0))
                    em.add_field(name='War Win Streak', value=clan.get('warWinStreak', 0))
                    em.add_field(name='War Wins', value=clan.get('warWins', 0))
                    em.add_field(name='War Draws', value=clan.get('warTies', 0))
                    em.add_field(name='War Losses', value=clan.get('warLosses', 0))
                    if clan['isWarLogPublic'] is True:
                        warlog = 'Public'
                    else:
                        warlog = 'Private'
                    em.add_field(name='War Log', value=warlog)
                    em.set_author(name=f"{clan.get('name', '[Unknown Name]')} ({clan.get('tag', '[Unknown Tag]')})")
                    em.set_thumbnail(url=clan['badgeUrls']['medium'])
                    await ctx.send(embed=em)
        else:
            clantag = clantag.strip('#')
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.clashofclans.com/v1/clans/%23{clantag}', headers=self.client) as respclan:
                    clan = await respclan.json()
                    color = discord.Color(value=0xe5f442)
                    em = discord.Embed(color=color, title='Clan Info')
                    em.add_field(name='Location', value=clan.get('location', {}).get('name'))
                    em.add_field(name='Clan Level', value=clan.get('clanLevel', 0))
                    em.add_field(name='Clan Points - Home Base', value=clan.get('clanPoints', 0))
                    em.add_field(name='Clan Points - Builder Base', value=clan.get('clanVersusPoints', 0))
                    clanmembers = clan.get('members', 0)
                    em.add_field(name='Members', value=f'{clanmembers}/50')
                    em.add_field(name='Required Trophies', value=clan.get('requiredTrophies', 0))
                    em.add_field(name='War Frequency', value=clan.get('warFrequency', 0))
                    em.add_field(name='War Win Streak', value=clan.get('warWinStreak', 0))
                    em.add_field(name='War Wins', value=clan.get('warWins', 0))
                    em.add_field(name='War Draws', value=clan.get('warTies', 0))
                    em.add_field(name='War Losses', value=clan.get('warLosses', 0))
                    if clan['isWarLogPublic'] is True:
                        warlog = 'Public'
                    else:
                        warlog = 'Private'
                    em.add_field(name='War Log', value=warlog)
                    em.set_author(name=f"{clan.get('name', '[Unknown Name]')} ({clan.get('tag', '[Unknown Tag]')})")
                    em.set_thumbnail(url=clan['badgeUrls']['medium'])
                    await ctx.send(embed=em)

def setup(bot): 
    bot.add_cog(coc(bot)) 


						







