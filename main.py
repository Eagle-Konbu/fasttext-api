from gensim.models import fasttext
from gensim.test.utils import datapath

import time
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


print("Loading...")
start = time.time()
model = fasttext.load_facebook_vectors("cc.ja.300.bin")
end = time.time()
print("Loaded.")
print(end - start)
print()


@app.route('/generate_words', methods=['POST'])
def generate_words():
    data = request.json
    print(data)

    positive_words = data['positive']
    negative_words= data['negative']
    topn = data['topn']

    ans = model.most_similar(positive=positive_words, negative=negative_words, topn=topn)
    ans = [{'word': x[0], 'similarity': x[1]} for x in ans]
    return jsonify({'data': ans})


app.run(debug=False, host='0.0.0.0')
