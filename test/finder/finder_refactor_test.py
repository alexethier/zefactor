from zefactor.api.finder.finder_refactor import FinderRefactor

def run(text, find_tokens):
  finder_refactor = FinderRefactor()
  return list(finder_refactor.scan_text(text, find_tokens))

def test_finder_refactor():
  find_tokens = [ "red", "lobster" ]

  matches = run(" red lobster ", find_tokens)
  assert len(matches) == 1
  assert "red lobster" in matches

  matches = run("red lobster ", find_tokens)
  assert len(matches) == 1
  assert "red lobster" in matches

  matches = run(" red lobster", find_tokens)
  assert len(matches) == 1
  assert "red lobster" in matches

  matches = run("red lobster", find_tokens)
  assert len(matches) == 1
  assert "red lobster" in matches

  matches = run(" red lobster_RED_LOBSTER red red red obster lobster lobsterr red lobster RED LOBSTER", find_tokens)
  assert len(matches) == 3
  assert "red lobster" in matches
  assert "RED_LOBSTER" in matches
  assert "RED LOBSTER" in matches

def test_finder_refactor_dup():
  find_tokens = [ "r" ]

  matches = run(" rrr rRr rr rrrrrrrrrrrr ", find_tokens)
  assert len(matches) == 0

  matches = run("r_R", find_tokens)
  assert len(matches) == 2
  assert "r" in matches
  assert "R" in matches
