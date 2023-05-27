#Sunset Yellow Discord Bot
#This code was mostly from https://youtu.be/SPTfmiYiuok
#I'm trying to edit, have fun and maybe improve on the YouTube video's discord chatbot finally making it my own
#Playing music codes from https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands


intents = discord.Intents.default(
)  # Create a new instance of the default intents
client = discord.Client(
  intents=intents)  # Pass the intents argument when initializing the Client

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='', intents=intents)

#client = discord.Client()
starting = ["help", "Help", "start", "Start"]
sad_words = [
  "sad", "Sad", "unhappy", "Worry", "angry", "miserable", "moody", "Moody",
  "Cry", "cry", "Cries", "cries", "sadge", "Sadge", "rejection", "Rejection",
  "rejected", "Rejected", "worry", "worried", "Worried", "Disappointed",
  "disappointed"
]

chanceBall = [
  "Divine intervention time: NO!", "Surprisingly, I do not know...",
  "Something tells me this is too big of a decision to simply let me decide! Trust yourself!",
  "Hm...umm...really sorry to break it to you...but LOL IT IS A BIG FAT NOPE",
  "YES! The souls deem it so!", "Hmmm...maybe", "LOL NO",
  "This will yield great outcomes! Go for it!!!",
  "It is an unfortunate nope. Perhaps, it is time for you to re evluate your life choices.",
  "Sorry...It is a no. Do not worry. Everything will be okay. If you wanted this to be a yes, you do not have to hear it from me. You can validate yourself. If you struggle to, then just to let you know: You are special. You are worth it. You are awesome. If you believe it to be a yes, I know you can make it. From me to you: I believe in you",
  "Yes! I wish you the best btw!", "As I see it, yes", "Ask again later",
  "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
  "Don’t count on it", "It is certain", "It is decidedly so", "Most likely",
  "My reply is no", "My sources say no.", "Outlook good",
  "Outlook not so good", "Reply hazy try again", "Signs point to yes",
  "Very doubtful", "Without a doubt", "Yes", "No", "Yes, definitely.",
  "You may rely on it", "The Whole World is screaming Yes!", "YAS QUEEN!",
  "Kamakura, Kamakura Yaas Queen!",
  "Yes, but do not trust the clock, go at your own pace!", "Hell Yeah!",
  "Not Yet", "The Universe smiles upon this."
]

