import re
import sys

import nltk

# from nltk.corpus import stopwords
#
# nltk.download('stopwords')
# stops = set(stopwords.words('english'))

stops= {'had', 'him', "isn't", "shan't", 'yourself', 'will', 'couldn', 'hadn', "shouldn't", 'his',
        'below', 'between', 'other', 'd', 'been', 'its', 'too', 're', "you've", 'they', 'against',
        'these', "don't", 'her', 'won', 'o', 'again', "it's", 'aren', "didn't", 'some', 'we', 'a',
        'through', 'doesn', "hasn't", 'or', 'me', 'an', 'herself', 'all', 'your', 'by', 'ourselves',
        "wasn't", 'did', "wouldn't", 'once', 'she', 'is', 'from', 'it', 'how', 'what', 'll', 'mightn',
        'for', 've', 'now', 'most', 'up', 'hasn', "you're", 'you', 'that', 'on', 'so', 'who', "mightn't",
        'not', 'during', 'further', "haven't", 'them', 'than', "should've", 'their', 'and', 'didn', 'just',
        'itself', 'there', "aren't", "she's", 'each', 'own', 'only', 'which', 'above', 'as', 'needn',
        'where', 'yours', 'should', 'until', 'the', 'he', 's', 'be', 'off', 'no', "won't", 'ma', 'theirs',
        "needn't", 'out', 'after', "couldn't", 'were', 'down', 'at', 'themselves', 'of', 'in', 'any', 'about',
         'i', 'then', 'before', 'do', 'with', 'few', 'ain', 'mustn', "that'll", 'nor', 'ours', 'm', 'same',
        'wouldn', 'this', 'here', 'hers', 'whom', 'under', 'if', 'myself', 'because', 'was', 'doing', 'don',
        'having', 'being', 'isn', 'those', 'am', 'himself', 'both', 'more', "doesn't", 'haven', 'why', 'have',
        'but', 'to', "you'll", 'does', 'wasn', 'while', 'my', 'are', 'our', "you'd", 'shouldn', "mustn't",
        'weren', 'such', 'shan', 'yourselves', 'very', "weren't", 'into', 'when', 't', 'has', 'y', "hadn't",
        'can', 'over'}
# print(stops)

def index_file(file_name: str, max_words: int = 20) -> list[tuple[str, int]]:
    word_counts = {}
    with open(file_name, mode='rt', encoding='utf-8') as f:
        for line in f:
            words = re.split(r'\W+', line)
            for word in words:
                word = word.lower()
                if word in stops or len(word) < 3:
                    continue
                word_counts[word] = word_counts.get(word, 0) + 1
        wc_items: list[tuple[str, int]] = list(word_counts.items())
        wc_items.sort(key=lambda t: t[1], reverse=True)
    return wc_items[:max_words]

if __name__ == '__main__':
    print(str(sys.argv))
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "wikipedia.txt"
    for word_count in index_file(filename, 15):
        print(f'{word_count[0]:30s} -> {word_count[1]:4d}')