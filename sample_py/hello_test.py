import unittest

from sample_py import hello

class HelloTest(unittest.TestCase):
  def test_hello(self):
    self.assertEqual(hello.hello(2), 'hellohello')
    self.assertEqual(hello.hello(1), 'hello')
    self.assertEqual(hello.hello(0), '')

  def test_world(self):
    self.assertEqual(hello.world(2), 'worldworld')
    self.assertEqual(hello.world(1), 'world')
    self.assertEqual(hello.world(0), '')
