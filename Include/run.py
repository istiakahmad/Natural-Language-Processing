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
from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. " \
               "The sky is pinkish-blue. You shouldn't eat cardboard."

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
from nltk.corpus import stopwords

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
from nltk.stem import PorterStemmer

# ps = PorterStemmer()
# example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
# for w in example_words:
#     print(ps.stem(w))
#
# new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
# words = word_tokenize(new_text)
# for w in words:
#     print(ps.stem(w))

                                            #Part of Speech Tagging with NLTK
"""
Part of Speech tagging does exactly what it sounds like, it tags each word in a sentence with the part of speech 
for that word. This means it labels words as noun, adjective, verb, etc. 
PoS tagging also covers tenses of the parts of speech. 

This is normally quite the challenge, but NLTK makes this pretty darn simple! 

we're going to cover a new sentence tokenizer, called the PunktSentenceTokenizer. 
This tokenizer is capable of unsupervised machine learning, 
so you can actually train it on any body of text that you use. 

"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            """
            Chinking
            }<VB.?|IN|DT|TO>+{
            This means we're removing from the chink one or more verbs, prepositions, determiners, or the word 'to'. 
            """
            chunkGram = r"""Chunk: {<.*>+}
                                            }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            chunked.draw()
    except Exception as e:
        print(str(e))
process_content()

                                                    # Chunking with NLTK

"""
Chunking in Natural Language Processing (NLP) is the process by which 
we group various words together by their part of speech tags. 

One of the most popular uses of this is to group things by what are called "noun phrases." 
We do this to find the main subjects and descriptive words around them, 
but chunking can be used for any combination of parts of speech.
"""

                                                    # Chinking with NLTK

"""
Chinking is a lot like chunking, it is basically a way for you to remove a chunk from a chunk. The chunk that 
you remove from your chunk is your chink.
"""

