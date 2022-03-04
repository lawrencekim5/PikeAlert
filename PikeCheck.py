import discord
import random
from discord.ext import commands

## member join and leave functions
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True, voice_states = True)
client = commands.Bot(command_prefix = "&", intents = intents)

## Detecting Users Joining a Voice Call
@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel and member.id == <memberid>: # Detects when the specified member joins the voice channel. Set member.id to the id of the member to be detected (use developer mode in discord to copy ids).

        channel = client.get_channel(<channelid>) # Set the channel for alerts to be made in.
        
        # Customize responses or actions here.
        responses = [
                f"@everyone PIKE DETECTED",
                f"@everyone PIKE SIGHTED",
                f"@everyone PIKE ALERT",
                f"@everyone PIKE CHECK"
        ]
        await channel.send(f"{random.choice(responses)}",file=discord.File(r'/home/voip/Desktop/PikeCheck/PikePlanted.wav'))

# Bot commands using command_prefix. Not necessary.
@client.command()
async def test(ctx):
    await ctx.send(f"I'm working right now!")

client.run("<bot_API_token_goes_here>")
