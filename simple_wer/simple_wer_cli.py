import logging

import click

from .simple_wer import simple_wer, read_from_file


@click.command()
@click.option(
    "--test-name",
    default="test",
    help="The name for current test, it is used to distinguish the file names for different tests.",
)
@click.option(
    "--logdir",
    default="logs",
    help="The directory to write the WER results.",
)
@click.argument("refs")
@click.argument("hyps")
def cli(test_name, logdir, refs, hyps):
    """
    The shell entry point to simple-wer, a simple tool to calculate WERs for ASR.

    The ``refs`` and ``hyps`` are the paths for references and hypothesis, their
    format should be ``utt_id \\t refenence/hypothesis``.

    """
    logging.basicConfig(
        format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
        level=logging.INFO,
    )
    results = read_from_file(refs=refs, hyps=hyps)
    simple_wer(logdir=logdir, test_name=test_name, results=results)
