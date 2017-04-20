# mineflayer_bot
A reddit bot that replies to comments on the r/enterthegungeon subreddit using PRAW.

it works like this, if the user has mentioned the words "mine flayer" (A commonly hated boss in the Enter the Gungeon videogame) in a comment on the r/EnterTheGungeon subreddit, then the bot will respond like this:

'I too would like for that shitty boss to stop pointing that gun at his bell and start pointing it at his head 
 
 I am a bot, check me out [here](https://github.com/josephcda/mineflayer_bot)'

For this, it uses this logic:

	subreddit = bot.subreddit('EnterTheGungeon')

	comments = subreddit.stream.comments()

	for comment in comments:
		text = comment.body
		if 'mine flayer' in text.lower():
			message = 'I too would like for that shitty boss to stop pointing that gun at his bell and start pointing it at his head \n \n \n ^^^I ^^^am ^^^a ^^^bot, ^^^check ^^^me ^^^out [^^^here](https://github.com/josephcda/mineflayer_bot)'
			comment.reply(message)
