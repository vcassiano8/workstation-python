import pytest

from workstation_python.bioinformatics.sequences import (
    dna_to_protein,
    dna_to_rna,
    gc_content,
    reverse_complement,
    rna_to_protein,
)


def test_dna_to_rna():
    assert dna_to_rna("ATGC") == "AUGC"


def test_rna_to_protein():
    assert rna_to_protein("AUGGCC") == "MA"


def test_dna_to_protein():
    assert dna_to_protein("ATGGCC") == "MA"


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_gc_content():
    assert gc_content("ATGC") == 50.0


def test_gc_content_empty_sequence():
    with pytest.raises(ValueError):
        gc_content("")