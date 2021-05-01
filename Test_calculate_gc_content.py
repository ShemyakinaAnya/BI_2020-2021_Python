import unittest
import Nucleic_Acids_classes


class TestCalculateGCContent(unittest.TestCase):

    def setUp(self):
        self.gc_content = Nucleic_Acids_classes.calculate_gc_content

    def test_gc_content_calculation(self):
        self.assertEqual(self.gc_content("AGTC"), 55)
        self.assertEqual(self.gc_content("GGCC"), 100)


if __name__ == '__main__':
    unittest.main()
