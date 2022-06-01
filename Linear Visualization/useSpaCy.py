from pathlib import Path
from spacy.tokens.doc import Doc
from spacy_conll import init_parser
import spacy
import spacy_conll
from spacy_conll import init_parser
from spacy_conll.parser import ConllParser
from spacy import displacy
from spacy_conll import init_parser
from spacy_conll.parser import ConllParser

# ввод предложения
# sentence = input()


# # to conll-u format
# nlp = spacy.load("ru_core_news_sm")
# nlp.add_pipe("conll_formatter")
# doc = nlp(sentence)
# conll = doc._.conll_str
# file = open('dataframe.conllu', 'w')
# file.write(conll)
# file.close()


# # Dependency visualization
# token = TokenList[0]
# s = ''
# for i in TokenList[0]:
#     s = s + i["form"] + ' '
# print(s)
#nlp = spacy.load("en_core_web_sm")

nlp = ConllParser(init_parser(parser="spacy", model_or_lang="ru_core_news_sm"))
doc = nlp.parse_conll_file_as_spacy(input_file="test.conllu.txt", input_encoding="utf-8")
for sent in doc.sents:
    for token in sent:
        print(token.text, token.dep_, token.pos_)
options = {"compact": True, "color": "black", "bg": "white", "distance": 110, "word_spacing": 60}
svg = displacy.render(doc, style="dep", options=options)
output_path = Path("sentence3.svg")
output_path.open("w", encoding="utf-8").write(svg)
