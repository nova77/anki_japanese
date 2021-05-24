"""All the anki related stuff."""

import genanki

from typing import Iterator
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
{{Japanese}}<br/>({{Romanji}})
</div>
</div>
"""

DECK_ID = 8899424244


def get_notes(model: genanki.Model, cards: CardsTuples) -> Iterator[genanki.Note]:
  for fields in cards:
    yield genanki.Note(model, fields=fields)


def get_deck(deck_id: int, name: str, model: genanki.Model, cards: CardsTuples) -> genanki.Deck:
  deck = genanki.Deck(deck_id, name)
  for note in get_notes(model, cards):
    deck.add_note(note)
  return deck


def get_model(model_id: int, name: str):
  fields = [
      {'name': 'English'},
      {'name': 'Japanese'},
      {'name': 'Romanji'},
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
  genanki.Package(deck).write_to_file(path)  # 'theogony_vocab.apkg'
