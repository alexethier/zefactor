from enum import Enum
class MatchReason(Enum):
  VALID_START = -3
  VALID_BETWEEN_TOKENS = -2
  VALID_WITHIN_TOKEN = -1
  VALID_DONE = 0
  INVALID_START = 1
  INVALID_END = 2
  INVALID_BETWEEN_TOKENS = 3
  INVALID_WITHIN_TOKEN = 4
