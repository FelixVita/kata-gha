import pytest

from debbiedowner import make_it_negative, complain_about

def test_negativity():
    assert make_it_negative(8) == -8
    assert complain_about('enthusiasm') == "I hate enthusiasm. Totally boring."

def test_easy():
    assert 1 == 1
