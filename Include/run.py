"""
before we start with any NLP project we need to pre-process it to make it ideal for working.
Basic text pre-processing includes:

Converting the entire text into uppercase or lowercase,
so that the algorithm does not treat the same words in different cases as different

Tokenization: Tokenization is just the term used to describe the process of converting
the normal text strings into a list of tokens i.e words that we actually want.
Sentence tokenizer can be used to find the list of sentences
and Word tokenizer can be used to find the list of words in strings.

Tokenizing - Splitting sentences and words from the body of text.

Corpus - Body of text, singular. Corpora is the plural of this.
Generally, corpora are grouped by some sort of defining characteristic. Example: A collection of medical journals.

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
                                        # stop words
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

                                            # Stemming
"""
The idea of stemming is a sort of normalizing method. Many variations of words carry the same meaning, 
other than when tense is involved.
The reason why we stem is to shorten the lookup, and normalize sentences.
One of the most popular stemming algorithms is the Porter stemmer, which has been around since 1979.
Example if we were to stem the following words: “Stems”, “Stemming”, “Stemmed”, “and Stemtization”, 
the result would be a single word “stem”.
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

# def process_content():
#     try:
#         for i in tokenized[:5]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             # print(tagged)
#             #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#
#             """
#             Chinking
#             }<VB.?|IN|DT|TO>+{
#             This means we're removing from the chink one or more verbs, prepositions, determiners, or the word 'to'.
#             """
#             chunkGram = r"""Chunk: {<.*>+}
#                                             }<VB.?|IN|DT|TO>+{"""
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked = chunkParser.parse(tagged)
#
#             print(chunked)
#             for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
#                 print(subtree)
#
#             chunked.draw()
#     except Exception as e:
#         print(str(e))
# process_content()

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

                                                    # Named Entity Recognition with NLTK
'''
One of the most major forms of chunking in natural language processing is called "Named Entity Recognition.
" The idea is to have the machine immediately be able to pull out "entities" like people, places, things, locations,
 monetary figures, and more.

This can be a bit of a challenge, but NLTK is this built in for us. 
There are two major options with NLTK's named entity recognition: either recognize all named entities, 
or recognize named entities as their respective type, like people, places, locations, etc.
'''
#
# def process_content():
#     try:
#         for i in tokenized[5:]:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             namedEnt = nltk.ne_chunk(tagged, binary=True)
#             namedEnt.draw()
#     except Exception as e:
#         print(str(e))
# process_content()

                                        # Lemmatizing
from nltk.stem import WordNetLemmatizer
'''
A very similar operation to stemming is called lemmatizing. The major difference between these is, as you saw earlier, 
stemming can often create non-existent words, whereas lemmas are actual words.
So, your root stem, meaning the word you end up with, is not something you can just look up in a dictionary, 
but you can look up a lemma.
Examples of Lemmatization are that “run” is a base form for words like “running” or “ran” or 
that the word “better” and “good” are in the same lemma so they are considered the same.
Some times you will wind up with a very similar word, but sometimes, you will wind up with a completely different word. 
'''

# lemmatizer = WordNetLemmatizer()
#
# print(lemmatizer.lemmatize("cats"))     # Defualt parameter 'noun'
# print(lemmatizer.lemmatize("cacti"))     # Defualt parameter 'noun'
# print(lemmatizer.lemmatize("geese"))     # Defualt parameter 'noun'
# print(lemmatizer.lemmatize("rocks"))     # Defualt parameter 'noun'
# print(lemmatizer.lemmatize("pythons"))     # Defualt parameter 'noun'
# print(lemmatizer.lemmatize("better", pos="a"))     # Defualt parameter 'pos' parts of speech
# print(lemmatizer.lemmatize("best", pos="a"))
# print(lemmatizer.lemmatize("run"))
# print(lemmatizer.lemmatize("ran",'v'))      # ran past form of run

                                        # The corpora
# print(nltk.__file__)
from nltk.corpus import gutenberg    # C:\Users\ishan\AppData\Roaming\nltk_data\corpora  (TYPE %appdata% to find path)

# sample text
# sample = gutenberg.raw("bible-kjv.txt")

# tok = sent_tokenize(sample)
# # print(tok[5:15])
# for x in range(6):
#     print(tok[x])

                                        # Wordnet
'''
WordNet is a lexical database for the English language, which was created by Princeton, and is part of the NLTK corpus.
You can use WordNet alongside the NLTK module to find the meanings of words, synonyms, antonyms, and more.
'''

from nltk.corpus import wordnet

# syns = wordnet.synsets("program")
# print(syns[0].name())               # An example of a synset:
# print(syns[0].lemmas()[0].name())   # Just the word:
# print(syns[0].definition())         # Definition of that first synset:
# print(syns[0].examples())           # Examples of the word in use:

# synonyms and antonyms
# synonyms = []
# antonyms = []
# for syn in wordnet.synsets("bad"):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
# print(set(synonyms))
# print(set(antonyms))

# compare the similarity of two words and their tenses
# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('boat.n.01')
# print(w1.wup_similarity(w2))

                                    # TF-IDF Approach
'''
A problem with the Bag of Words approach is that highly frequent words start to dominate in the document 
(e.g. larger score), but may not contain as much “informational content”. 
Also, it will give more weight to longer documents than shorter documents.

One approach is to rescale the frequency of words by how often they appear in all documents 
so that the scores for frequent words like “the” that are also frequent across all documents are penalized. 
This approach to scoring is called Term Frequency-Inverse Document Frequency, or TF-IDF for short, where:

Term Frequency: is a scoring of the frequency of the word in the current document.
TF = (Number of times term t appears in a document)/(Number of terms in the document)

Inverse Document Frequency: is a scoring of how rare the word is across documents.
IDF = 1+log(N/n), where, N is the number of documents and n is the number of documents a term t has appeared in.
'''