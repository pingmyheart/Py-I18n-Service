from typing import Optional

from dto.service_response import ServiceResponse


class RetrieveTranslationResponse(ServiceResponse):
    translation: Optional[str] | None = None
