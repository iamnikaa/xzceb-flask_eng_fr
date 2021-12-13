"""Module for translation functions"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

language_translator.set_service_url(URL)

def frenchToEnglish(inpstr):
    """Function to translate french text to english"""
    translation = language_translator.translate(
        text=inpstr,
        model_id='fr-en').get_result()
    result = translation['translations'][0]['translation']  # pylint: disable=E1136
    return result

def englishToFrench(inpstr):
    """Function to translate english text to french"""
    translation = language_translator.translate(
        text=inpstr,
        model_id='en-fr').get_result()
    result = translation['translations'][0]['translation']  # pylint: disable=E1136
    return result