#Tarot cards: https://labyrinthos.co/blogs/tarot-card-meanings-list
tarothi = ["ytarot", "Ytarot"]
tarot = [
  "The World Upright: fulfillment, harmony, completion",
  "The World Reversed: incompletion, no closure",
  "Judgement Upright: reflection, reckoning, awakening",
  "Judgement Reversed: lack of self awareness, doubt, self loathing",
  "The Sun Upright: joy, success, celebration, positivity",
  "The Sun Reversed: negativity, depression, sadness",
  "The Moon Upright: unconscious, illusions, intuition",
  "The Moon Reversed: confusion, fear, misinterpretation",
  "The Star Upright: hope, faith, rejuvenation",
  "The Star Reversed: faithlessness, discouragement, insecurity",
  "The Tower Upright: sudden upheaval, broken pride, disaster",
  "The Tower Reversed: disaster avoided, delayed disaster, fear of suffering",
  "The Devil Upright: addiction, materialism, playfulness",
  "The Devil Reversed: freedom, release, restoring control",
  "Temperance Upright: middle path, patience, finding meaning",
  "Temperance Reversed: extremes, excess, lack of balance",
  "Death Upright: end of cycle, beginnings, change, metamorphosis",
  "Death Reversed: fear of change, holding on, stagnation, decay",
  "The Hanged Man Upright: sacrifice, release, martyrdom",
  "The Hanged Man Reversed: stalling, needless sacrifice, fear of sacrifice",
  "Justice Upright: cause and effect, clarity, truth",
  "Justice Reversed: dishonesty, unaccountability, unfairness",
  "The Wheel of Fortune Upright: change, cycles, inevitable fate",
  "The Wheel of Fortune Reversed: no control, clinging to control, bad luck",
  "The Hermit Reversed: loneliness, isolation, lost your way",
  "The Hermit Upright: contemplation, search for truth, inner guidance",
  "Strength Upright: inner strength, bravery, compassion, focus",
  "Strength Reversed: self doubt, weakness, insecurity",
  "The Chariot Upright: direction, control, willpower",
  "The Chariot Reversed: lack of control, lack of direction, aggression",
  "The Lovers Upright: partnerships, duality, union",
  "The Lovers Reversed: loss of balance, one-sidedness, disharmony",
  "The Hierophant Upright: tradition, conformity, morality, ethics",
  "The Hierophant Reversed: rebellion, subversiveness, new approaches",
  "The Emperor Upright: authority, structure, control, fatherhood",
  "The Emperor Reversed: tyranny, rigidity, coldness",
  "The Empress Upright: motherhood, fertility, nature",
  "The Empress Reversed: dependence, smothering, emptiness, nosiness",
  "The High Priestess Upright: intuitive, unconscious, inner voice",
  "The High Priestess Reversed: lack of center, lost inner voice, repressed feelings",
  "The Magician Upright: willpower, desire, creation, manifestation",
  "The Magician Reversed: trickery, illusions, out of touch",
  "The Fool Upright: innocence, new beginnings, free spirit",
  "The Fool Reversed: recklessness, taken advantage of, inconsideration"
]
tarotwands = [
  'Seven of Wands Upright: perseverance, defensive, maintaining control',
  'Seven of Wands Reversed: give up, destroyed confidence, overwhelmed',
  'Four of Wands Upright: community, home, celebration',
  'Four of Wands Reversed: lack of support, transience, home conflicts',
  'Ace of Wands Upright: creation, willpower, inspiration, desire',
  'Ace of Wands Reversed: lack of energy, lack of passion, boredom',
  'Ten of Wands Upright: accomplishment, responsibility, burden',
  'Ten of Wands Reversed: inability to delegate, overstressed, burnt out',
  'Nine of Wands Upright: resilience, grit, last stand',
  'Nine of Wands Reversed: exhaustion, fatigue, questioning motivations',
  'Eight of Wands Upright: rapid action, movement, quick decisions',
  'Eight of Wands Reversed: panic, waiting, slowdown',
  'Six of Wands Upright: victory, success, public reward',
  'Six of Wands Reversed: excess pride, lack of recognition, punishment',
  'Five of Wands Upright: competition, rivalry, conflict',
  'Five of Wands Reversed: avoiding conflict, respecting differences',
  'Three of Wands Upright: looking ahead, expansion, rapid growth',
  'Three of Wands Reversed: obstacles, delays, frustration',
  'Two of Wands Upright: planning, making decisions, leaving home',
  'Two of Wands Reversed: fear of change, playing safe, bad planning',
  'Page of Wands Upright: exploration, excitement, freedom',
  'Page of Wands Reversed: lack of direction, procrastination, creating conflict',
  'Queen of Wands Upright: courage, determination, joy',
  'Queen of Wands Reversed: selfishness, jealousy, insecurities',
  'King of Wands Upright: big picture, leader, overcoming challenges',
  'King of Wands Reversed: impulsive, overbearing, unachievable expectations',
  'Knight of Wands Upright: action, adventure, fearlessness',
  'Knight of Wands Reversed: anger, impulsiveness, recklessness'
]

