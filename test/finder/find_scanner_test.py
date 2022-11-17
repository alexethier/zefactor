from zefactor.api.finder.find_scanner import FindScanner
from zefactor.api.finder.match_result import MatchResult

def check_text(find_scanner, text):
  if len(text) < 1:
    return find_scanner.check_next(text)

  match_result = None
  for char in text:
    match_result = find_scanner.check_next(char)
    if match_result != MatchResult.CONTINUE:
      break
  return match_result
        

def test_find_scanner_match():
  find_tokens = [ "red", "lobster" ]

  matches = { " red lobster ": "red lobster", " redlobster ": "redlobster", " redLobster ": "redLobster", " RedLobster ": "RedLobster", " red_lobster ": "red_lobster", "_REDLOBSTEr%": "REDLOBSTEr" }
  for match in matches:
    expected_output = matches[match]

    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, match)
    assert match_result == MatchResult.MATCH
    
    text = find_scanner.input()
    assert text == expected_output


def test_find_scanner_small_match():
  find_tokens = [ "r" ]

  matches = { " r ": "r" }
  for match in matches:
    expected_output = matches[match]

    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, match)
    assert match_result == MatchResult.MATCH

    text = find_scanner.input()
    assert text == expected_output

  no_matches = [ " rr ", "  ", "   ", "           " ]
  for no_match in no_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, no_match)
    assert match_result == MatchResult.NO_MATCH

  continue_matches = [ " ", "" ]
  for continue_match in continue_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, continue_match)
    assert match_result == MatchResult.CONTINUE


def test_find_scanner_match_multi1():
  find_tokens = [ "r", "r", "r" ]

  matches = { " rrr ": "rrr", " r r%r ": "r r%r", " rr r ": "rr r" }
  for match in matches:
    expected_output = matches[match]

    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, match)
    assert match_result == MatchResult.MATCH

    text = find_scanner.input()
    assert text == expected_output

  no_matches = [ " rrrr " ]
  for no_match in no_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, no_match)
    assert match_result == MatchResult.NO_MATCH

  continue_matches = [ " rr ", " r r" ]
  for continue_match in continue_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, continue_match)
    assert match_result == MatchResult.CONTINUE

def test_find_scanner_match_multi2():
  find_tokens = [ "r", "rr" ]

  matches = { " rrr ": "rrr", " r rr ": "r rr" }
  for match in matches:
    expected_output = matches[match]

    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, match)
    assert match_result == MatchResult.MATCH

    text = find_scanner.input()
    assert text == expected_output

  no_matches = [ " rrrr ", " rr_r " ]
  for no_match in no_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, no_match)
    assert match_result == MatchResult.NO_MATCH

def test_find_scanner_no_match():
  find_tokens = [ "red", "lobster" ]

  no_matches = [ " blue fish ", " redlobste ", "redlobster ", " red lobersterr " ]
  for no_match in no_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, no_match)
    assert match_result == MatchResult.NO_MATCH

def test_find_scanner_continue():
  find_tokens = [ "red", "lobster" ]

  continue_matches = [ " red ", " redl", "_redlobster" ]
  for continue_match in continue_matches:
    find_scanner = FindScanner(find_tokens)
    match_result = check_text(find_scanner, continue_match)
    assert match_result == MatchResult.CONTINUE
