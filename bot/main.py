import discord
import random
import asyncio
from discord.ext import commands
#from discord.ext import guild

token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
    	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name ="Evil's code"))
    	print('online')
    	print('connected to client{}'.format(client.user.id))
    	

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.upper().startswith('VERIFY'):
            answer = random.randint(1000, 9999)
            await message.channel.send('> Your verification code is {}''\n''> RE ENTER YOUR VERIFICATION CODE HERE '.format(answer))
#            await message .channel.send('> RE ENTER YOUR VERIFICATION CODE ')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
                

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=40.0)
            except asyncio.TimeoutError:
                return await message.channel.send('> {} Sorry, you took too long .type verify again '.format(message.author.mention))
                

            if int(guess.content) == answer:

            	role = discord.utils.get(message.guild.roles, name='verified')
            	await message.author.add_roles(role)
            	await message.channel.send('>  CONGO VERIFIED SUCCESS FULLY!')
            	await message.channel.purge(limit=9)
            	await message.channel.send('SIMPLY TYPE VERIFY TO GET YOUR VERIFICATION CODE')
            	
            
            else:
                await message.channel.send('> ENTERED WRONG CODE .THE CODE WAS{}.'.format(answer))
                await message.channel.purge(limit=9)
                await message.channel.send('SIMPLY TYPE VERIFY TO GET YOUR VERIFICATION CODE')


client = MyClient()
client.run(token)
