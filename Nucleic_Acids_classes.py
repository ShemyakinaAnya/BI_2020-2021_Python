def reverse_complement(seq, complementarity):
    bases = list(seq)
    bases = [complementarity[base] for base in bases]
    reversed_complement = ''.join(bases)[::-1]
    return reversed_complement


def calculate_gc_content(seq):
    gc_counts = 0
    for base in seq:
        if base == 'G' or base == 'C':
            gc_counts += 1
    gc_content = int(gc_counts / len(seq) * 100)
    return gc_content


class BaseIterator:
    def __init__(self, seq):
        self.seq = seq
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.seq[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


class Rna:
    def __init__(self, seq):
        self.seq = seq.upper()

    def __iter__(self):
        return BaseIterator(self)

    def gc_content(self):
        return calculate_gc_content(self.seq)

    def reverse_complement(self):
        complementarity = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        return reverse_complement(self.seq, complementarity)


class Dna:
    def __init__(self, seq):
        self.seq = seq.upper()

    def __iter__(self):
        return BaseIterator(self)

    def gc_content(self):
        return calculate_gc_content(self.seq)

    def reverse_complement(self):
        complementarity = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return reverse_complement(self.seq, complementarity)

    def transcribe(self):
        transcribed_DNA = []
        for base in self.seq:
            if base == 'T':
                transcribed_DNA.append('U')
            else:
                transcribed_DNA.append(base)
        transcribed_DNA = Rna(''.join(transcribed_DNA))
        return transcribed_DNA
