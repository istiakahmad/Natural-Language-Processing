from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. " \
               "The sky is pinkish-blue. You shouldn't eat cardboard."


"""
Tokenizing - Splitting sentences and words from the body of text.

Corpus - Body of text, singular. Corpora is the plural of this. Example: A collection of medical journals.

Lexicon - Words and their meanings. Example: English dictionary. Consider, however, that various fields will have 
different lexicons. For example: To a financial investor, the first meaning for the word "Bull" is someone who is 
confident about the market, as compared to the common English lexicon, where the first meaning for the word "Bull" 
is an animal. As such, there is a special lexicon for financial investors, doctors, children, mechanics, and so on.

Token - Each "entity" that is a part of whatever was split up based on rules. For examples, each word is a token when 
a sentence is "tokenized" into words. Each sentence can also be a token, if you tokenized the sentences out of a paragraph.

"""

# print("split up into a list of sentences:")
# print(sent_tokenize(EXAMPLE_TEXT))

# print("tokenize by word:")
# print(word_tokenize(EXAMPLE_TEXT))

"""
we can recognize ourselves that some words carry more meaning than other words. We can also see that some words are 
just plain useless, and are filler words.

we call these words "stop words" because they are useless, and we wish to do nothing with them.
Another version of the term "stop words" can be more literal: Words we stop on.

NLTK starts you off with a bunch of words that they consider to be stop words, 
you can access it via the NLTK corpus with:
"""
# print("stopwords Lists: "+ str(set(stopwords.words('english'))))
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(EXAMPLE_TEXT)

# filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# filtered_sentence = []
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print(word_tokens)
# print(filtered_sentence)


"""
The idea of stemming is a sort of normalizing method. Many variations of words carry the same meaning, 
other than when tense is involved.

The reason why we stem is to shorten the lookup, and normalize sentences.

One of the most popular stemming algorithms is the Porter stemmer, which has been around since 1979.
"""
ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))


