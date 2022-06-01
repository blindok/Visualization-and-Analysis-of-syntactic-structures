from pathlib import Path

import stanza
from numba import jit
from nltk.tree import Tree, TreePrettyPrinter
import spacy
from spacy import displacy


language_eng = 'en'
language_rus = 'ru'


def lemmatize(sentence):
    nlp = stanza.Pipeline(lang=language_eng, processors='tokenize,mwt,pos,lemma')
    doc = nlp(sentence)
    print(*[f'word: {word.text + " "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
    return


def toConllu(sentence):
    #stanza.download('ru')  # Р·Р°РіСЂСѓР·РєР° РјРѕРґРµР»Рё
    nlp = stanza.Pipeline('en')  # Р·Р°РїСѓСЃС‚РёС‚ РїР°Р№РїР»Р°Р№РЅ

    doc = nlp(sentence)
    doc.sentences[0].print_dependencies()
    print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
    print("TYPE-> ", type(doc.sentences[0]))


def tree(sent):
    nlp = stanza.Pipeline(lang=language_eng, processors='tokenize,pos,constituency')
    doc = nlp(sent)
    s = ''
    for sentence in doc.sentences:
        print(sentence.constituency)
        s = s + str(sentence.constituency)
    tree = Tree.fromstring(s)
    tpp = TreePrettyPrinter(tree)
    print(tpp.text())


from spacy import displacy


def printf(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    print(doc)
    #displacy.serve(doc, style="dep")
    # displacy.render([doc], style="dep", page=True)
    options = {"compact": False, "color": "white"}
    svg = displacy.render(doc, style="dep", options=options)
    output_path = Path("s.svg")
    output_path.open("w", encoding="utf-8").write(svg)


sentence = input()

#Р»РµРјРјР°С‚РёР·Р°С†РёСЏ
#lemmatize(sentence)


#toConllu(sentence)
#tree(sentence)
printf(sentence)
