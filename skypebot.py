import Skype4Py 
### random selection lists ###
fap = ['You must fap to Barbies', 'You must do the suicidewank; re roll for what to fap to. Information: !suicidewank', 'You must fap to asshole', 'You must fap to reddit.com/r/gore', 'You must fap to Habbo cyber', 'You must fap to men', 'You must fap to fat chicks', 'You must fap to celebs', 'You must fap to lesbian', 'You must fap to anal', 'You must fap to masturbation', 'You must fap to scat', 'You must fap to literotica', 'You must fap to Cartoon', 'You must fap to generic porn', 'You must fap to public porn']
bored = ['Learn code', 'Troll a server', 'Read a book', 'Speed run a game', 'Buy a random item on ebay', 'Draw a picture and send it to Yanz', 'Learn to backflip', 'Go for a run', 'Write a short story', 'Go for a walk', 'Exercise', 'Masturbate', 'Reddit.com', 'Play a video game', 'Message an old friend', 'Go out to lunch/dinner', 'Hang out with someone you havent before', 'Meditate']
exercise = ['10 pushups', '10 jumping jacks', '10 burpees', '1 minute plank', '30 second jog on spot', '10 crunches', '30 pushups', '10 lunges', '1km run', '30 burpees', '1 minute side planks', '20 V sits', '15 situps', '5 pullups']
positions = ['You must fuck doggy style', 'Use missionary next time', 'Its time to scissor', '69 dinner for 2', 'Ride em cowgirl', 'Go reverse cowgirl', 'Use lotus blossum', 'The jack hammer', 'Go for it standing up']
truth = ['If you were the opposite sex for the day, what would you do?' 'What was your first sexual experience?', 'What do you hate most about yourself?', 'Do you hate anyone?', 'What is the worst thing you have ever done?', 'Do you regret anything?', 'Do like your best friend?', 'What is one thing you want to change about yourself?', 'First time your sick ass masturbated?']
dare = ['Fap on cam for other person playing game (If male-female or if it tickles your fancy)', 'Go streaking', 'Get nude pics off nearest girl, post results', 'Message 3 people with Would you hate me if I was gay?, post results', 'Send nudes', 'GFY', 'Think of a dare' ]
roll = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
###commands###
def command(Message, Status): 
 ##people commands##
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!yanz':
            Message.Chat.SendMessage('yanz is a fat cunt')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == 'nasin is':
            Message.Chat.SendMessage('the FATTEST cunt')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!penis':
            Message.Chat.SendMessage('Suck a penis.')
### truth or dare game ###
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!truth':
            from random import choice
            Message.Chat.SendMessage(choice(truth))
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!dare':
            from random import choice
            Message.Chat.SendMessage(choice(dare))
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!truthordare':
            Message.Chat.SendMessage('Use either !dare or !truth and do the dare or answer the question. Use !roll and highest number goes first')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!roll':
            from random import choice
            Message.Chat.SendMessage(choice(roll))
### yanzbot responders ###
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == 'fuck you yanzbot':
            Message.Chat.SendMessage('No fuck you cunt')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == 'nou':
            Message.Chat.SendMessage('nou faggot')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == 'fuck up yanzbot':
            Message.Chat.SendMessage('STFU kid')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!say hi':
            Message.Chat.SendMessage('Well.. Hello I guess?')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!ask wu':
            Message.Chat.SendMessage('Whats up?')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!tc':
            Message.Chat.SendMessage('Thats cool.')   
### actual commands ###
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!suicidewank':
            Message.Chat.SendMessage('Get something to fap to using !fappyget and then fap. When you are about to finish yell MUM DAD, HELP and finish before they come in')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == 'xspamspamspamx':
            Message.Chat.SendMessage('xspamspamspamx')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!help':
            Message.Chat.SendMessage('**************************************\n* !about - Displays about\n* !exercise - Random exercise\n* !truthordare - Play truth or dare \n* !done - Done fapping/exercise\n* !fappyget - Fap to something\n* !bored - Something to do\n* !sex - Displays sex position\n**************************************')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!done':
            Message.Chat.SendMessage('Well done! Try another!')
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!about':
            Message.Chat.SendMessage('**************************************\n** This bot was written in Python 2.7 by Yanz\n** This bot is not sentient\n** There will be more added to the bot\n** Always open to suggestions\n**************************************')
### choice commands ###   
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!exercise':
            from random import choice
            Message.Chat.SendMessage(choice(exercise))
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!sex':
            from random import choice
            Message.Chat.SendMessage(choice(positions))
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!fappyget':
            from random import choice
            Message.Chat.SendMessage(choice(fap))
    if Status == 'SENT' or (Status == 'RECEIVED'):
        if Message.Body == '!bored':
            from random import choice
            Message.Chat.SendMessage(choice(bored))

## connection to skype ##
skype = Skype4Py.Skype(); 
skype.OnMessageStatus = command 
if skype.Client.IsRunning == False: 
    skype.Client.Start() 
skype.Attach();  
while True: 
    raw_input('')