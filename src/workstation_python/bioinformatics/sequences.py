from Bio.Seq import Seq


def validate_dna(sequence: str) -> bool:
    """Return True if a sequence contains only valid DNA bases."""
    sequence = sequence.upper()
    return bool(sequence) and all(base in "ACGT" for base in sequence)


def complement_dna(sequence: str) -> str:
    """Return the complementary DNA strand."""
    return str(Seq(sequence).complement())


def reverse_complement_dna(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    return str(Seq(sequence).reverse_complement())


def transcribe_dna(sequence: str) -> str:
    """Transcribe DNA into RNA."""
    return str(Seq(sequence).transcribe())


def gc_content(sequence: str) -> float:
    """Calculate GC content as a percentage."""
    sequence = sequence.upper()

    if not validate_dna(sequence):
        raise ValueError("Invalid DNA sequence.")

    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100


def translate_rna(sequence: str) -> str:
    """Translate an RNA sequence into a protein sequence."""
    return str(Seq(sequence).translate(to_stop=False))