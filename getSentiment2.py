import nltk
import numpy
import re

tweets = []
for line in open('training_data.txt'):
    words=re.split(' ',line)
    print(words[0:len(words)-1])
    sent=words[-1].rstrip(' \n')
    print(sent)
    wds = words[0:len(words)-1]
    #from IPython import embed
    #embed()
    f= [e.lower() for e in wds if len(e) >= 3]
    print(f)
    print('Done')
    tweets.append((f, sent))

pos_tweets = [('I love this car', 'positive'),
              ('I like this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('he is a bad person', 'negative'),
              ('He is my enemy', 'negative')]

#tweets = []
#for (words, sentiment) in pos_tweets + neg_tweets:
#    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
#    tweets.append((words_filtered, sentiment))

#test_tweets = [
#    (['feel', 'happy', 'this', 'morning'], 'positive'),
#    (['larry', 'friend'], 'positive'),
#    (['not', 'like', 'that', 'man'], 'negative'),
#    (['house', 'not', 'great'], 'negative'),
#    (['your', 'song', 'annoying'], 'negative')]

#word_features = get_word_features(get_words_in_tweets(tweets))
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

word_features = get_word_features(get_words_in_tweets(tweets))

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

'''
def train(labeled_featuresets, estimator=ELEProbDist):
    # Create the P(label) distribution
    label_freqdist = extract_features(document)
    label_probdist = estimator(label_freqdist)
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    return NaiveBayesClassifier(label_probdist, feature_probdist)

#print label_probdist.prob('positive')
#print label_probdist.prob('negative')
#
#print feature_probdist
#
#print feature_probdist[('negative', 'contains(best)')].prob(True)
'''

#tweet = 'i like this car'
#tweet = 'he is my enemy'
tweet = 'he good'
tweet = 'Got Donald Trump toilet paper so I can finally wipe my ass with Donald Trump'
print classifier.classify(extract_features(tweet.split()))


for line in open('Raw_Tweets.txt'):
    print('Line is: ',line)
    print classifier.classify(extract_features(line.split()))

