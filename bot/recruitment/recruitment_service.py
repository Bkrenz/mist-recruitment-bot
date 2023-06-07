import os
import discord
from ..api.mist_api import Mist
import json
from discord.ext import commands

from .recruit_embed import RecruitEmbed

class RecruitmentService:
    
    recruit_category = int(os.getenv('RECRUIT_CATEGORY_ID'))


    @staticmethod
    async def generate_recruit_channel(app_id: str, guild: discord.Guild):
        app_json = json.loads(Mist.get_applicant_by_id(app_id))
        char_name = app_json['character_name'].split('-')[0]

        category = discord.utils.get(guild.categories, id=RecruitmentService.recruit_category)
        channel = await guild.create_text_channel(f'{app_id}-{char_name}', category=category)

        embed = RecruitEmbed.get_embed(app_json)

        await channel.send(embed=embed)

        # Check if there is an archive for this app
        if os.path.isfile(f'archive/{app_id}-{char_name}.txt'):
            with open(f'archive/{app_id}-{char_name}.txt', encoding='utf-32') as f:
                message = ''
                for line in f:
                    message += line.strip() + '\n'
                    if len(message) > 1800:
                        await channel.send(message)
                        message = ''
                if len(message) > 0:
                    await channel.send(message)


    @staticmethod
    async def archive_channel(ctx: commands.Context, bot_id: int):
        channel = ctx.channel
        file_name = f'archive/{ctx.channel.name}.txt'
        archived_messages = []
        current_author = None
        async for message in channel.history(oldest_first=True, limit=None):
            if message.author.id == bot_id:
                continue
            if current_author is None or current_author != message.author:
                current_author = message.author
                archived_messages.append(f"\n**{message.author}**\n")
            archived_messages.append(f"{message.content}\n")
        
        with open(file_name, 'w', encoding='utf-32') as f:
            for message in archived_messages:
                f.write(message)