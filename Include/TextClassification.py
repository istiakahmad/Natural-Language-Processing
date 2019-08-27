
                                        # Text Classification
import random
from nltk.corpus import movie_reviews

'''
Movie Reviews datasets
the code is translated to: In each category (we have pos or neg), 
take all of the file IDs (each review has its own ID), 
then store the word_tokenized version (a list of words) for the file ID, 
followed by the positive or negative label in one big list.
'''
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

'''
we use random to shuffle our documents. This is because we're going to be training and testing. 
If we left them in order, chances are we'd train on all of the negatives, 
some positives, and then test only against positives. We don't want that,
so we shuffle the data.
'''
random.shuffle(documents)

'''
print out documents[1], which is a big list, where the first element is a list the words, 
and the 2nd element is the "pos" or "neg" label.
'''
print(documents[1])
#
# all_words = []
# for w in movie_reviews.words():
#     all_words.append(w.lower())
#
# all_words = nltk.FreqDist(all_words)

'''
the most popular "words" are actually things like punctuation, "the," "a" and so on, 
but quickly we get to legitimate words. We intend to store a few thousand of the most popular words, 
so this shouldn't be a problem.
'''
# print(all_words.most_common(15))
# print(all_words["stupid"])
