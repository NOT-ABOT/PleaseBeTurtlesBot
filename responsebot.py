import praw, time, re, sqlite3

############################################################################################
#This needs to be filled in manually                                                       #
############################################################################################

user_agent = ''
app_id = ''
app_secret = ''
app_uri = ''
app_scopes = ''
refresh_token = ''

sub = ''
maxposts = 100
username = ''
response = 'Today\'s fish is trout a la creme. Enjoy your meal'

print('Retrieving Databse...')
database = sqlite3.connect('database.db')
cur = database.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS answered(id TEXT)')
database.commit()

def login():
    r = praw.Reddit(user_agent)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(refresh_token)
    return r

disclaimer = '''\n\n
*I am a bot, and this was done automatically. If you have any questions or concerns
regarding the actions of this bot, please [message the owner of this](https://www.reddit.com/message/compose/?to=pleasebeturtles).
If you would like a bot of your own, feel free to [message the creator of this bot](https://www.reddit.com/message/compose/?to=___NOT_A_BOT___)'''

def comment_reply():
    comments = r.get_subreddit(sub).get_comments(limit=maxposts)
    for comment in comments:
        cur.execute('SELECT * FROM answered WHERE ID=?', [comment.id])
        if not cur.fetchone():
            try:
                author = comment.author.name
                if author.lower() != username.lower():
                    comment_text = comment.body.lower()
                        if re.match('[Ff]ish(.*)', comment_text):
                            comment.reply(response +  disclaimer)
                            cur.execute('INSERT INTO answered VALUES(?)', [comment.id])
                            database.commit()
                        else:
                            pass
            except AttributeError:
                pass
r
load = 1
while True:
    print('Scanning...')
    comment_reply()
    load += 1
    time.sleep(2)
    if load == 1800:
        r
