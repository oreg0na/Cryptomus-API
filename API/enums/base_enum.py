from enum import Enum

class _BaseCryptomusEnum(Enum):
  def __str__(self) -> str:
    return self.value
  
  @classmethod
  def ro_list(cls):
    return list(cls)