import javaproperties

from configuration import EnvironmentConfiguration
from configuration.logging_configuration import logger as log
from dto.service_dto import RetrieveTranslationResponse
from enumeration.response_code_enum import ResponseCodeEnum


class TranslationService:
    def __init__(self, env: EnvironmentConfiguration):
        self.env = env

    def translate(self, key: str,
                  language: str) -> RetrieveTranslationResponse:
        """
        Retrieves the translation for a given key and language.

        :param key: Translation key to look up.
        :param language: Translation language code (e.g., 'en', 'fr').
        :return: RetrieveTranslationResponse containing the translation.
        """
        log.info(f"Attempting to retrieve translation for key: {key}, language: {language}")
        try:
            translation_folder = self.env.get("TRANSLATION_FOLDER")
            with open(f'{translation_folder}/translation-{language}.properties', 'r', encoding="iso-8859-1") as file:
                properties = javaproperties.load(file)
                translation = properties.get(key, None)
                if not translation:
                    log.warning(f"Translation not found for key: {key}, language: {language}")
                    return RetrieveTranslationResponse(response_code=ResponseCodeEnum.TRANSLATION_NOT_FOUND.code,
                                                       response_message=ResponseCodeEnum.TRANSLATION_NOT_FOUND.message)
                log.info(f"Translation found for key: {key}, language: {language}")
                return RetrieveTranslationResponse(response_code=ResponseCodeEnum.SUCCESS.code,
                                                   response_message=ResponseCodeEnum.SUCCESS.message,
                                                   translation=translation)
        except FileNotFoundError:
            log.error(f"Translation file not found for language: {language}")
            return RetrieveTranslationResponse(response_code=ResponseCodeEnum.TRANSLATION_FILE_NOT_FOUND.code,
                                               response_message=ResponseCodeEnum.TRANSLATION_FILE_NOT_FOUND.message)
