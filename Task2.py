import nltk
import stanza
sentences = nltk.corpus.brown.sents()
sentences_list = list(sentences)
def get_pos_from_stanza_output(output) :
    r = []
    for s in output.sentences : 
        pos = []
        for w in s.words : 
            pos.append(convert_pos(w.upos)) 
        r.append(pos)
    return r
def convert_pos(pos) :
    if pos=="CCONJ" :
        return "CONJ"
    elif pos=="AUX" :
        return "VERB"
    elif pos=="INTJ" :
        return "X"
    elif pos=="PART" :
        return "PRT"
    elif pos=="PROPN" :
        return "NOUN"
    elif pos=="PUNCT" :
        return "."
    elif pos=="SCONJ" :
        return "ADP"
    elif pos=="SYM" :
        return "X"
    else :
        return pos
    pos_tagger=stanza.Pipeline(processors="tokenize,pos", tokenize_pretokenized=True)
    
def accuracy(gold,output) :
    correct = 0
    total = 0
    assert(len(gold)==len(output))
    for i in range(len(gold)) : # loop through every sentence
        assert(len(gold[i])==len(output[i]))
        total += len(gold[i])
        for j in range(len(gold[i])) :# loop through every token
            if gold[i][j]==output[i][j] : # match
                correct += 1
    return((correct*100)/total)
    
pos_tagger=stanza.Pipeline(processors="tokenize,pos", tokenize_pretokenized=True)
output = pos_tagger([["He", "came", "second", "in", "the", "race", "as", "he", "lost", "by", "a", "second", "."],["The", "committe", "chair", "sat", "on", "the", "office", "chair", "."], ["The", "lawyer", "had", "to", "object", "as", "the", "object", "of", "the", "evidence", "was", "weak", "."], ["A", "minute", "amount", "of", "sand", "falls", "in", "the", "hour", "glass", "every", "minute", "."],["I", "left", "my", "phone", "over", "the", "left", "window", "of", "the", "house", "."]])
pos = get_pos_from_stanza_output(output)
pos
correct_pos = [['PRON',
  'VERB',
  'ADJ',
  'ADP',
  'DET',
  'NOUN',
  'ADP',
  'PRON',
  'VERB',
  'ADP',
  'DET',
  'NOUN',
  '.'], ['DET', 'NOUN', 'NOUN', 'VERB', 'ADP', 'DET', 'NOUN', 'NOUN', '.'], ['DET',
  'NOUN',
  'VERB',
  'PRT',
  'VERB',
  'ADP',
  'DET',
  'NOUN',
  'ADP',
  'DET',
  'NOUN',
  'VERB',
  'ADJ',
  '.'], ['DET',
  'ADJ',
  'NOUN',
  'ADP',
  'NOUN',
  'VERB',
  'ADP',
  'DET',
  'NOUN',
  'NOUN',
  'ADJ',
  'NOUN',
  '.'], ['PRON',
  'VERB',
  'PRON',
  'NOUN',
  'ADP',
  'DET',
  'ADJ',
  'NOUN',
  'ADP',
  'DET',
  'NOUN',
  '.']]
acc = accuracy(correct_pos,pos)
print("Final Accuracy is", acc, end='%')
    
