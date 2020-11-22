import os
from keep_alive import keep_alive
import discord.ext
from discord.ext import commands
from random import choice as randchoice
from random import randint
import static_lists
from random import choice
import asyncio

extensions = []


bot = commands.Bot(
	command_prefix="~",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
    help_command=None
)

bot.author_id = 649992575247319041  # Change to your discord id!!!


@bot.event 
async def on_ready():  # When the bot is ready
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('with my chumbuddies'))
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

#repeats what you tell it
@bot.command(brief="Repeats what you say", usage="repeat <words>")
async def repeat(ctx, *, input):
    await ctx.send(input)

@bot.command(brief="Opinion", usage="wayfaringcommands")
async def wayfaringcommands(ctx):
  embed=discord.Embed(
    title=("**Wayfaringcommands is inferior**")
  )
  embed.set_image(url="https://media1.tenor.com/images/8c9bb076d44f255e81137aa2ae59811b/tenor.gif?itemid=12638023")
  await ctx.send(embed=embed)


#funny "a" gif
@bot.command(brief="Sends the funny \"a\" gif", usage="a")
async def a(ctx):
  await ctx.send("https://tenor.com/view/gawr-gura-gawr-gura-gif-18439720")

#funny peanut
@bot.command(brief="Sends the funny \"peanut butter baby\" gif", usage="peanut")
async def peanut(ctx):
  await ctx.send("https://media.tenor.com/images/2a0f7c74fe87afe2cc6649046f998c28/tenor.gif")


#Chooses random attacker
@bot.command(brief="Random siege attacker",usage="random_attack")
async def random_attack(ctx):
  op = static_lists.attack_operators
  message = (f"**{randchoice(op)}**")
  embed = discord.Embed(title = message)
  await ctx.send(embed=embed)

#Chooses random defender
@bot.command(brief="Random siege defender", usage="random_defense")
async def random_defense(ctx):
  op = static_lists.defense_operators
  message = (f"**{randchoice(op)}**")
  embed = discord.Embed(title = message)
  await ctx.send(embed=embed)

#Chooses random attacker with stupid name
@bot.command(brief="Random siege attacker", usage="random_meme_attack")
async def random_meme_attack(ctx):
  op = static_lists.attack_operators_meme
  message = (f"**{randchoice(op)}**")
  embed = discord.Embed(title = message)
  await ctx.send(embed=embed)

#Chooses random defender with stupid name
@bot.command(brief="Random siege defender", usage="random_meme_attack")
async def random_meme_defense(ctx):
  op = static_lists.defense_operators_meme
  message = (f"**{randchoice(op)}**")
  embed = discord.Embed(title = message)
  await ctx.send(embed=embed)
  
#flips a coin  
@bot.command(brief="Flips a coin", usage="coinflip")
async def coinflip(ctx):
  sides = ["Heads", "Tails"]
  await ctx.send(f"Result is {sides[randint(0,2)]}!")

#Cough cough, gets image from some research i did
@bot.command(brief="Random image for **research**", usage="devianart")
async def deviantart(ctx):
  message = ("**devianart moment**")
  embed = discord.Embed(
    title = message)
  embed.set_image(url=randchoice(static_lists.deviantart_imgs))
  await ctx.send(embed=embed)

#Say hi :D
@bot.command(brief="Say hello", usage="hello")
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))



#delete messages, default is 10 if no value is entered
@bot.command(brief="Deletes given number of messages", usage="clear <number of messages>")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
  if amount > 50:
    await ctx.send("You cannot clear more than 50 at once")
  else:
    await ctx.channel.purge(limit=amount)


#help command
@bot.command(brief="Get some help", usage="help")
async def help(ctx):
  helptext = ""
  for command in bot.commands:
      helptext+=f"{bot.command_prefix}{command.usage}\n "

  embed = discord.Embed(
    title="Help",
  )
  embed.add_field(name=f"**Commands** \n", value=helptext, inline=False)

  await ctx.send(embed=embed)


