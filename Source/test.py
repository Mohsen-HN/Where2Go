import instaloader

# Get instance
L = instaloader.Instaloader()


# # Optionally, login or load session
# L.login('USER', 'PASSWORD')        # (login)
# L.interactive_login('USER')      # (ask password on terminal)
# L.load_session_from_file('USER') # (load session created w/
#                                #  `instaloader -l USERNAME`)

i = 0 
for post in instaloader.Hashtag.from_name(L.context, 'genevatravel').get_posts():
    # post is an instance of instaloader.Post
    L.download_post(post, target='#genevatravel')
    i += 1
    if i > 10:
        exit()