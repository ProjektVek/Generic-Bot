import discord #importing discord library
import os #importing .env files

client = discord.Client() #Declaring the client

@client.event #Action performed on client events
async def on_ready(): #Assincronuos Function (Declared by 'def') that will execute when the bot is ready
  print('We Have Logged in as {0.user}'.format(client)) #0 will get override by 'client'; This will get the bot name

@client.event #Triggers when is a client event
async def on_message(message): #will triggers when a message is received, and the message will be receveid as parameter
  if message.author == client.user: #if the message is from this bot, will be ignored
    return
  
  if message.content.startswith('$hello'): #whenever the message starts with "$hello"
    await message.channel.send('Hello') #Will send a message Hello
  
client.run(os.getenv('TOKEN')) #Running the bot