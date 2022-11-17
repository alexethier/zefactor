from zefactor.api.replacer.replacer_manager import ReplacerManager
from zefactor.api.transform.transform_manager import TransformManager
from zefactor.api.finder.finder_scan_manager import FinderScanManager

def test_replacer_manager_edges():

  replacement_map = { "red lobster":"ruby tuesday" }

  replacement_texts = { "red lobster" : "ruby tuesday", "red lobster RED LOBSTE": "ruby tuesday RED LOBSTE", " red lobster " : " ruby tuesday ", "%red lobster-" :"%ruby tuesday-" }
  for replacement_input in replacement_texts:
    replacer_manager = ReplacerManager()
    replacement_output = replacer_manager.apply_text(replacement_input, replacement_map)
    assert replacement_output == replacement_texts[replacement_input]

def test_replacer_manager():

  find_tokens = [ "red", "lobster" ]
  replace_tokens = [ "ruby", "tuesday" ]

  transform_manager = TransformManager()

  replacement_texts = { "red_lobster RED%LOBSTER redlobster redlobsterr RED_LOB" : "ruby_tuesday RUBY%TUESDAY rubytuesday redlobsterr RED_LOB" }
  for replacement_input in replacement_texts:

    finder_scan_manager = FinderScanManager(find_tokens)
    for char in replacement_input:
      finder_scan_manager.check_next(char)
    find_matches = finder_scan_manager.matches()

    replacement_map = transform_manager.compute_replacement_map(find_matches, find_tokens, replace_tokens)
    replacer_manager = ReplacerManager()
    replacement_output = replacer_manager.apply_text(replacement_input, replacement_map)
    assert replacement_output == replacement_texts[replacement_input]

def test_replacer_manager_lines():

  find_tokens = [ "red", "lobster" ]
  replace_tokens = [ "ruby", "tuesday" ]

  transform_manager = TransformManager()

  replacement_texts = { "red\nlobster" : "red\nlobster" }
  for replacement_input in replacement_texts:

    finder_scan_manager = FinderScanManager(find_tokens)
    for char in replacement_input:
      finder_scan_manager.check_next(char)
    find_matches = finder_scan_manager.matches()

    replacement_map = transform_manager.compute_replacement_map(find_matches, find_tokens, replace_tokens)
    replacer_manager = ReplacerManager()
    replacement_output = replacer_manager.apply_text(replacement_input, replacement_map)
    assert replacement_output == replacement_texts[replacement_input]
