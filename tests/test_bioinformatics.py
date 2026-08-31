from workstation_python.bioinformatics.sequences import (
    complement_dna,
    gc_content,
    reverse_complement_dna,
    transcribe_dna,
    translate_rna,
    validate_dna,
)


def test_validate_dna():
    assert validate_dna("ATGCGT")
    assert not validate_dna("ATGCX")


def test_complement_dna():
    assert complement_dna("ATGC") == "TACG"


def test_reverse_complement_dna():
    assert reverse_complement_dna("ATGC") == "GCAT"


def test_transcribe_dna():
    assert transcribe_dna("ATGC") == "AUGC"


def test_gc_content():
    assert gc_content("ATGC") == 50.0


def test_translate_rna():
    assert translate_rna("AUGGCCAUUGUA") == "MAIV"