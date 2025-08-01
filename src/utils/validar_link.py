import re

def validar(url):
    regex1 = r"https:\/\/www\.tiktok\.com\/@[\w.-]+\/video\/\d+(\?.*)?"
    regex2 = r"https:\/\/(vm|www)\.tiktok\.com\/[A-Za-z0-9]+\/?"

    if re.fullmatch(regex1, url) or re.fullmatch(regex2, url):
        return 200
    else:
        return 404
