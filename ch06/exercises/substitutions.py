import json
def main():
    file = open("news.txt")
    fileraw = file.read()
    news = str(fileraw)
    jsonfile = open("subs.json")
    subs = json.load(jsonfile)
    betternews = news
    for key in subs:
        betternews = betternews.replace(key, subs[key])
    print(betternews)
    newfile = open("betternews.txt", "w")
    newfile.write(betternews)
main()