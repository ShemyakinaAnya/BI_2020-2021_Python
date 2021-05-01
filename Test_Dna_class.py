import unittest
import Nucleic_Acids_classes
from collections.abc import Iterable


class TestDna(unittest.TestCase):

    def setUp(self):
        self.Dna = Nucleic_Acids_classes.Dna("CAGGACTGTAGGCT")

    def test_iterablity(self):
        Dna_iterator = iter(self.Dna)
        self.assertEqual(isinstance(Dna_iterator, Iterable), True)

    def test_gc_content(self):
        self.assertEqual(self.Dna.gc_content(), 57)

    def test_reverse_complement(self):
        self.assertEqual(self.Dna.reverse_complement(), "AGCCTACAGTCCTG")

    def test_transcribe(self):
        self.assertEqual(self.Dna.transcribe().seq, "CAGGACUGUAGGCU")

if __name__ == '__main__':
    unittest.main()
