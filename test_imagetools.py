__author__ = 'charles'

import unittest
import imgtools

class TestImgTools(unittest.TestCase):

    def test_img_tools_tallys_returns_image(self):
        self.assertIsNotNone(imgtools.generate_tally_mask(5))