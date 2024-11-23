import random
voorvoegsel = ["super ","snap ","the ","big ","mine","fort","poppy ","hello ","tik","docter "]
achtervoegsel = ["man","chat", "watcher","mac","craft","night","playtime","neighbor","tok","strane"]
for i in range(10):
    samen = random.choice(voorvoegsel) + random.choice(achtervoegsel)

    print("random samenvoegsel " + samen)