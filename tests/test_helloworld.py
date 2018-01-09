import pytest

from helloworld.helloworld import return_me

def test_print_me():
	assert(return_me('hi') == 'hi')
