import requests
from bs4 import BeautifulSoup
import time
import random

def fetch_word_sentences(word):
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    
    # 添加user-agent模擬瀏覽器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # 查找包含例句的HTML元素
            examples = soup.find_all("div", class_="examp dexamp")
            
            # 提取並打印例句
            sentences = []
            for example in examples:
                sentence = example.get_text().strip()
                if sentence[0].isupper() and sentence[-1] in [".", "!", "?"]:
                    sentences.append(sentence)
            
            return sentences
        else:
            print(f"Failed to fetch data for word: {word}, Status code: {response.status_code}")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

def get_sentence(word):#word list
    # 測試函數
    #word = "example"  # 可以替換成你想查詢的單字
    for i in word:
        sentences = fetch_word_sentences(i[0])

        # print(f"Sentences for the word '{word}':")
        if sentences:
            random_sentence = random.choice(sentences)
            #print(f"Random sentence for the word '{word}': {random_sentence}")
            i.append(random_sentence)
        else:
            #print(f"No sentences found for the word '{word}'")
            i.append("")
        # 添加隨機延遲避免被認為是惡意爬蟲
        time.sleep(random.uniform(1, 3))

# word=[['percentage', 'n.百分比 '], ['most', 'adj./adv.最大程度地 '], ['earthquake', 'n.地震 '], ['synonym', 'n.同義詞 '], ['relieve', 'v.減輕(痛苦) ']]
# example=[]
# get_sentence(word,example)
# print(word)