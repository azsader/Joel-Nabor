from disnake.ext import commands
import disnake
from main import config
class Application(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot=bot
    class Application_Modal(disnake.ui.Modal):
            def __init__(self):
                super().__init__('Набор в клан')

                self.EmTitle = disnake.ui.TextInput(label = 'Ваше имя и возраст', min_length=4, max_length=50, required=True, placeholder='Георгий, 18 лет', style=disnake.TextInputStyle.paragraph)
                self.add_item(self.EmTitle)

                self.EmDescription = disnake.ui.TextInput(label = 'Ваш часовой пояс', min_length=3, max_length=10, required=True, placeholder='МСК', style=disnake.TextInputStyle.paragraph)
                self.add_item(self.EmDescription)

                self.EmFooter = disnake.ui.TextInput(label = 'Расскажите о себе и почему именно вы?', min_length=25, max_length=500, required=True, placeholder='Я довольно трудолюбивый! Я считаю что именно я должен попасть на эту должность.', style=disnake.TextInputStyle.paragraph)
                self.add_item(self.EmFooter)

    @commands.slash_command(description='Отправляет сообщение о заявке в указанный канал')
    async def embed(self, inter, channel: disnake.channel):
        await inter.channel.send(embed=disnake.Embed(
            title='Набор в клан!',
            description=config["texts"]["text_embed"]),

            components=[
                disnake.ui.Button(label="Подать заявку", style=disnake.ButtonStyle.gray, id='application')
            ])
    @commands.Cog.listener()
    async def button_listener(inter):
        c=inter.component.custom_id
        if c not in ['add', 'refusal', 'application']