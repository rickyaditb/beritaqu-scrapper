def load_lexicon(file):
    lexicon = {}
    with open(file, 'r') as f:
        for line in f:
            word, weight = line.strip().split('\t')
            try:
                lexicon[word] = float(weight)
            except ValueError:
                continue
    return lexicon

# Analyze sentiment
def checkSentiment(text):
    positive_lexicon = load_lexicon('./sentiment/positive.tsv')
    negative_lexicon = load_lexicon('./sentiment/negative.tsv')
    words = text.lower().split()
    sentiment_score = 0
    for word in words:
        if word in positive_lexicon:
            sentiment_score += positive_lexicon[word]
        elif word in negative_lexicon:
            sentiment_score += negative_lexicon[word]
    return sentiment_score