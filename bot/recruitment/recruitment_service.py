import os
import discord
from ..api.mist_api import Mist
import json

from .recruit_embed import RecruitEmbed

class RecruitmentService:
    
    recruit_category = int(os.getenv('RECRUIT_CATEGORY_ID'))

    @staticmethod
    def generate_recruit_text_channel(message: discord.Message):
        embed = message.embeds[0]
        guild = message.guild
        app_id = embed.title.split(' ')[-1]
        app_data = Mist.get_applicant_by_id(app_id)


    @staticmethod
    async def generate_recruit_channel(app_id: str, guild: discord.Guild):
        app_json = json.loads(Mist.get_applicant_by_id(app_id))
        char_name = app_json['character_name'].split('-')[0]

        category = discord.utils.get(guild.categories, id=RecruitmentService.recruit_category)
        channel = await guild.create_text_channel(f'{app_id}-{char_name}', category=category)

        embed = RecruitEmbed.get_embed(app_json)
        await channel.send(embed=embed)
        
        
        