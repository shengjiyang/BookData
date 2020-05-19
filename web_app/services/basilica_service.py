# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv
import pprint

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    print(type(connection))
    return connection


if __name__ == "__main__":
    
    print("---------")
    connection = basilica_api_client()

    print("---------")
    Hal9000 = "I'm sorry, Dave; I'm afraid I can't do that."
    embedding = connection.embed_sentence(Hal9000)
    print(Hal9000)
    print(type(embedding))
    print(list(embedding))

    print("---------")
    lines = ["Colorless green ideas sleep furiously",
             "...your computer has too much computer in it, and not enough typewriter",
             "Get ye flask",
             "You cannot get ye flask!"]

    print(lines)

    embeddings = connection.embed_sentences(lines)
    print("EMBEDDINGS...")
    print(type(embeddings))
    print(list(embeddings))

    chinese_sentence = "葉問：我要打十個！"
    print("---------")
    print(chinese_sentence)
    chinese_embeded = connection.embed_sentence(chinese_sentence)
    print(list(chinese_embeded))