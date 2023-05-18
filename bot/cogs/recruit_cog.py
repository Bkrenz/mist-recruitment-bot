import os
import re
import traceback
import logging

from discord.ext import commands
from discord.commands import SlashCommandGroup

from ..recruitment.recruitment_service import RecruitmentService


class RecruitCog(commands.Cog, name="Recruit"):
    """Mist Bot's interaction with the Recruit Webhook"""

    mist_admin_group= SlashCommandGroup('mist', 'Mist Admin commands')
    recruit_group = mist_admin_group.create_subgroup('apps', 'Applicant Commands')

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.RECRUIT_WEBHOOK_ID = int(os.getenv("RECRUIT_WEBHOOK_ID"))
        self.RECRUIT_CATEGORY_ID = int(os.getenv("RECRUIT_CATEGORY_ID"))


    @recruit_group.command(description='Create a channel for the Applicant.')
    async def app(self, ctx: commands.Context, applicant_id: str):
        """Looks up an applicant by ID"""
        await RecruitmentService.generate_recruit_channel(app_id=applicant_id, guild=ctx.guild)
        await ctx.respond('Printed app data.')
        


def setup(bot: commands.Bot):
    bot.add_cog(RecruitCog(bot))
