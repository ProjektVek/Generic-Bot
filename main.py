import discord #Importing Discord.py
import os #Importing .env
import requests #allows http requests
import json #for work with json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client() #Registering Discord Client

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing'] #List of word that will be detected

start_encouragements = [ #List of encouragement phrases
    'Cheer up!',
    'Hang in there',
    'You are a great person!'
]

if "responding" not in db.keys(): #creating responding key
    db["responding"] = True

#function to insert new encouragement
def update_encouragements(encouraging_message): 
    if "encouragements" in db.keys(): #If "encouragements" is a database key
        encouragements = db["encouragements"] #receives all encouragements from database
        encouragements.append(encouraging_message) #insert encouraging message in database
        db["encoragements"] = encouragements #update database
    else:
        db["encouragements"] = [encouraging_message] #creates the "encouragement in the database"

#function to delete encouragement
def delete_encouragement(index):
    encouragements = db["encouragements"] #getting encouragements from db
    if len(encouragements) > index: #if the index is valid
        del encouragements[index] #delete the message in the defined index
        db["encouragements"] = encouragements #update database

#function to get quotes from API
def get_quote(): 
    response = requests.get("https://zenquotes.io/api/random") #Getting random quote from API zenquotes
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

@client.event #Using Client to Register a Event
async def on_ready(): #Declaring function on_ready; Will be triggered when bot is started
    print('We have logged in as {0.user}'.format(client)) #0 gets substituted by "client"

@client.event #This will triggers whenever that is a client event
async def on_message(message):
    if message.author == client.user: #If the message is from this bot, do nothing
        return

    msg = message.content

    if message.content.startswith('$hello'): #Whenever the message starts with "hello"
        await message.channel.send('Hello!') #Tries to send the message hello

    if message.content.startswith('$inspire'): #return a inspiritional quote from api
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        #Looking for all encouragement phrases
        options = start_encouragements
        if msg.startswith('report db'): #if report db was typed, it will report db search state
            await message.channel.send('Looking in db...')
        if "encouragements" in db.keys(): #if there are messages in database
            options += db["encouragements"] #add this messages
            if msg.startswith('report db'):
                await message.channel.send('found')
                await message.channel.send('Messages:\n{}'.format(options))

    if any(word in msg for word in sad_words): #if it finds a "sad_word" in the message
        await message.channel.send(random.choice(options)) #send a encouragement message

    #Add new messages
    if msg.startswith('$new'): #if message starts with "$new"
        encouraging_message = msg.split('$new',1)[1] #get the message
        update_encouragements(encouraging_message)
        await message.channel.send('New encouraging message added: ' + encouraging_message)

    #deleting messages in db
    if msg.startswith('$del'): #if message starts with "$del"
        encouragements = [] #creating new list
        if "encouragements" in db.keys():
            index = int(msg.split('$del ',1)[1]) #getting the index
            delete_encouragement(index) #deleting message
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    #getting list of encouragements
    if msg.startswith('$list'):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    #switching respond on and off
    if msg.startswith('$responding'): #the command starts with $responding
        value = msg.split('$responding',1)[1]

        if value.lower() == 'true': #if value equals true: turn response on
            db["responding"] = True
            await message.channel.send("Responding is on")
        if value.lower() == 'false': #if value equals false: turn response off
            db["responding"] = False
            await message.channel.send("Responding is off")  

    #if message.content.startswith('print json'): #Sends Json text
    #    await message.channel.send('{}'.format(get_quote()))
keep_alive()   

token = os.environ['TOKEN']
client.run(token) #Running the bot