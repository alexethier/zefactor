from zefactor.api.transform.transform_manager import TransformManager

def test_transform_manager_map():

  test_inputs = { "red lobster" : "ruby tuesday", "Red Lobster" : "Ruby Tuesday", "RED_LOBSTER": "RUBY_TUESDAY", "RedLOBSTER": "RubyTUESDAY" }

  transform_manager = TransformManager()
  replacement_map = transform_manager.compute_replacement_map(test_inputs.keys(), [ "red", "lobster" ], [ "ruby", "tuesday" ])

  for test_input in test_inputs:
    assert test_input in replacement_map
    assert replacement_map[test_input] == test_inputs[test_input]

