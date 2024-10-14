from googletrans import Translator

def translate_text(text, dest_language):
    # Create a Translator object
    translator = Translator()

    # Translate the text
    translation = translator.translate(text, dest=dest_language)

    # Return the translated text
    return translation.text

if __name__ == "__main__":
    # Input text and destination language
    text_to_translate = input("Enter the text to translate: ")
    dest_language = input("Enter the destination language code (e.g., 'en' for English, 'fr' for French): ")

    # Translate the text
    translated_text = translate_text(text_to_translate, dest_language)

    # Output the result
    print(f"Translated text: {translated_text}")
