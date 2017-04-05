#!/usr/bin/env python

import csv, argparse, collections

parser = argparse.ArgumentParser()
parser.add_argument('--foods_file', default='foods.txt')
parser.add_argument('--tweet_files', nargs='+', default=['tweet_pgh.csv', 'tweet_ny.csv', 'tweet_austin.csv', 'tweet_sf.csv'])
args = parser.parse_args()

foods = [f[0] for f in csv.reader(open(args.foods_file))]

all_counters = {}
for filename in args.tweet_files:
    print "starting " + filename
    this_file_foods = collections.Counter()
    for line in csv.reader(open(filename)):
        words = line[5].lower().split()
        for word in words:
            if word in foods:
                this_file_foods[word] += 1
    all_counters[filename] = this_file_foods
    print "done with " + filename

total_counter = collections.Counter()
for counter in all_counters.values():
    total_counter += counter

for filename, counter in all_counters.iteritems():
    tfidfs = collections.Counter()
    for word, count in counter.iteritems():
        tf = count
        idf = 1.0 / total_counter[word]
        tfidfs[word] = tf * idf
    print filename
    print tfidfs.most_common(10)
        
        
