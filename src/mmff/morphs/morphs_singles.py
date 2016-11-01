from Bio import Seq
from Bio import SeqRecord
from Bio.Seq import MutableSeq
from copy import copy, deepcopy


def mmff_reverse(seq):
    # Keep all attributes from original
    new_seq = deepcopy(seq)
    mmff_seq = new_seq.seq.tomutable()
    mmff_seq.reverse()
    new_seq.seq = mmff_seq.toseq()
    return new_seq


def mmff_passthrough(seq):
    return seq
