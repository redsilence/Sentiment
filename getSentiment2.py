import nltk
import numpy
import re
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--train", help="train")
parser.add_argument("--tweet", help="tweet")
args = parser.parse_args()


def find_ones(a):
    b=np.asarray(a)
    c=np.where(b==1)
    return(len(c[0]))


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


f = file_len(args.train)/2

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

tweets = []
for i,line in enumerate(open(args.train)):
    if i<f:
    	words=re.split(' ',line)
    	#print(words[0:len(words)-1])
    	sent=words[-1].rstrip(' \n')
    	#print(sent)
    	wds = words[0:len(words)-1]
    	#from IPython import embed
    	#embed()
    	f= [e.lower() for e in wds if len(e) >= 3]
    	#print(f)
    	#print('Done')
    	tweets.append((f, sent))

word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
n_pos=[]
for line in open(args.tweet):
    #print('Line is: ',line)
    out = classifier.classify(extract_features(line.split()))
    #print(out)
    if out == "positive":
        n_pos.append(1)
    else:
        n_pos.append(-1)

ff = file_len(args.tweet)
#print("Positives = ",n_pos)
print("total nos= ",ff)
print(find_ones(n_pos))




# starting second round


#del(training_set)
#del(classifier)
#del(word_features)
f = file_len(args.train)/2

#print(f)

tweets = []
for i,line in enumerate(open(args.train)):
    #print(i,f)
    if i>f:
    	words=re.split(' ',line)
    	#print(i,f,words[0:len(words)-1])
    	sent=words[-1].rstrip(' \n')
    	#print(sent)
    	wds = words[0:len(words)-1]
    	#from IPython import embed
    	#embed()
    	ff= [e.lower() for e in wds if len(e) >= 3]
    	#print(f)
    	#print('Done')
    	tweets.append((ff, sent))

word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
n_pos=[]
for line in open(args.tweet):
    #print('Line is: ',line)
    out = classifier.classify(extract_features(line.split()))
    #print(out)
    if out == "positive":
        n_pos.append(1)
    else:
        n_pos.append(-1)

ff = file_len(args.tweet)
#print("Positives = ",n_pos)
print("total nos= ",ff)
print(find_ones(n_pos))


# starting third round

f = file_len(args.train)/2

#print(f)

tweets = []
for i,line in enumerate(open(args.train)):
    #print(i,f)
    words=re.split(' ',line)
    #print(i,f,words[0:len(words)-1])
    sent=words[-1].rstrip(' \n')
    #print(sent)
    wds = words[0:len(words)-1]
    #from IPython import embed
    #embed()
    ff= [e.lower() for e in wds if len(e) >= 3]
    #print(f)
    #print('Done')
    tweets.append((ff, sent))

word_features = get_word_features(get_words_in_tweets(tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
n_pos=[]
for line in open(args.tweet):
    #print('Line is: ',line)
    out = classifier.classify(extract_features(line.split()))
    #print(out)
    if out == "positive":
        n_pos.append(1)
    else:
        n_pos.append(-1)

ff = file_len(args.tweet)
#print("Positives = ",n_pos)
print("total nos= ",ff)
print(find_ones(n_pos))

