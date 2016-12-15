"""
103 
"""

from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

grammar = CFG.fromstring("""
	S -> X | '{' Z '}'
	Z -> X ',' Z | X
	X -> Y | X 'U' X 
	Y -> '{}' | 'N' | 'R'
	""")

for sentence in generate(grammar, depth=6, n=200):
	print(' '.join(sentence))