from unittest import TestCase
from scripts import util

class TestUtils(TestCase):
  def test_labeler(self):
    self.assertEqual(1, util.labeler('M'))
    self.assertEqual(0, util.labeler('B'))
    self.assertEqual(None, util.labeler('A'))
