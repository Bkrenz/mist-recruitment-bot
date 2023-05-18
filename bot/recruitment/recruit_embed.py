import discord

class RecruitEmbed:

    class_colors =  {
        'DeathKnight' :  0xC41E3A,
        'DemonHunter' :  0xA330C9,
        'Druid' :  0xFF7C0A,
        'Evoker' :  0x33937F,
        'Hunter' :  0xAAD372,
        'Mage' :  0x3FC7EB,
        'Monk' :  0x00FF98,
        'Paladin' :  0xF48CBA,
        'Priest' :  0xFFFFFF,
        'Rogue' :  0xFFF468,
        'Shaman' :  0x0070DD,
        'Warlock' :  0x8788EE,
        'Warrior' :  0xC69B6D
    }

    @staticmethod
    def get_embed(applicant):
        embed = discord.Embed(title=f"{applicant['character_name']}",
                              description=applicant['character_name'],
                              color=RecruitEmbed.class_colors[applicant['wow_class']])

        # name/age/bnet
        embed.add_field(name="✍️ Name",
                        value=f"{applicant['character_name']}",
                        inline=True)
        embed.add_field(name="🔞 Age",
                        value=f"{applicant['age']}",
                        inline=True)
        embed.add_field(name="<:bnet:1070180625430089728> Battle.net",
                        value=f"{applicant['battlenet_contact']}",
                        inline=True)
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)
        
        

        # discord/class/spec
        embed.add_field(name="<:discord:1070180627028131870> Discord",
                        value=f"{applicant['discord_contact']}",
                        inline=True)
        embed.add_field(name=f"Class",
                        value=f"{applicant['wow_class']}",
                        inline=True)
        embed.add_field(name="⚔️ Spec",
                        value=f"{applicant['primary_spec']}",
                        inline=True)
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)

        # links
        embed.add_field(name="<:wcl:1070180727892758608> WCL",
                        value=f"[Click Here]({applicant['warcraftlogs_link'].split(' ')[0]})",
                        inline=True)
        embed.add_field(name="<:rio:1070180628131225732> R.IO",
                        value=f"[Click Here]({applicant['raiderio_link']})",
                        inline=True)
        embed.add_field(name="<:wow:1070181155279745094> WCA",
                        value=f"[Click Here]({applicant['armory_link']})",
                        inline=True)
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)

        # real life
        embed.add_field(name="📖 Tell us about yourself in real life!",
                        value=f"{applicant['real_life_summary']}",
                        inline=False)
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)

        # skills summary
        embed.add_field(name="🎯 What experience, skill, and attitude will you bring to the guild?",
                        value=f"{applicant['skills_summary']}",
                        inline=False)
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)

        # proclivity
        embed.add_field(name="🎮 How often do you play WoW?",
                        value=f"{applicant['proclivity_summary']}",
                        inline=False)
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)

        # pizza question
        embed.add_field(name="🍕 Does pineapple belong on pizza?",
                        value=f"{applicant['pizza_question']}",
                        inline=False)

        # footer
        embed.set_footer(text="Mist Recruiting",
                         icon_url="https://raw.githubusercontent.com/mist-guild/mist-rustbolt/master/public/logo192.png")
        
        embed.add_field(name = chr(173), value = chr(173), inline=False)

        return embed