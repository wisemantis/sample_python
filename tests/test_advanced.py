# -*- coding: utf-8 -*-

from .context import sample
from .context import mymath

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

    def test_mymath_add(self):
        self.assertTrue( mymath.add(1,2)==3 )

    def test_mymath_multiply(self):
        self.assertTrue( mymath.multiply(1,2)==2 )

    def test_mymath_sin(self):
        self.assertTrue( mymath.trig.sin(0)==0 )


if __name__ == '__main__':
    unittest.main()
