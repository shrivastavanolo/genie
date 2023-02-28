from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Genie")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.custom")
exit_conditions = ("q", "quit", "exit","bye","ok thanks","ok bye")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {bot.get_response(query)}")