tarotcups = [
  'King of Cups Upright: compassion, control, balance',
  'King of Cups Reversed: coldness, moodiness, bad advice',
  'Queen of Cups Upright: compassion, calm, comfort',
  'Queen of Cups Reversed: martyrdom, insecurity, dependence',
  'Knight of Cups Upright: following the heart, idealist, romantic',
  'Knight of Cups Reversed: moodiness, disappointment',
  'Page of Cups Upright: happy surprise, dreamer, sensitivity',
  'Page of Cups Reversed: emotional immaturity, insecurity, disappointment',
  'Ten of Cups Upright: inner happiness, fulfillment, dreams coming true',
  'Ten of Cups Reversed: shattered dreams, broken family, domestic disharmony',
  'Nine of Cups Upright: satisfaction, emotional stability, luxury',
  'Nine of Cups Reversed: lack of inner joy, smugness, dissatisfaction',
  'Eight of Cups Upright: walking away, disillusionment, leaving behind',
  'Eight of Cups Reversed: avoidance, fear of change, fear of loss',
  'Seven of Cups Upright: searching for purpose, choices, daydreaming',
  'Seven of Cups Reversed: lack of purpose, diversion, confusion',
  'Six of Cups Upright: familiarity, happy memories, healing',
  'Six of Cups Reversed: moving forward, leaving home, independence',
  'Five of Cups Upright: loss, grief, self-pity',
  'Five of Cups Reversed: acceptance, moving on, finding peace',
  'Four of Cups Upright: apathy, contemplation, disconnectedness',
  'Four of Cups Reversed: sudden awareness, choosing happiness, acceptance',
  'Three of Cups Upright: friendship, community, happiness',
  'Three of Cups Reversed: overindulgence, gossip, isolation',
  'Two of Cups Upright: unity, partnership, connection',
  'Two of Cups Reversed: imbalance, broken communication, tension',
  'Ace of Cups Upright: new feelings, spirituality, intuition',
  'Ace of Cups Reversed: emotional loss, blocked creativity, emptiness'
]

tarotswords = [
  'King of Swords Upright: head over heart, discipline, truth',
  'King of Swords Reversed: manipulative, cruel, weakness',
  'Knight of Swords Upright: action, impulsiveness, defending beliefs',
  'Knight of Swords Reversed: no direction, disregard for consequences, unpredictability',
  'Queen of Swords Upright: complexity, perceptiveness, clear mindedness',
  'Queen of Swords Reversed: cold hearted, cruel, bitterness',
  'Page of Swords Upright: curiosity, restlessness, mental energy',
  'Page of Swords Reversed: deception, manipulation, all talk',
  'Ten of Swords Upright: failure, collapse, defeat',
  'Ten of Swords Reversed: can not get worse, only upwards, inevitable end',
  'Nine of Swords Upright: anxiety, hopelessness, trauma',
  'Nine of Swords Reversed: hope, reaching out, despair',
  'Eight of Swords Upright: imprisonment, entrapment, self-victimization',
  'Eight of Swords Reversed: self acceptance, new perspective, freedom',
  'Seven of Swords Upright: deception, trickery, tactics and strategy',
  'Seven of Swords Reversed: coming clean, rethinking approach, deception',
  'Six of Swords Upright: transition, leaving behind, moving on',
  'Six of Swords Reversed: emotional baggage, unresolved issues, resisting transition',
  'Five of Swords Upright: unbridled ambition, win at all costs, sneakiness',
  'Five of Swords Reversed: lingering resentment, desire to reconcile, forgiveness',
  'Three of Swords Upright: heartbreak, suffering, grief',
  'Three of Swords Reversed: recovery, forgiveness, moving on',
  'Four of Swords Upright: rest, restoration, contemplation',
  'Four of Swords Reversed: restlessness, burnout, stress',
  'Two of Swords Upright: difficult choices, indecision, stalemate',
  'Two of Swords Reversed: lesser of two evils, no right choice, confusion',
  'Ace of Swords Upright: breakthrough, clarity, sharp mind',
  'Ace of Swords Reversed: confusion, brutality, chaos'
]
tarotpentacle = [
  'King of Pentacles Upright: abundance, prosperity, security',
  'King of Pentacles Reversed: greed, indulgence, sensuality',
  'Queen of Pentacles Upright: practicality, creature comforts, financial security',
  'Queen of Pentacles Reversed: self-centeredness, jealousy, smothering',
  'Knight of Pentacles Upright: efficiency, hard work, responsibility',
  'Knight of Pentacles Reversed: laziness, obsessiveness, work without reward',
  'Page of Pentacles Upright: ambition, desire, diligence',
  'Page of Pentacles Reversed: lack of commitment, greediness, laziness',
  'Ten of Pentacles Upright: legacy, culmination, inheritance',
  'Ten of Pentacles Reversed: fleeting success, lack of stability, lack of resources',
  'Nine of Pentacles Upright: fruits of labor, rewards, luxury',
  'Nine of Pentacles Reversed: reckless spending, living beyond means, false success',
  'Eight of Pentacles Upright: apprenticeship, passion, high standards',
  'Eight of Pentacles Reversed: lack of passion, uninspired, no motivation',
  'Seven of Pentacles Upright: hard work, perseverance, diligence',
  'Seven of Pentacles Reversed: work without results, distractions, lack of rewards',
  'Six of Pentacles Upright: charity, generosity, sharing',
  'Six of Pentacles Reversed: strings attached, stinginess, power and domination',
  'Five of Pentacles Upright: need, poverty, insecurity',
  'Five of Pentacles Reversed: recovery, charity, improvement',
  'Four of Pentacles Upright: conservation, frugality, security',
  'Four of Pentacles Reversed: greediness, stinginess, possessiveness',
  'Three of Pentacles Upright: teamwork, collaboration, building',
  'Three of Pentacles Reversed: lack of teamwork, disorganized, group conflict',
  'Two of Pentacles Upright: balancing decisions, priorities, adapting to change',
  'Two of Pentacles Reversed: loss of balance, disorganized, overwhelmed',
  'Ace of Pentacles Upright: opportunity, prosperity, new venture',
  'Ace of Pentacles Reversed: lost opportunity, missed chance, bad investment'
]

