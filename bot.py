import discord
import requests
import io

DISCORD_BOT_TOKEN = "MTM5NjkyNzg4Nzc4OTI2NDk0Nw.GvDfcn.re-SA6ITwru1I6dbM0FdoQngVjy5yrGQRhVgFU"
HF_API_TOKEN = "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"

# Use any text-to-image model (you can change the model URL)
HF_MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

headers = {"Authorization": f"Bearer {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}"}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!generate "):
        prompt = message.content[len("!generate "):]
        await message.channel.send("Generating image...")

        response = requests.post(HF_MODEL_URL, headers=headers, json={"inputs": prompt})

        if response.status_code == 200:
            image_data = response.content
            image_file = discord.File(io.BytesIO(image_data), filename="output.png")
            await message.channel.send(file=image_file)
        else:
            await message.channel.send("Error generating image. Try again later.")

client.run(MTM5NjkyNzg4Nzc4OTI2NDk0Nw.GvDfcn.re-SA6ITwru1I6dbM0FdoQngVjy5yrGQRhVgFU)
