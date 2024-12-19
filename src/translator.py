from transformers import MarianMTModel, MarianTokenizer

import torch

from functools import lru_cache


class Translator:

    def __init__(self):

        self.LANGUAGE_MODELS = {

            "Arabic": "Helsinki-NLP/opus-mt-en-ar",

            "Chinese": "Helsinki-NLP/opus-mt-en-zh",

            "French": "Helsinki-NLP/opus-mt-en-fr",

            "German": "Helsinki-NLP/opus-mt-en-de",

            "Hindi": "Helsinki-NLP/opus-mt-en-hi",

            "Italian": "Helsinki-NLP/opus-mt-en-it",

            "Japanese": "Helsinki-NLP/opus-mt-en-jap",

            "Portuguese": "Helsinki-NLP/opus-mt-en-pt",

            "Russian": "Helsinki-NLP/opus-mt-en-ru",

            "Spanish": "Helsinki-NLP/opus-mt-en-es"

        }

    

    @lru_cache(maxsize=2)  # Cache the last 2 models

    def load_model(self, model_name):

        """Load the translation model and tokenizer."""

        model = MarianMTModel.from_pretrained(model_name)

        tokenizer = MarianTokenizer.from_pretrained(model_name)

        return model, tokenizer

    

    def translate_text(self, text_chunks, model, tokenizer):

        """Translate text chunks using the loaded model."""

        translated_chunks = []

        

        for chunk in text_chunks:

            # Tokenize and translate

            inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=512)

            

            # Generate translation

            translated = model.generate(**inputs)

            

            # Decode the translation

            translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

            translated_chunks.append(translated_text)

        

        return translated_chunks