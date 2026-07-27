import logging

from .simple_wer import simple_wer, read_from_file
from .simple_wer_cli import *

logging.basicConfig(
    format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)
