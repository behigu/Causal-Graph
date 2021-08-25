from unittest import TestCase
from scripts import utils

class TestUtils(TestCase):
  def test_labeler(self):
    self.assertEqual(1, utils.labeler('M'))
    self.assertEqual(0, utils.labeler('B'))
    self.assertEqual(None, utils.labeler('A'))
