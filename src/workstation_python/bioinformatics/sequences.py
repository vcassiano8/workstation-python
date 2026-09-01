from Bio.Seq import Seq


def dna_to_rna(sequence: str) -> str:
    """Transcribe a DNA sequence into RNA."""
    return str(Seq(sequence.upper()).transcribe())


def rna_to_protein(sequence: str) -> str:
    """Translate an RNA sequence into a protein sequence."""
    return str(Seq(sequence.upper()).translate(to_stop=False))


def dna_to_protein(sequence: str) -> str:
    """Transcribe DNA into RNA and translate it into protein."""
    return str(Seq(sequence.upper()).transcribe().translate(to_stop=False))


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    return str(Seq(sequence.upper()).reverse_complement())


def gc_content(sequence: str) -> float:
    """Calculate the GC content percentage of a DNA sequence."""
    sequence = sequence.upper()

    if not sequence:
        raise ValueError("Sequence cannot be empty.")

    valid_bases = {"A", "T", "C", "G"}

    if any(base not in valid_bases for base in sequence):
        raise ValueError("Sequence must contain only A, T, C and G.")

    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100