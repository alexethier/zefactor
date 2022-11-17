from zefactor.api.finder.finder_scan_manager import FinderScanManager

def check_text(find_tokens, text):
  finder_scan_manager = FinderScanManager(find_tokens)

  if len(text) < 1:
    find_scan_manager.check_next(text)

  for char in text:
    finder_scan_manager.check_next(char)

  return finder_scan_manager.matches()

def test_find_scan_manager():
  find_tokens = [ "red", "lobster" ]

  matches = check_text(find_tokens, "red lobster")
  assert len(matches) == 1
  assert matches[0] == "red lobster"

  matches = check_text(find_tokens, "red lobster red lobster")
  assert len(matches) == 1
  assert matches[0] == "red lobster"

  matches = check_text(find_tokens, "red lobsterred lobster")
  assert len(matches) == 0

  matches = check_text(find_tokens, "red lobster_rEd lobster")
  assert len(matches) == 2
  assert "red lobster" in matches
  assert "rEd lobster" in matches

  matches = check_text(find_tokens, "ared lobster red lobsterr red lobste ed lobster red red red obster lobster lobster RED LOBSTER anotherRedLobster")
  assert len(matches) == 1
  assert "RED LOBSTER" in matches

def test_find_scan_manager_repeat():
  find_tokens = [ "r" ]

  matches = check_text(find_tokens, "rR")
  assert len(matches) == 0

  matches = check_text(find_tokens, "r R")
  assert len(matches) == 2
  assert "r" in matches
  assert "R" in matches

def test_find_scan_manager_multi():
  find_tokens = [ "r", "r" ]

  nonalpha = "!@#$%^&*()_+-="
  check_text_input = "r" + "r".join(nonalpha) + "r R"  + "R".join(nonalpha) + "R"

  matches = check_text(find_tokens, check_text_input)
  print(matches)
  for char in nonalpha:
    assert f"r{char}r" in matches
    assert f"R{char}R" in matches
