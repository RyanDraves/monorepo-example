import unittest

from sample_py import hello

class HelloTest(unittest.TestCase):
  def test_hello(self):
    self.assertEqual(hello.hello(2), 'hellohello')
    self.assertEqual(hello.hello(1), 'hello')
    self.assertEqual(hello.hello(0), '')
