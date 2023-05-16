# simple-wer
A simple command line tool to calculate WER for ASR.


## Installation

```
pip install simple-wer
```


## Usage

```
$ simple-wer --help
Usage: simple-wer [OPTIONS] REFS HYPS

  The shell entry point to simple-wer, a simple tool to calculate WERs for
  ASR.

  The ``refs`` and ``hyps`` are the paths for references and hypothesis, their
  format should be ``utt_id \t refenence/hypothesis``.

Options:
  --test-name TEXT  The name for current test, it is used to distinguish the
                    file names for different tests.
  --logdir TEXT     The directory to write the WER results.
  --help            Show this message and exit.
```

For example:

The `refs.txt` contains:

```
1       I LOVE YOU
2       I HATE YOU
```

The `hyps.txt` contains:

```
1       i LOVE YOU
2       I hate YOU
```

Run the following command:

```
simple-wer --test-name example refs.txt hyps.txt
```

The logs look like:

```
2023-05-16 11:16:05,253 INFO [simple_wer.py:21] The transcripts are stored in logs/recogs-example.txt
2023-05-16 11:16:05,255 INFO [simple_wer.py:123] [example] %WER 33.33% [2 / 6, 0 ins, 0 del, 2 sub ]
2023-05-16 11:16:05,257 INFO [simple_wer.py:29] Wrote detailed error stats to logs/errs-example.txt
```

There will be two files (`recogs-example.txt` and `errs-example.txt`) in logs,

`recogs-example.txt` looks like:

```
1:      ref=['I', 'LOVE', 'YOU']
1:      hyp=['i', 'LOVE', 'YOU']

2:      ref=['I', 'HATE', 'YOU']
2:      hyp=['I', 'hate', 'YOU']
```

`errs-example.txt` looks like:

```
%WER = 33.33
Errors: 0 insertions, 0 deletions, 2 substitutions, over 6 reference words (4 correct)
Search below for sections starting with PER-UTT DETAILS:, SUBSTITUTIONS:, DELETIONS:, INSERTIONS:, PER-WORD STATS:

PER-UTT DETAILS: corr or (ref->hyp)  
1:      (I->i) LOVE YOU
2:      I (HATE->hate) YOU

SUBSTITUTIONS: count ref -> hyp
1   I -> i
1   HATE -> hate

DELETIONS: count ref

INSERTIONS: count hyp

PER-WORD STATS: word  corr tot_errs count_in_ref count_in_hyp
i   0 1 0 1
hate   0 1 0 1
I   1 1 2 1
HATE   0 1 1 0
YOU   2 0 2 2
LOVE   1 0 1 1
```
