from games_file import game_file
import discord
import random
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot_token = 'NzIyNDg2Mzg5NjAxNzMwNjYx.Xu1OaA.BCY6jc2nCTUNpWDkDRrNQRDNo8s'

# Events


@bot.event
async def on_ready():
    print('Crew Bot: On ready')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server')


@bot.event
async def on_member_remove(member):
    print(f'{member} has been cut')


# @client.event
# async  def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Missing argument in command')


# Commands


# Play Game

@bot.command(aliases=['game', 'Play'])
# take any number of args (args stored as an array)
async def play(ctx, *args):

    # load games JSON file
    games_file_obj = game_file('games.json')
    games_list = games_file_obj.latest_game_array()

    if len(args) > 0:
        if args[0] == 'add':
            if len(args) > 1:
                game_title = args[1]
                added = games_file_obj.add_game(game_title, games_list)
                if added:
                    print('added ' + args[1])
                    msg = 'added ' + args[1] + ' to the list'
                else:
                    msg = 'game already added'
            else:
                msg = 'please type a game title'

        elif args[0] == 'remove':
            if len(args) > 1:
                game_title = args[1]
                removed = games_file_obj.remove_game(game_title, games_list)
                if removed:
                    print('removed ' + args[1])
                    msg = 'removed ' + args[1] + ' from the list'
                else:
                    msg = 'game not found'
            else:
                msg = 'please type a game title'
        elif args[0] == 'list-all':
            msg = 'all games: ' + ' '.join(games_list)
    else:
        game = random.choice(games_list)
        msg = 'You should play ' + game
        print(f'game: play {game}')

    await ctx.send(f'{msg}')

# High School Musical Commands


@bot.command(aliases=['what-team'])
async def what_team(ctx):
    await ctx.send('Wildcats')
    print('What Team? Wildcats')


@bot.command()
async def wildcats(ctx):
    await ctx.send('Get\'cha Head in the Game')
    print('Wildcats!, Get\'cha Head in the Game')


# 8Ball

@bot.command(aliases=['8Ball', '8ball'])
async def _8ball(ctx, *, question):
    if question.lower() in ["is leon gay?"]:
        await ctx.send('8Ball says "Definitely"')
        print('8Ball Question: {question}, Answer: Definitely')
    else:
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'Yes',
                     'You may rely on it.']
        rand_ans = random.choice(responses)
        await ctx.send(f'8Ball says "{rand_ans}"')
        print(f'8Ball Question: {question}, Answer: {rand_ans}')


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Ask a question you dumb fuck')


bot.run(bot_token)
