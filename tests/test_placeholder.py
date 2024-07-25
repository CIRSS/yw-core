from yw_generator.yw_generator import yw_generator


def test_place_holder():
    assert yw_generator("test") == "test"
