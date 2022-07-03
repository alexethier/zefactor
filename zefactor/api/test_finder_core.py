from .finder_core import FinderRefactor

def get_line1():
  return "blue fish AnBlueFishO ABlueFish BlueFishy AblueFISHt"

def get_line2():
  return "red dog Red:Dog bluefish AnotherBlueFish three_turtles redred dog"

def test_scan_text1():
  
  finder = FinderRefactor()

  items = list(finder.scan_text(get_line1(), ["blue", "fish"]))
  assert len(items) == 3
  assert items[0] == 'blue fish'
  assert items[1] == 'BlueFish'
  assert items[2] == 'blueFISH'

def test_scan_text2():

  finder = FinderRefactor()

  items = list(finder.scan_text(get_line2(), ["red", "dog"]))
  assert len(items) == 2
  assert items[0] == 'red dog'
  assert items[1] == 'Red:Dog'
