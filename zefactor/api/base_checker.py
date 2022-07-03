from zefactor.api.match_reason import MatchReason

class BaseChecker:

  # Given a list of tokens like [ happy, turtle ]
  # It will check against a stream of characters to see if they match
  # This assumes there will be a placeholder between the tokens
  def __init__(self, check_strings, case_sensitive):
    self._check_strings = []
    self._check_strings.extend(check_strings)
    self._check_string = self._check_strings.pop(0)
    self._case_sensitive = case_sensitive

    self._index = 0
    self._char_count = -1

    # In order to fully match, the token must terminate with a non-alphanumeric char. This is so 'rock' won't match tokens like 'rocket'.
    self._last_char = None
    self._first_char = None
    self._matched = False
    self._done = False

  def check_next(self, next_char):
    self._char_count += 1

    # A match must start with a non-alphanumeric character or a different case
    if(self._first_char == None):
      self._first_char = next_char
      return MatchReason.VALID_START

    if(self._char_count == 1):
      if(self._first_char.isalnum()):
        if((self._first_char.isupper() and next_char.isupper()) or (self._first_char.islower() and next_char.islower())):
          return MatchReason.INVALID_START

    next_char_cased = next_char
    if(not self._case_sensitive):
      next_char_cased = next_char.lower()

    # If we are done matching, the next character must terminate the sequence by being non-alphanumeric or a different case
    if(self._matched):
      if(not next_char_cased.isalnum()):
        self._done = True
        return MatchReason.VALID_DONE
      else:
        if((self._last_char.isupper() and next_char.isupper()) or (self._last_char.islower() and next_char.islower())):
          return MatchReason.INVALID_END
        else:
          self._done = True
          return MatchReason.VALID_DONE
    self._last_char = next_char

    # When checking the next character between tokens, any non-alphanumeric is allowed 
    # or the first character in the next token must be present
    if(self._index == -1):
      if(not next_char_cased.isalnum()):
        self._index = 0
        return MatchReason.VALID_BETWEEN_TOKENS
      elif(next_char_cased == self._check_string[0]):
        self._index = 1
        return MatchReason.VALID_BETWEEN_TOKENS
      else:
        return MatchReason.INVALID_BETWEEN_TOKENS

    if(self._check_string[self._index] == next_char_cased):

      # Check next index
      self._index = self._index + 1
      if(self._index == len(self._check_string)):
        if(len(self._check_strings) > 0):
          self._check_string = self._check_strings.pop(0)
          self._index = -1
        else:
          self._matched = True

      return MatchReason.VALID_WITHIN_TOKEN
    else:
      return MatchReason.INVALID_WITHIN_TOKEN

  def is_done(self):
    return self._done
