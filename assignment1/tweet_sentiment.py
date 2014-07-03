import sys
import json

def make_dici(file,dici):
    for line in file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        dici[term] = int(score)  # Convert the score to an integer.		

def get_sent(msg,dici):
    sent = 0
    for term in dici:
        if msg.find(term) >= 0:
            sent += dici[term]

    return sent

def main():
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    make_dici(sent_file,scores)
    tweet_file = open(sys.argv[2])
    parsed = {}
    for mgot in tweet_file:
        sent = 0
        parsed.clear()
        parsed = json.loads(mgot)
        if parsed.has_key('text'):
            if parsed.has_key('lang'):
                if parsed.get('lang') == 'en':
                    sent += get_sent(parsed.get('text').encode('utf-8'),scores)
                    print sent
			
if __name__ == '__main__':
    main()
