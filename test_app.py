from app import t_function
from unittest import TestCase


class Test(TestCase):
    def test_t_function(self):
        assert t_function() == "ello"
