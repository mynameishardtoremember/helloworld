import pytest

from helloworld import helloworld

def test_print_me():
	assert(helloworld.return_me('hi') == 'hi')
