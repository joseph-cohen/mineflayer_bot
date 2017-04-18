import praw

bot = praw.Reddit(user_agent = 'mineflayer_bot v0.1.2',
	client_id = '9dckV-29pYCLlA',
	client_secret = '_E8PrpgN3FvxYqKav_Io30bWIAY',
	username = 'mineflayer_bot',
	password = 'Contrasena1')

subreddit = bot.subreddit('EnterTheGungeon')

comments = subreddit.stream.comments()

for comment in comments:
	text = comment.body
	if 'mine flayer' in text.lower():
		message = 'I too would like for that shitty boss to stop pointing that gun at his bell and start pointing it at his head \n \n \n ^^^I ^^^am ^^^a ^^^bot, ^^^check ^^^me ^^^out [^^here](https://github.com/josephcda/mineflayer_bot)'
		comment.reply(message)