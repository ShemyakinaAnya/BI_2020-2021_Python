import unittest
import Nucleic_Acids_classes
from collections.abc import Iterable


class TestRna(unittest.TestCase):

    def setUp(self):
        self.Rna = Nucleic_Acids_classes.Rna("CAGGACUGUAGGCU")

    def test_iterablity(self):
        Rna_iterator = iter(self.Rna)
        self.assertEqual(isinstance(Rna_iterator, Iterable), True)

    def test_gc_content(self):
        self.assertEqual(self.Rna.gc_content(), 57)

    def test_reverse_complement(self):
        self.assertEqual(self.Rna.reverse_complement(), "AGCCUACAGUCCUG")


if __name__ == '__main__':
    unittest.main()
