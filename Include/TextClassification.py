                                        # Text Classification
import nltk
import random
from nltk.corpus import movie_reviews
import pickle

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
# print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

'''
the most popular "words" are actually things like punctuation, "the," "a" and so on, 
but quickly we get to legitimate words. We intend to store a few thousand of the most popular words, 
so this shouldn't be a problem.
'''
# print(all_words.most_common(15))
# print(all_words["stupid"])

word_features = list(all_words.keys())[:3000]
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]
# print(featuresets)

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]


# we're going to use first is the Naive Bayes classifier. This is a pretty popular algorithm used in text classification,
classifier = nltk.NaiveBayesClassifier.train(training_set)
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)    #first parameter to pickle.dump() is what are you dumping, the second parameter is where are you dumping it.
save_classifier.close()


print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

'''
What this tells you is the ratio of occurences in negative to positive, or visa versa, for every word. 
So here, we can see that the term "insulting" appears 10.6 more times as often in negative reviews 
as it does in positive reviews. Ludicrous, 10.1.
'''
classifier.show_most_informative_features(15)

# classifier_f = open("naivebayes.pickle", "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()

