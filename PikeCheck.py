import discord
import random
from discord.ext import commands

## member join and leave functions
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True, voice_states = True)
client = commands.Bot(command_prefix = "&", intents = intents)

## Detecting Users Joining a Voice Call
@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel and member.id == 514662157116243998: # Detects when the specified member joins the voice channel. Change member.id to the id of the Member to be detected (use developer mode in discord to copy ids)
        await member.voice.channel.connect()
        channel = client.get_channel(279720195830972416) # Set the channel for alerts to be made in.
        responses = [
                f"@everyone PIKE DETECTED",
                f"@everyone PIKE SIGHTED",
                f"@everyone PIKE ALERT",
                f"@everyone PIKE CHECK"
        ]
        await channel.send(f"{random.choice(responses)}",file=discord.File(r'/home/voip/Desktop/PikeCheck/PikePlanted.wav'))
        
@client.command()
async def status(ctx):
    await ctx.send(f"Standing by. Pike Detection is online.")

# Keyword events
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "pike is gone" in message.content.lower():
        responses = [
                f"Confirmed.",
                f"Roger that.",
                f"Affirmative.",
                f"Very well.",
                f"Affirmed.",
                f"Verified.",
                f"Processed.",
                f"Received."
        ]

        await message.channel.send(f"{random.choice(responses)}")
        await message.guild.voice_client.disconnect()
    await client.process_commands(message)


client.run("tokengoeshere")
