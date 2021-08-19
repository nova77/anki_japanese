"""All the anki related stuff."""

import hashlib
import itertools
from absl import logging
import genanki

from typing import Iterator, Optional
from cards_io import CardsTuples

CARD_STYLE = """
.front {
  background-color: white;
  font-family: arial;
  padding: 5px;
  border-radius: 30px;
}

.back {
  background-color: #caf2fe;
  font-family: arial;
  padding: 5px;
  border-radius: 30px;
}

.text {
  font-family: arial;
  font-size: 30px;
  color: black;
  text-align: center;
}
"""

FRONT_TEMPLATE = """
<div class=front>
<div class=text>
{{English}}
</div>
</div>
"""

BACK_TEMPLATE = """
{{FrontSide}}
<hr id="answer">
<div class=back>
<div class=text>
{{Japanese}}<br/>{{Other}}
</div>
</div>
"""


def hash_cards(cards: CardsTuples) -> int:
  values = list(itertools.chain.from_iterable(cards))
  values_str = ','.join(values).encode("utf-8")
  return int(hashlib.sha1(values_str).hexdigest(), 16) % (2 ** 61)


def get_notes(model: genanki.Model,
              cards: CardsTuples) -> Iterator[genanki.Note]:
  for en, ja, *other in cards:
    # other is optional
    other = f'({other[0]})' if (other and other[0]) else ''
    yield genanki.Note(model, fields=[en, ja, other])


def get_deck(name: str,
             model: genanki.Model,
             cards: CardsTuples,
             deck_id: Optional[int] = None) -> genanki.Deck:
  if deck_id is None:
    deck_id = hash_cards(cards)
    logging.info(f'"{name}" hashed as {deck_id}')

  deck = genanki.Deck(deck_id, name)
  for note in get_notes(model, cards):
    deck.add_note(note)
  return deck


def get_model(model_id: int, name: str):
  fields = [
    {'name': 'English'},
    {'name': 'Japanese'},
    {'name': 'Other'},
  ]
  templates = [
    {
      'name': 'en/ja',
      'qfmt': FRONT_TEMPLATE,
      'afmt': BACK_TEMPLATE
    }
  ]

  return genanki.Model(model_id, name, fields=fields,
                       templates=templates, css=CARD_STYLE)


def write_deck(deck: genanki.Deck, path: str):
  genanki.Package(deck).write_to_file(path)
