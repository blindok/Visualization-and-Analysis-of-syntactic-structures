import nltk
from nltk import RegexpParser
sentence = input()
tokens = nltk.word_tokenize(sentence)  #или можно использовать функцию split()
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
# entities = nltk.chunk.ne_chunk(tagged)
# print(entities)
# entities.draw()
chunker = RegexpParser("""
                    NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases
                    P: {<IN>}            #To extract Prepositions
                    V: {<V.*>}           #To extract Verbs
                    PP: {<p> <NP>}       #To extract Prepositional Phrases
                    VP: {<V> <NP|PP>*}   #To extract Verb Phrases
                    """)
output = chunker.parse(tagged)
print(output)
output.draw()