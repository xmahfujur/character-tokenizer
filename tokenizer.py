class CharacterTokenizer:
    def __init__(self):

        self.token_to_id = {}
        self.id_to_token = {}


        #unknown token handle with <UNK> spacial token

        self.token_to_id['<UNK>'] = 0
        self.id_to_token[0] = '<UNK>'

        self.vocab = {}


    def train(self, text):

        tokens = set(sorted(text))

        #assign token to id

        for id , token in enumerate(tokens, start=1):
            self.token_to_id[token] = id
            self.id_to_token[id] = token

        self.vocab = self.token_to_id.copy()


    def encode(self, input):
        tokens = list(input)
        id = []
        for token in tokens:
            if token not in self.token_to_id:
                id.append('<UNK>')

            else:
                id.append(self.token_to_id[token])

        return id



    def decode(self, ids):

        return ''.join(self.id_to_token[id] for id in ids)


    def save(self, path):
        import json

        data = {
            'version' : '1.0',
            'tokenizer_type' : 'character',
            'unknown_token' : '<UNK>',
            'unk_token_id' : 0,
            'vocab_size' : len(self.vocab),
            'token_to_id' : self.token_to_id,
            'id_to_token' : self.id_to_token

        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )
