"""Load the cards data from the csv file/path."""

from typing import Dict, List, Tuple

import os
import csv
import glob

CardsTuples = List[Tuple[str, ...]]


def load_card(fname: str) -> CardsTuples:
  with open(fname) as f:
    reader = csv.reader(f)
    return list(reader)

def load_cards(dir: str) -> Dict[str, CardsTuples]:
  """Returns a dictionary of each entry per card."""
  res = {}
  for fname in glob.glob(f'{dir}/*.csv'):
    card = load_card(fname)
    title = os.path.basename(fname)
    title = title[:-len('.csv')]
    res[title] = card
  return res
