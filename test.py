
from googletrans import Translator

translator = Translator()
textBetween = "포뮬러 50ml, 트리트먼트 30ml"
textBetween = translator.translate(textBetween)
print(textBetween.text)