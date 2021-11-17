#if the file dosen't run, please comment all the matplotlib commands or give pip install matplotlib
import nltk
import stanza
import matplotlib.pyplot as plt
sentences = nltk.corpus.brown.sents()
sentences_list = list(sentences)
List_Genre = ["learned", "government", "reviews"]
def get_pos_from_stanza_output(output) :
    r = []
    for s in output.sentences : 
        pos = []
        for w in s.words : 
            pos.append(convert_pos(w.upos)) 
        r.append(pos)
    return r
def get_pos_from_nltk_tagged_sents(o) :
    r = []
    for s in o : 
        pos = []
        for w in s : 
            pos.append(w[1]) 
        r.append(pos)
    return r
def accuracy(gold,output) :
    correct = 0
    total = 0
    assert(len(gold)==len(output))
    for i in range(len(gold)) : 
        assert(len(gold[i])==len(output[i]))
        total += len(gold[i])
        for j in range(len(gold[i])) :
            if gold[i][j]==output[i][j] : 
                correct += 1
    return((correct*100)/total)
    
def convert_pos(Stanza_Tagset_Final) :
    if Stanza_Tagset_Final=="CCONJ" :
        return "CONJ"
    elif Stanza_Tagset_Final=="AUX" :
        return "VERB"
    elif Stanza_Tagset_Final=="INTJ" :
        return "X"
    elif Stanza_Tagset_Final=="PART" :
        return "PRT"
    elif Stanza_Tagset_Final=="PROPN" :
        return "NOUN"
    elif Stanza_Tagset_Final=="PUNCT" :
        return "."
    elif Stanza_Tagset_Final=="SCONJ" :
        return "ADP"
    elif Stanza_Tagset_Final=="SYM" :
        return "X"
    else :
        return Stanza_Tagset_Final

for i in List_Genre:
    sentences = nltk.corpus.brown.sents(categories=i)
    len(sentences)
    sent_pos = nltk.corpus.brown.tagged_sents(categories=i, tagset="universal")
    len(sent_pos)
    pos_tagger=stanza.Pipeline(processors="tokenize,pos", tokenize_pretokenized=True)
    output = pos_tagger(list(sentences))
    Stanza_Tagset_Final = get_pos_from_stanza_output(output)
    NLTK_Tagset_Final = get_pos_from_nltk_tagged_sents(sent_pos)
    x = accuracy(NLTK_Tagset_Final, Stanza_Tagset_Final)
    print("'",i, "'", "accuracy:", x, end='%')
names = ['learned', 'government', 'reviews']
values = [94.35091924700914, 94.43501575937361, 93.51415094339623]

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.show()


