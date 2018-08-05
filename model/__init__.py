
import os

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


EnglishBot = ChatBot("Chatterbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database='./db/database.sqlite3',
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

EnglishBot.set_trainer(ChatterBotCorpusTrainer)

if not os.path.exists("./db/database.sqlite3"):
    EnglishBot.train("chatterbot.corpus.english")


EnglishBot.set_trainer(ListTrainer)
