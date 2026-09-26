# Character Tokenizer

 A small character-level tokenizer written in Python. It builds a vocabulary from the unique characters in a text corpus, converts characters to integer IDs, and converts IDs back to text.

 ## Features

 - Character-level vocabulary generation
 - Reserved `<UNK>` token with ID `0`
 - Text encoding and decoding
 - Vocabulary export as JSON
 - PDF corpus loading with PyMuPDF

 ## Project Structure

 ```text
 character-tokenizer/
 |-- Tokenizer.py       # CharacterTokenizer implementation
 |-- loader.py          # Loads text from PDF files
 |-- pipeline.py        # Training and demonstration script
 |-- vocab.json         # Example generated vocabulary
 |-- requirements.txt   # Python dependencies
 |-- datasets/          # Training text and generated data
 ```

 ## Installation

 Create and activate a virtual environment, then install the dependencies:

 ```powershell
 python -m venv .venv
 .\.venv\Scripts\Activate.ps1
 pip install -r requirements.txt
 ```

 The project uses these dependencies:

 - `python-dotenv` for environment variables
 - `PyMuPDF` for extracting text from PDF files

 ## Configure the PDF Loader

 `loader.py` reads two paths from a `.env` file in the project directory:

 ```dotenv
 DATASETS_PATH=C:\path\to\pdfs
 DESTINATION_PATH=C:\Nthropos\character-tokenizer\datasets
 ```

 All PDF files inside `DATASETS_PATH`, including nested folders, are read. Their extracted text is written to `DESTINATION_PATH/data.txt`.

 ## Run the Pipeline

 From the `character-tokenizer` directory, run:

 ```powershell
 python pipeline.py
 ```

 The pipeline:

 1. Extracts text from the configured PDF directory.
 2. Trains a `CharacterTokenizer` from the extracted text.
 3. Saves the vocabulary to `vocab.json`.
 4. Encodes and decodes a sample sentence.

 ## Use the Tokenizer Directly

 ```python
 from Tokenizer import CharacterTokenizer

 tokenizer = CharacterTokenizer()
 tokenizer.train("hello world")

 encoded = tokenizer.encode("hello")
 decoded = tokenizer.decode(encoded)

 print(encoded)
 print(decoded)

 tokenizer.save("vocab.json")
 ```

 `train()` creates one token for each distinct character in the training text. The generated numeric IDs are stored in `token_to_id`, while `id_to_token` supports decoding.

 ## Vocabulary Format

 A saved vocabulary contains:

 ```json
 {
	 "version": "1.0",
	 "tokenizer_type": "character",
	 "unknown_token": "<UNK>",
	 "unk_token_id": 0,
	 "vocab_size": 81,
	 "token_to_id": {},
	 "id_to_token": {}
 }
 ```

 The exact vocabulary size and IDs depend on the characters present in the training corpus.

 ## Important Notes

 - Train the tokenizer before calling `encode()`.
 - Character matching is case-sensitive, so `A` and `a` are different tokens.
 - Whitespace, punctuation, and newline characters are treated as tokens.
 - The current `encode()` implementation represents unseen characters as the string `<UNK>`. If decoding text containing unseen characters is required, update it to emit the numeric unknown ID `0`.
 - The current implementation saves vocabularies but does not yet provide a method to load a saved `vocab.json` back into a tokenizer instance.

 ## License

 No license has been specified for this project yet.
