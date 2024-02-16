import requests
from urllib.parse import quote

def translate_text(text, source_lang, target_lang):
    encoded_text = quote(text)
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}'.format(
        source_lang, target_lang, encoded_text)
    response = requests.get(url)
    translations = []
    if response.ok:
        data = response.json()
        for item in data[0]:
            if item[0]:
                translation = item[0]
                if target_lang == 'ur':
                    translation = translation.replace(", ", "-")
                else:
                    translation = translation.replace(", ", ".")
                if '.' in text:
                    translation = translation.split('. ')[1] if translation.startswith('. ') else translation
                translations.append(translation)
    return translations

def main():
    source_lang = input("Enter the source language (e.g., en for English): ")
    target_lang = input("Enter the target language (e.g., ur for Urdu): ")
    text = input("Enter the text to translate: ")
    translated_texts = translate_text(text, source_lang, target_lang)
    print("Translated texts:", " ".join(translated_texts))

if __name__ == "__main__":
    main()
