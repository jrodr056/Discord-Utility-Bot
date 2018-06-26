import discord
import random, os
from random import randint
import logging
import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from google_images_download import google_images_download

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('_test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('_math'):
        equation = message.content[5:].replace(" ", "")
        con = True
        for x in equation:
            if x != '1' and x != '2' and x != '3' and x != '4' and x != '5' and x != '6' and x != '7' and x != '8' and x != '9' and x != '+' and x != '-' and x != '*' and x != '/' and x != '\'' and x != "%":
                con = False
        if con:
            temp = await client.send_message(message.channel, eval(equation))

    elif message.content.startswith('_roll'):
        num = message.content[5:].replace(" ", "")
        if num.isdigit():
            x = randint(1, int(num))
            await client.send_message(message.channel, x)

    elif message.content.startswith('_help') or message.content.startswith('_h'):
        text = "'_math' - then input an equation to spit out an answer\n"
        text += "'_roll' then a number to roll a #sided die\n"
        text += "'_image' then image that you and it will post an image"
        await client.send_message(message.channel, text)

    elif message.content.startswith('_image'):
        picsearch = message.content[6:]
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords":picsearch,"limit":5,"print_urls":True}
        paths = response.download(arguments)
        dir = "downloads" + "\\"
        dir += picsearch
        pic = random.choice(os.listdir(dir))
        dir+= "\\" + pic;
        await client.send_file(message.channel, dir)

    elif message.content.startswith('_rps'):
        option = message.content[4:].replace(" ","")
        num = randint(1,3)
        cpu = ""
        if num == 1:
            cpu = "rock"

        elif num == 2:
            cpu = "paper"
        else:
            cpu = "scissors"

        if option!= "rock" and option !="scissors" and option!="paper":
            await client.send_message(message.channel, "Uhhh that's not an option friend.")

        elif (option == "rock" and num == 1) or (option =="scissors" and num == 3) or (option == "paper" and num == 2):
            await client.send_message(message.channel, "I rolled " + cpu + ", we draw..")

        elif (option =="rock" and num == 2) or (option == "paper" and num == 3) or (option == "scissors" and num == 1):
            await client.send_message(message.channel, "I rolled " + cpu + " on purpose to let you win.")

        elif (option == "rock" and num == 3) or (option == "paper" and num == 1) or (option == "scissors" and num == 2):
            await client.send_message(message.channel, "I rolled " + cpu + ". It's obvious I would win.")

client.run("NDAwODkyOTgxMzI3OTUzOTIw.DTiSDA.oBDl_KK2Q68wjqPvV0QTdoOUASo")
