import pytest

from helloworld import helloworld

def test_print_me():
	assert(helloworld.return_me('hi') == 'hi')

def test_plus_me():
	assert(helloworld.plus_me(99) == 100)

def test_minus_me():
	assert(helloworld.minus_me(1) == 0)
