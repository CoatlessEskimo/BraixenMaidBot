# FennecBot
### The project that will eventually be turned into Free6

## Instructions
For this bot to work correctly, you need to create a file in the same directory, called ".env", and it must contain the following text:

```
# .env
DISCORD_TOKEN=yourdiscordtokengoeshere
```

This bot requires the following python libraries:
* random
* discord.py

Simply run the FennecBot.py file with python in your environment of choice, and enjoy!

## Automated Features

### Link Formatting

For reasons I can't be bothered to research, links that use 'media.discordapp.net' instead of 'cdn.discordapp.com' fail to embed properly. This bot detects these links and automatically deletes the message, fixes the link, and reposts the original message with the corrected link and a mention.

The bot can also convert other types of links, such as changing YouTube Shorts links into YouTube Video links, with more to come in the future.

### Link Filter

An NSFW link filter is included that only applies outside of NSFW channels. This list can be changed to include whatever links you prefer.

## Commands

`#!man` - Shows the help page.
`#!source` - Attaches the currently running source, in case GitHub goes down or the currently used revision is needed.
`#!github` - Attaches a link to this github repo.
`#!agpl` - Shows the GNU AGPL v3 notice.

`#!toggleNSFW` - Turns the NSFW filter on and off per server.
`#!toggleYT` - Turns off the YouTube Shorts filter per server.

`#!init` - Checks to see if required files are present, and creates them if they're not. (PENDING REMOVAL.)
`#!permission` - Tells user if they have admin or not. (PENDING REMOVAL.)
