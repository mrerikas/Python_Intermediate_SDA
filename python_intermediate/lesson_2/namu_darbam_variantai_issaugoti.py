import json


# 1 variantas
class JsonDBManager:
    def __enter__(self):
        global DB
        from os.path import exists
        if exists("DB.json"):
            with open("DB.json") as f:
                DB = json.load(f)
        else:
            DB = {}

    def __exit__(self, exc_type, exc_val, exc_tb):
        global DB
        with open("DB.json", 'w') as f:
            f.write(json.dumps(DB, ensure_ascii=False))


with JsonDBManager():
    DB['raktas'] = "vertė"
    DB['raktas_2'] = "vertė_5"
    exit(1)
# 2 variantas
import atexit


def persist_database():
    with open("DB.json", 'w') as f:
        f.write(json.dumps(DB, ensure_ascii=False))


atexit.register(persist_database)
