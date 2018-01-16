import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class mod:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def dm(self, ctx, user: discord.Member, *, msg: str):
        """Escort your DM to someone thru the bot. Usage: *dm [tag person] [msg]"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("SuccESS! Your DM has made it! :white_check_mark: ")
        except:
            await ctx.send("Error :x:. Make sure your message is shaped in this way: *dm [tag person] [msg]")
    
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def warn(self, ctx, user: discord.Member, *, reason: str):
        """It's time to stop. Sends that warning. Usage: *warn [tag person] [reason]"""
        try:
            color = discord.Color(value=0xf44242)
            em = discord.Embed(color=color, title=f"WARNING: by {ctx.message.author.name} from **{ctx.author.guild.name}**.", description=f"{reason}")
            await user.send(embed=em)
            await ctx.message.delete()
            await ctx.send("User has been DM'd :white_check_mark:. Pray that the user is a gud boi now. :pray:")
        except:
            await ctx.send("Something happened and the DM could not make it :x:. The user could be blocking DMs from the server, or you did not use the format correctly. Usage: *warn [tag person] [reason].")    
       
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, num: int):
        """Deletes a # of msgs. *purge [# of msgs].""" 
        try: 
            await ctx.channel.purge(limit=num+1)
            await ctx.send("Purged successfully :white_check_mark:")
        except:
            await ctx.send("Purge unsuccessful. That must be an invalid number, or you/the bot do not have Manage Msgs permission.")
    
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member):
        """Kicks a member into the world outside your server."""
        await ctx.channel.send(f"Be gone {user.name}! Oh, and close the door on the way out :door:.")
        await user.kick()
        
        
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member):
        """Swings the mighty Ban Hammer on that bad boy."""
        await ctx.channel.send(f"The ban hammer has fallen. And it has struck {user.name}.")
        await user.ban()



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def mute(self, ctx, user: discord.Member, time: int):
        '''Forces someone to shut up. Usage: *mute [user] [time in mins]'''
        if time is None:
            await ctx.guild.set_permissions(user, send_messages=False)
            await ctx.channel.send(f"{user.mention} is now forced to shut up. :zipper_mouth: ")
        else:
            try:
                time = time * 60
                float(time)
            except:
                return await ctx.send("Your time is an invalid number. Make sure...it is a number.")
            await ctx.guild.set_permissions(user, send_messages=False)
            await ctx.channel.send(f"{user.mention} is now forced to shut up. :zipper_mouth: ")
            await asyncio.sleep(time)
            await ctx.guild.set_permissions(user, send_messages=True)
            await ctx.channel.send(f"{user.mention} is now un-shutted up.")
        except discord.Forbidden:
            return await ctx.send("I could not mute the user. Make sure I have the manage channels permission.")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unmute(self, ctx, user: discord.Member):
        '''Allows someone to un-shut up. Usage: *unmute [user]'''
        if user is None:
            await ctx.send("Dang. You must enter a user to un-shut them up!")
        else:
            await ctx.guild.set_permissions(user, send_messages=True)
            await ctx.channel.send(f"{user.mention} is now un-shutted up.")
        
        
    @commands.command()
    async def serverinfo(self, ctx):
        """Are you a nerd? Here's some server info."""
        guild = ctx.guild
        roles = [x.name for x in guild.roles]
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at.strftime("%b %m, %Y, %A, %I:%M %p"))         
        em = discord.Embed(description= "-", title='Server Info', colour=0x00ff00)
        em.set_thumbnail(url=guild.icon_url)
        em.add_field(name='__Server __', value=str(guild.name))
        em.add_field(name='__Server ID__', value=str(guild.id))
        em.add_field(name='__Owner__', value=str(guild.owner))
        em.add_field(name='__Owner ID__', value=guild.owner_id) 
        em.add_field(name='__Member Count__', value=str(guild.member_count))
        em.add_field(name='__Text/Voice Channels__', value=str(channels))
        em.add_field(name='__Server Region__', value='%s' % str(guild.region))
        em.add_field(name='__ Total Roles__', value='%s' % str(role_length))
        em.add_field(name='__Roles__', value='%s' % str(roles))
        em.set_footer(text='Created - %s' % time)        
        await ctx.send(embed=em)
        
        
def setup(bot): 
    bot.add_cog(mod(bot))        