#Wow this shit works -note to add a way to keep reminders ticking if bot is restarted
@bot.command(brief = "Reminds you to do something, time formats as 5s 5m 5h 5d for second, minute, hour and day respectivly", usage = "reminder <time> <note>")
async def reminder(ctx, remindertime, *, reminder):
  print(remindertime)
  print(reminder)
  user = ctx.message.author
  seconds = 0
  if remindertime.endswith("d"):
    seconds += int(remindertime[:-1]) * 60 * 60 * 24
    counter = f"{seconds // 60 // 60 // 24} days"
  elif remindertime.endswith("h"):
    seconds += int(remindertime[:-1]) * 60 * 60
    counter = f"{seconds // 60 // 60} hours"
  elif remindertime.endswith("m"):
    seconds += int(remindertime[:-1]) * 60
    counter = f"{seconds // 60} minutes"
  elif remindertime.endswith("s"):
    seconds += int(remindertime[:-1])
    counter = f"{seconds} seconds"
  if seconds < 300:
    message = "**Duration too short, pls try again :(**"
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/744484778744741959/744564004697014322/questionmark.gif")
    await ctx.send(embed=embed)
  elif seconds > 7776000:
    message = "**Duration too long, pls try again :(**"
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/744484778744741959/744564004697014322/questionmark.gif")
    await ctx.send(embed=embed)
  else:
    await ctx.send(f"Alright, I will remind you about {reminder} in {counter}.")
    await asyncio.sleep(seconds)
    message = f"Hi {user.mention}, you asked me to remind you about {reminder} {counter} ago."
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://media1.tenor.com/images/80c48fb0b8aa3a41e591dbd304fc2bd5/tenor.gif?itemid=5390507")
    await user.send(embed=embed)

#Embeds pat with random gif
@bot.command(brief="Gives someone a pat", usage="pat <mention member>")
async def pat(ctx, member: discord.Member):
  pat_gifs = static_lists.pat_gifs
  user = ctx.author.name
  name = member.name
  message = ("**" + user + "**" + " gave **" + name + "** a pat")
  embed = discord.Embed(
    title = message)
  embed.set_image(url=randchoice(pat_gifs))
  await ctx.send(embed=embed)

#Embeds hug with random gif
@bot.command(brief="Gives someone a hug", usage="hug <mention member>")
async def hug(ctx, member: discord.Member):
  user = ctx.author.name
  name = member.name
  message = ("**" + user + "** " + "gives **" + name + "** much hugs")
  hug_gifs = static_lists.hug_gifs
  embed = discord.Embed(title = message)
  embed.set_image(url=randchoice(hug_gifs))
  await ctx.send(embed=embed)

#pokes someone with a random gif
@bot.command(brief="Gives someone a poke", usage="poke <mention member>")
async def poke(ctx, member: discord.Member):
  poke_gifs= static_lists.poke_gifs
  user = ctx.author.name
  name = member.name
  message = ("**" + user + "** " + "poked **" + name + "**")
  embed = discord.Embed(title = message)
  embed.set_image(url=randchoice(poke_gifs))
  await ctx.send(embed=embed)

#I dont want to talk about this one, blame lynchie
@bot.command(brief="Nut on someone", usage="nut <mention member>")
async def nut(ctx, member: discord.Member):
  nut_gifs = static_lists.nut_gifs
  name = member.name
  user = ctx.author.name
  message = ("**" + user + "** nutted on **" + name + "**")
  embed = discord.Embed(title = message)
  embed.set_image(url=randchoice(nut_gifs))
  await ctx.send(embed=embed)

#error handling
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    message = "You seem to be missing an input, please **try again?**"
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/744484778744741959/744564004697014322/questionmark.gif")
    await ctx.send(embed=embed)
  elif isinstance(error, commands.BadArgument):
    message = "I dont think i know that person, please **try again?**"
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/744484778744741959/744564004697014322/questionmark.gif")
    await ctx.send(embed=embed)
  elif isinstance(error, commands.CommandNotFound):
    message = "I dont think that command exists, please **try again?**"
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/744484778744741959/744564004697014322/questionmark.gif")
    await ctx.send(embed=embed)
  elif isinstance(error, commands.MissingPermissions):
    message = "You don't have permission for that"
    embed = discord.Embed(
      title = message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/744484778744741959/744564004697014322/questionmark.gif")
    await ctx.send(embed=embed)



if __name__ == '__main__':  # Ensures this is the file being ran
  for extension in extensions:
    bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot
