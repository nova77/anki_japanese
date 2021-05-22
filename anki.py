"""All the anki related stuff."""

import genanki

from typing import Iterator
from cards_io import CardsTuples

CARD_STYLE = """
  .card {
    font-family: arial;
    font-size: 30px;
    text-align: center;
    color: black;
    background-color: white;
  }
  .from {
    font-style: italic;
  }
"""
DECK_ID = 8899424244


def get_notes(model: genanki.Model, cards: CardsTuples) -> Iterator[genanki.Note]:
  for front, back in cards:
    yield genanki.Note(model,
                       fields=[front, back])


def get_deck(id: int, name: str, model: genanki.Model, cards: CardsTuples) -> genanki.Deck:
  deck = genanki.Deck(id, name)
  for note in get_notes(model, cards):
    deck.add_note(note)
  return deck


def get_model(id: int, name: str):
  fields = [
      {'name': 'English'},
      {'name': 'Japanese'}
  ]
  templates = [
      {
          'name': 'Card 1',
          'qfmt': '{{English}}',
          'afmt': '{{FrontSide}}<hr id="answer">{{Japanese}}',
      }
  ]

  return genanki.Model(id, name, fields=fields,
                       templates=templates, css=CARD_STYLE)
