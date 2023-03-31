import unittest

from sample_py import hello

class HelloTest(unittest.TestCase):
  def test_hello(self):
    self.assertEquals(hello.hello(2), 'hellohello')
    self.assertEquals(hello.hello(1), 'hello')
    self.assertEquals(hello.hello(0), '')
