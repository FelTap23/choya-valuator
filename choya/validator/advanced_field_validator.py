from abc import ABC, abstractmethod
from typing import Any

#TODO add more details to this validator
class AdvancedFieldValidator(ABC):
    @abstractmethod
    def validate(field_name: str, value : Any) -> bool:
        pass