ballof8 = ["8ball", "Magical8ball", "8Ball", "8-ball", "8-Ball"]

starter_encouragements = [
  "Cheer up!", "Hang in there.", "You have got this.",
  "Oh no! Take a deep breath and calm down first. It is fine if you are feeling sad but if you feel like it is a problem, please remember that you are the bigger person!",
  "Life is better when you’re laughing.",
  "Stars can’t shine without darkness.",
  "Cheer up, tomorrow is another chance.", "Stay Determined.",
  "Tomorrow is another day.",
  "You can do this. 00:00 is a new day. Stay determined till then. Look at how strong you are! Come on bud! You are at the home stretch!",
  "You are a great person! Just believe in yourself bud!",
  "Things may be tough, but you're tougher!", "Your opinions are valid!✨",
  "The only thing that matters is that you can still love yourself for you. That's the most important part!"
]

sweet_links = [
  "https://www.youtube.com/watch?v=2JO3NYg6Bt0",
  "https://www.youtube.com/watch?v=6FPIuCteus0",
  "https://www.youtube.com/watch?v=mGTJq6dfpSE",
  "Here, listen to this and cheer up! https://www.youtube.com/watch?v=pw-2e3T03Co&t=3231s&ab_channel=pengweng",
  "https://www.youtube.com/watch?v=AArJ_lJGKv0",
  "https://www.youtube.com/watch?v=38k5zr1e0HI",
  "https://www.youtube.com/watch?v=ITc-om9SVr4",
  "https://www.youtube.com/watch?v=639hc_F2TZU",
  "https://www.youtube.com/watch?v=w5_X-QFwmoo",
  "https://www.youtube.com/watch?v=0D28qd--kRE",
  "https://www.youtube.com/watch?v=cVVs1loGEVg",
  "https://www.youtube.com/watch?v=VxHkydPsyjY",
  "https://www.youtube.com/watch?v=Fw7C6IsDYgI",
  "https://www.youtube.com/watch?v=zFT3f9biz68",
  "https://www.youtube.com/watch?v=7UWBYJjuIL0",
  "https://www.youtube.com/watch?v=-5q5mZbe3V8",
  "https://www.youtube.com/watch?v=KCssqGPEWvM",
  "https://www.youtube.com/watch?v=BEMaH9Sm3lQ",
  "https://www.oprahdaily.com/life/health/a27507222/how-to-stop-being-sad/",
  "https://www.youtube.com/watch?v=b53b2mMJ2k0",
  "https://www.youtube.com/watch?v=b53b2mMJ2k0",
  "https://www.youtube.com/watch?v=KVAt8jwUobI",
  "https://www.youtube.com/watch?v=kX0vO4vlJuU",
  "https://www.youtube.com/watch?v=xEeFrLSkMm8",
  "https://www.youtube.com/watch?v=OGMeHzBLuM8",
  "https://www.youtube.com/watch?v=TgOu00Mf3kI",
  "https://www.youtube.com/watch?v=vGbuUFRdYqU",
  "https://www.youtube.com/watch?v=h-wATDal7_0",
  "https://www.youtube.com/watch?v=bNT-zFJKifI",
  "https://www.youtube.com/watch?v=50VNCymT-Cs",
  "https://www.youtube.com/watch?v=mzmjdntlRJk",
  "https://www.youtube.com/watch?v=d_HlPboLRL8",
  "https://www.youtube.com/watch?v=24u3NoPvgMw",
  "https://www.youtube.com/watch?v=V1Pl8CzNzCw",
  "https://www.youtube.com/watch?v=nSDgHBxUbVQ",
  "https://www.youtube.com/watch?v=oFrvRiixXcA"
]

