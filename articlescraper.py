import requests
import jieba
import jieba.posseg as pseg
import re
from bs4 import BeautifulSoup

def parse_article(URL, hashmap):
    # test_URL = "https://www.bbc.com/zhongwen/simp"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("h3")
    headlines = []
    for result in results:
        result = result.text

        # removing artefacts in headlines 
        result=re.sub(r"视频, ", "", result)
        result=re.sub(r"代理服务器和翻墙软件", "", result)
        result=re.sub(r"观察：", "", result)
        result=re.sub(r"BBC", "", result)
        headlines.append(result)

    for str in headlines:
        seg_list = pseg.lcut(str)

        # pos indicates the parts of speech 
        for char, pos in seg_list:
            if pos in ["nz","nr","ns","ORG","TIME","l","eng"] and len(char) != 1:
                hashmap[char] = hashmap.get(char, 0) + 1
    
    return hashmap
    
if __name__ == "__main__":
    test_url = "https://www.bbc.com/zhongwen/simp"
    test_hashmap = {}
    print(parse_article(test_url, test_hashmap))
    