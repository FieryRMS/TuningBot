ctftime_help = '''

`{prefix}ctftime upcoming [1-5]`
return info on a number of upcoming ctfs from ctftime.org

`{prefix}ctftime current`
return info on the currently running ctfs on ctftime.org

`{prefix}ctftime [countdown/timeleft]`
return specific times for the time until a ctf begins, or until a currently running ctf ends.

`{prefix}ctftime top [year]`
display the leaderboards from ctftime from a certain year.
'''

ctf_help = '''

`{prefix}ctf create "CTF NAME"`
create a text channel and role in the CTF category for a ctf (must have permissions to manage channels)*

`{prefix}ctf challenge [add/working/solved/remove] "challenge name"`
add a ctf challenge to a list of challenges in the ctf, then mark it as solved or being worked on.  Shorthand: challenge -{prefix} chal/chall, add -{prefix} a, working -{prefix} w, solved -{prefix} s, remove -{prefix} r

`{prefix}ctf challenge list`
get a list of the challenges in the ctf, and their statuses.

`{prefix}ctf challenge pull [https://ctfd.url]`
will add all of the challenges on the provided CTFd CTF and add them to your challenge list, including solve state.

`{prefix}ctf setcreds [ctfd username] [password]`
pin the message of ctf credentials, can be fetched by the bot later in order to use {prefix}ctf challenge pull.

`{prefix}ctf creds`
gets the credentials from the pinned message.

`{prefix}ctf [join/leave]`
give the user the role of the ctf channel they are in.

`{prefix}ctf archive`
move the ctf channel to the archive category.

`{prefix}ctf delete`
delete the ctf role, and entry from the database for the ctf (must have permissions to manage channels)*
'''

config_help = '''

`{prefix}config ctf_category "CTF CATEGORY"`
specify the category to be used for CTF channels, defaults to "CTF".

`{prefix}config archive_category "ARCHIVE CATEGORY"`
specify the category to be used for archived CTF channels, defaults to "Archive".
'''

utility_help = '''
`{prefix}magicb [filetype]`
return the magicbytes/file header of a supplied filetype.
`{prefix}rot "message"`
return all 25 different possible combinations for the popular caesar cipher - use quotes for messages more than 1 word
`{prefix}b64 [encode/decode] "message"`
encode or decode in base64 - if message has spaces use quotations
`{prefix}b32 [encode/decode] "message"`
encode or decode in base32 - if message has spaces use quotations
`{prefix}binary [encode/decode] "message"`
encode or decode in binary - if message has spaces use quotations
`{prefix}hex [encode/decode] "message"`
encode or decode in hex - if message has spaces use quotations
`{prefix}url [encode/decode] "message"`
encode or decode based on url encoding - if message has spaces use quotations
`{prefix}reverse "message"`
reverse the supplied string - if message has spaces use quotations
`{prefix}counteach "message"`
count the occurences of each character in the supplied message - if message has spaces use quotations
`{prefix}characters "message"`
count the amount of characters in your supplied message
`{prefix}wordcount "phrase"`
count the amount of words in your supplied message
`{prefix}atbash "message"`
encode or decode in the atbash cipher - if message has spaces use quotations (encode/decode do the same thing)
`{prefix}github [user]`
get a direct link to a github profile page with your supplied user
`{prefix}twitter [user]`
get a direct link to a twitter profile page with your supplied user
`{prefix}cointoss`
get a 50/50 cointoss to make all your life's decisions
`{prefix}amicool`
for the truth.
'''


help_page = '''

`{prefix}help ctftime`
info for all ctftime commands

`{prefix}help ctf`
info for all ctf commands

`{prefix}help config`
bot configuration info

`{prefix}help utility`
everything else! (basically misc)

`{prefix}report/request "an issue or feature"`
report an issue, or request a feature for NullCTF, if it is helpful your name will be added to the 'cool names' list!
'''


src = "https://github.com/NullPxl/NullCTF"