red_flags = {
  "Kill", "kill", "suicide", "Suicide", "depressed", "Depressed", "depressing",
  "Suicidal", "murder", "Murder", "killing", "Killing", "murderer", "Murderer",
  "scared", "Scared"
}
sayYellow = [
  "Heya~ Whatz cooking good looking~", "Hola~ Soy Yellow!", "Yellow!",
  "Hello, sunshine!", "I come in peace!", "Ahoy, matey!",
  "Top of the mornin’ to ya!", "Wazzup homeslice?", "Aloha!", "Que pasa!",
  "Bonjour!", "Ciaossu!",
  "Salutations pretty person. What do you require of me?", "Annyeong~",
  "Hey beautiful!", "Yo! Wazzup?"
]
salutations = [
  "Hiya", "hiya", "Heya", "Yahallo", "yahallo", "heya", "Yellow", "yellow",
  "Aloha", "aloha", "bonjour", "Bonjour", "annyeong", "Annyeong", "Hello",
  "hello", "Konnichiwa", "Konnichiwa", "Hola", "hola", "Nihao", "nihao"
]

if "responding" not in db.keys():
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  # Example
  # if msg.startswith('$inspire'):
  #   quote = get_quote()
  #   await message.channel.send(quote)
  # if db["responding"]:
  # if any(word in msg for word in sad_words):
  #       await message.channel.send(random.choice(options))
  #Example
  # if msg.startswith(starting):
  #   await message.channel.send("Get all the commands needed: help \n If you're sad: sad")

  # if msg.startswith('$inspire'):
  #   quote = get_quote()
  #   await message.channel.send(quote)

  #IMPORTANT: Here's where all the commands are
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(
        random.choice(options) + " " + random.choice(sweet_links))

    # Example:
    # if any(word in msg for word in sad_words):
    #   await message.channel.send(random.choice(options))
    #starting
    if any(word in msg for word in salutations):
      embed = discord.Embed(title=random.choice(sayYellow),
                            color=discord.Color.orange())
      # await message.channel.send(embed=embed)
    #await message.channel.send(random.choice(sayYellow))
    # Red flags
    if any(word in msg for word in red_flags):
      await message.channel.send(
        random.choice(options) +
        "\n \nHold on. Please don't let go yet. \n \nSamaritans of Singapore: 1800-221 4444\n Singapore Website: https://www.sos.org.sg/ \n \nSocial Awareness Education & Mental Health Resources \n Website: https://ttsresources.carrd.co/ \n \n International Suicide Helplines: https://www.opencounseling.com/suicide-hotlines \n \n"
      )
      #Games
    if any(word in msg for word in ballof8):
      await message.channel.send(random.choice(chanceBall))
      #tarot
    if any(word in msg for word in tarothi):
      await message.channel.send(
        "journey- \n\nPast: " + random.choice(tarot) + "\n\nPresent: " +
        random.choice(tarot) + "\n\nFuture: " + random.choice(tarot) +
        "\n \npassion, inspiration and willpower- \n" +
        random.choice(tarotwands) +
        "\n \nemotions, the unconscious, creativity, and intuition- \n" +
        random.choice(tarotcups) +
        "\n \nintelligence, logic, truth, ambition, conflict and communication- \n"
        + random.choice(tarotswords) +
        "\n \nsecurity, stability, nature, health, and prosperity- \n" +
        random.choice(tarotpentacle))

    if any(word in msg for word in starting):
      embed = discord.Embed(
        title="Sunset Yellow",
        #url="https://realdrewdata.medium.com/",
        description="I'll be your little buddy! Tell me how you're feeling!",
        color=discord.Color.orange())

      embed.add_field(name="**Help**",
                      value="Get all the commands needed",
                      inline=False)
      embed.add_field(
        name="**ytarot**",
        value=
        "Get a full tarot reading! All tarot stuff are from: https://labyrinthos.co/blogs/tarot-card-meanings-list",
        inline=False)
      embed.add_field(
        name="**sad**",
        value=
        "If you're sad, you can type in I am sad. \n\nThere are also other ways to initiate the bot (and I'll leave the fun of finding them to you! For example, typing in cries.\n\n You can try talking to the bot on how you're feeling. It might reply",
        inline=False)
      embed.add_field(name="**8ball**",
                      value="Chance ball! Ask it anything!",
                      inline=False)
    # embed.add_field(name="**ytarot**",
    #       value="Get a full tarot reading! All tarot stuff are from: https://labyrinthos.co/blogs/tarot-card-meanings-list",
    # inline=False)

  await message.channel.send(embed=embed)

  #   # Red flags
  # if any(word in msg for word in red_flags):
  #   await message.channel.send(random.choice(options)+"\n \nHold on. Please don't let go yet. \n \nSamaritans of Singapore: 1800-221 4444\n Singapore Website: https://www.sos.org.sg/ \n \nSocial Awareness Education & Mental Health Resources \n Website: https://ttsresources.carrd.co/ \n \n International Suicide Helplines: https://www.opencounseling.com/suicide-hotlines \n \n")

  #   #Games
  # if any(word in msg for word in ballof8):
  #   await message.channel.send(random.choice(chanceBall))

  # #tarot
  # if any(word in msg for word in tarothi):
  #   await message.channel.send(random.choice(tarot))

  #embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
  #Example from https://python.plainenglish.io/python-discord-bots-formatting-text-efca0c5dc64a
  # embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
  # embed.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=False)
  # embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
  # embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
  # embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
  # embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
  # embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
  # embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
  # embed.set_footer(text="Learn more here: realdrewdata.medium.com")

  # embed.add_field(name="**Help**", value="Get all the commands needed", inline=False)
  # embed.add_field(name="**sad**", value="If you're sad, you can type in I am sad. \n\nThere are also other ways to initiate the bot (and I'll leave the fun of finding them to you! For example, typing in cries.\n\n You can try talking to the bot on how you're feeling. It might reply", inline=False)
  # embed.add_field(name="**8ball**", value="Chance ball! Ask it anything!", inline=False)
  # await message.channel.send(embed=embed)
  #await message.channel.send("Get all the commands needed: help \n \nIf you're sad: sad\n\nGames: 8ball")

  #Happy mood

  #Music
  # if msg.startswith('!join'):
  #   async def join(ctx):
  #     if not ctx.message.author.voice:
  #       await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
  #       return
  #     else:
  #       channel = ctx.message.author.voice.channel
  #     await channel.connect()

  #Organize

  # if msg.startswith("$new"):
  #   encouraging_message = msg.split("$new ",1)[1]
  #   update_encouragements(encouraging_message)
  #   await message.channel.send("New encouraging message added.")

  # if msg.startswith("$del"):
  #   encouragements = []
  #   if "encouragements" in db.keys():
  #     index = int(msg.split("$del",1)[1])
  #     delete_encouragment(index)
  #     encouragements = db["encouragements"]
  #   await message.channel.send(encouragements)

  # if msg.startswith("$list"):
  #   encouragements = []
  #   if "encouragements" in db.keys():
  #     encouragements = db["encouragements"]
  #   await message.channel.send(encouragements)

  # if msg.startswith("$responding"):
  #   value = msg.split("$responding ",1)[1]

  #   if value.lower() == "true":
  #     db["responding"] = True
  #     await message.channel.send("Responding is on.")
  #   else:
  #     db["responding"] = False
  #     await message.channel.send("Responding is off.")


keep_alive()
client.run('OTMwMzA5MDY1MTU3MDAxMjg2.G7sLSC.oWv2rb1s_Ul2PJm2meEgcow-AuTF9smbJFv2IM')
