import os

from absl import logging
from absl import flags
from absl import app

import cards_io
import anki

FLAGS = flags.FLAGS

cards_dir = flags.DEFINE_string('cards_dir', 'cards', 'The path to the cards')
output_dir = flags.DEFINE_string(
    'output_dir', 'decks', 'The output dir where to write the decks')

model_id = flags.DEFINE_integer('model_id', 12345, 'The model id')
model_name = flags.DEFINE_string(
    'model_name', 'Japanese Decks', 'The model name')


def main(argv):
  del argv  # Unused.
  cards = cards_io.load_cards(cards_dir.value)
  logging.info(f'Loaded {len(cards)} cards.')
  model = anki.get_model(model_id.value, model_name.value)

  for name, cards in cards.items():
    deck = anki.get_deck(name, model, cards)
    os.makedirs(output_dir.value, exist_ok=True)
    output_fname = os.path.join(output_dir.value, f'{name}.apkg')
    anki.write_deck(deck, output_fname)
    logging.info(f'Wrote {output_fname}')

  logging.info('All done!')


if __name__ == '__main__':
  app.run(main)
