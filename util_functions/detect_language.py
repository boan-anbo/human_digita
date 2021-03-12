from langdetect import detect

from human_digita.common.const import LanguageTypes


def detect_language(text: str) -> LanguageTypes.choices:
    try:
        result = detect(text)
        if result == 'en':
            return LanguageTypes.ENGLISH
        if result == 'zh-cn' or result == 'zh-tw':
            return LanguageTypes.CHINESE
        return LanguageTypes.OTHER
    except Exception as e:
        print(e)
        return LanguageTypes.UNKNOWN
