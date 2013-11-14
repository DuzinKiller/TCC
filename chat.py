import aiml

bot = aiml.Kernel()

bot.learn("startup.xml")
bot.learn("startup2.xml")
bot.respond('load')

bot.respond('Seja Bem-Vindo! Em que posso ajudar ?')

while True: print bot.respond(raw_input("> "))
