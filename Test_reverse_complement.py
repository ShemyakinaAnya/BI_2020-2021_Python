import unittest
import Nucleic_Acids_classes


class TestReverseComplement(unittest.TestCase):

    def setUp(self):
        self.reverse_complement = Nucleic_Acids_classes.reverse_complement

    def test_reverse_complement_for_RNA(self):
        complementarity_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        self.assertEqual(self.reverse_complement("AGUC", complementarity_rna), "GACU")

    def test_reverse_complement_for_RNA_false(self):
        complementarity_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        self.assertNotEqual(self.reverse_complement("AGUC", complementarity_rna), "CACU")

    def test_reverse_complement_for_DNA(self):
        complementarity_dna = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        self.assertEqual(self.reverse_complement("AGTC", complementarity_dna), "GACT")


if __name__ == '__main__':
    unittest.main()
