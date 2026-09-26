from loader import load_text_from_pdf
from Tokenizer import CharacterTokenizer

tokenizer = CharacterTokenizer()

text = load_text_from_pdf()
tokenizer.train(text)
tokenizer.save('vocab.json')

ids = tokenizer.encode('Hello My name is Md Mahfujur Rahman')
print(ids)

tokens = tokenizer.decode(ids)

print(tokens)
