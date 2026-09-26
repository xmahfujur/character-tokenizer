from dotenv import load_dotenv
import os
import pymupdf
import pathlib
load_dotenv()

def load_text_from_pdf():

    datasets_path = os.getenv('DATASETS_PATH')
    destination_path = os.getenv('DESTINATION_PATH')

    datasets_path = pathlib.Path(datasets_path)
    destination_path = pathlib.Path(destination_path)


    datasets_paths = datasets_path.rglob('*.pdf')
    with open(destination_path / 'data.txt', 'w', encoding='utf-8') as f:
    
        for pdf_path in datasets_paths:
            print('Reading ', pdf_path)
            pdf = pymupdf.open(pdf_path)

            for page in pdf:
                text = page.get_text()
                f.write(text)
                f.write('\n\n')

    with open(destination_path / 'data.txt', 'r', encoding='utf-8') as f:
        data =  f.read()

 


    return data