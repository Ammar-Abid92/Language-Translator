from typing import List

from googletrans import Translator, constants
translator = Translator()
# translate any language text to english text (by default)
# Maryam ke Rauf and Faik 😂😂
sentences = ["Теперь прошу, ты, пожалуйста, молчи",
"Смотри в глаза и ничего не говори",
"Я все решил, наша речь не о любви"]
translations = translator.translate(sentences, dest="ur")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")