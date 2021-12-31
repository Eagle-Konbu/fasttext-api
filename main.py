from gensim.models import fasttext
import re
import time

print("Loading...")
start = time.time()
model = fasttext.load_facebook_vectors("cc.ja.300.bin")
end = time.time()
print("Loaded.")
print(f"time: {end-start}")
print()

while True:
    positive_words = []
    negative_words = []
    input_text = input("単語を入力 > ")
    if input_text == "end": break

    negative_flg = False
    str_tmp = ""
    for c in input_text:
        if c == '+' or c == '-':
            if negative_flg:
                negative_words.append(str_tmp)
            else:
                positive_words.append(str_tmp)
            str_tmp = ""
            negative_flg = (c == '-')
            continue
        str_tmp += c
    if negative_flg:
        negative_words.append(str_tmp)
    else:
        positive_words.append(str_tmp)
    
    positive_words = [word for word in set(positive_words) if len(word) > 0]
    negative_words = [word for word in set(negative_words) if len(word) > 0]

    start = time()
    ans = [{'word': x[0], 'similarity': x[1]} for x in model.most_similar(positive=positive_words, negative=negative_words, topn=30)]
    end = time()
    print(ans)
    print(f"time: {end-start}s")
