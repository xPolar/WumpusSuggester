import datetime
import discord
from discord.ext import commands

class other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.errorcolor = 0xFF2B2B
        self.blurple = 0x7289DA

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def prefix(self, ctx, *, pre):
        with open(r"PREFIXESJSONFILEPATHHERE", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        embed = discord.Embed(
            title = "Prefix",
            description = f"{ctx.message.guild}'s prefix is  now `{pre}`",
            color = self.blurple
        )
        await ctx.send(embed = embed)

        with open(r"PREFIXESJSONFILEPATHHERE", "w") as f:
            json.dump(prefixes, f, indent = 4)

    @commands.command()
    async def help(self, ctx, module = None):
        if message.guild == None:
            pass
        else:
            with open(r"PREFIXESJSONFILEPATHHERE", "r") as f:
                prefixes = json.load(f)
            if str(message.guild.id) not in prefixes:
                prefix = "s!"
            else:
                prefix = prefixes[str(message.guild.id)]
        if module == None:
            embed = discord.Embed(
                title = "Suggestion",
                description = "`9 total commands`",
                timestamp = datetime.datetime.utcnow(),
                color = self.blurple
            )
            embed.set_author(name = "Categorys")
            embed.add_field(name = "Other", value = "`6 total commands`")
            embed.footer(text = f"For more information on each category do {prefix}help (Category)")
            await ctx.send(embed = embed)
        else:
            if module.lower() == "suggestion":
                embed = discord.Embed(
                    title = "Commands",
                    description = "**Suggest** - Make a suggestion.\n**Approve / Accept** - Approve a suggestion.\n**Deny** - Deny a suggestion.\n**Consider / Maybe** - Consider a suggestion.\n**Implement** - Implement a suggestion.\n**Note** - Add a note to a suggestion.\n**Suggestionchannel** - Set the channel where suggestions are sent.\n**Suggestionlogchannel** - Set the channel where all suggestion related actions will be sent.\n**Staffrole** - Set the role which can accept, deny, etc to suggestions.\n**",
                    timestamp = datetime.datetime.utcnow(),
                    color = self.blurple
                )
                embed.set_author(name = "Suggestion")
                embed.footer(text = f"For more information on each command do {prefix}help (Command)")
                await ctx.send(embed = embed)
            elif module.lower() == "other":
                embed = discord.Embed(
                    title = "Commands",
                    descripton = "**Help** - Shows this message.\n**Prefix** - Set the bot's prefix.\n**Support** - Send a link to the support server.\n**Invite** - Send a link to invite the bot.\n**Github** - Send a link to view the github.\n**Leave** - Makes the bot leave the server so you don't have to kick it.\n**Ping** - Shows the bot's current ping.",
                    timestamp = datetime.datetime.utcnow(),
                    color = self.blurple
                )
                embed.set_author(name = "Other")
                embed.footer(text = f"For more information on each command do {prefix}help (Command)")
            else:
                if module.lower() == "suggest":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Make a suggestion to the current server you are in.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Suggest")
                    embed.add_field(name = "Usage", value = f"{prefix}suggest (Suggestion)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "approve" or module.lower() == "accept":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Mark a suggestion as approved.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Approve")
                    embed.add_field(name = "Usage", value = f"{prefix}approve (Suggestion ID) (Reason)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "deny":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Mark a suggestion as denied.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Deny")
                    embed.add_field(name = "Usage", value = f"{prefix}deny (Suggestion ID) (Reason)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "consider" or module.lower() == "maybe":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Mark a suggestion as considered.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Consider")
                    embed.add_field(name = "Usage", value = f"{prefix}consider (Suggestion ID) (Reason)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "implement":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Mark a suggestion as implemented.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Implement")
                    embed.add_field(name = "Usage", value = f"{prefix}implement (Suggestion ID) (Reason)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "note":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Add a note to a suggestion.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Note")
                    embed.add_field(name = "Usage", value = f"{prefix}note (Suggestion ID) (Note)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "suggestionchannel":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Set which channel suggestions should be sent to.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Suggestionchannel")
                    embed.add_field(name = "Usage", value = f"{prefix}suggestionchannel (Channel)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "suggestionlogchannel":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Set which channel suggestion related logs should be sent to.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Suggestionlogchannel")
                    embed.add_field(name = "Usage", value = f"{prefix}suggestionlogchannel (Channel)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "staffrole":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Set which role can deny and accept suggestions.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Staffrole")
                    embed.add_field(name = "Usage", value = f"{prefix}staffrole (Role)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "prefix":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Set the server's prefix.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Prefix")
                    embed.add_field(name = "Usage", value = f"{prefix}prefix (New Prefix)")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "support":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Send an invite link to the support server.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Support")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "invite":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Send an invite link to invite the bot.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Invite")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "github":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Send a link to view the Github.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Github")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)
                elif module.lower() == "leave":
                    embed = discord.Embed(
                        title = "Description",
                        description = "Makes the bot leave the server so you don't have to kick it.",
                        timestamp = datetime.datetime.utcnow(),
                        color = self.blurple
                    )
                    embed.set_author(name = "Leave")
                    embed.set_footer(name = f"For more help feel free to join the support server with {prefix}support!")
                    await ctx.send(embed = embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Feel free to invite me!",
            url = "https://discordapp.com/api/oauth2/authorize?client_id=606307707334426654&permissions=8&scope=bot",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            title = "Feel free to join the support server!",
            url = "https://discord.gg/r6e3CNq",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    #Ping command
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title = f"Pong! {round(self.bot.latency * 1000)} ms",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    #Leave command
    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def leave(self, ctx):
        embed = discord.Embed(
            title = "Leave",
            description = "I have left this server, please let the devs know why you wanted to remove the bot by joining the [Support Server](https://discordapp.com/invite/tjA5ssJ).",
            color = self.errorcolor
        )
        await ctx.send(embed = embed)
        await ctx.guild.leave()

    @commands.command()
    async def github(self, ctx):
        embed = discord.Embed(
            title = "Feel free to view the github!",
            url = "https://github.com/xPolar/WumpusSuggester",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    @leave.error
    async def leave_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You are missing the **Manage Server** permission!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(other(bot))
