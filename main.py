
from absl import logging
from absl import flags
from absl import app

from . import cards_io

FLAGS = flags.FLAGS

flags.DEFINE_string('cards_dir', 'cards', 'The path to the cards')
flags.DEFINE_string('output', 'collection.apkg', 'The output collection')



def main(argv):
  del argv  # Unused.




if __name__ == '__main__':
  app.run(main)
