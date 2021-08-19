### What is this?

A simple tool to create Anki cards from csv files to help me learn japanese.

### Usage examples

```bash
# by default it will look into the "cards" directory for csv files 
# and output to "decks":
python main.py

# you can specify the cards & output directory with their 
# corresponding flag:
python main.py --cards_dir /my/csv/files --output_dir  /tmp/mycards
```

### CSV format

The csv is formatted as

    <front>,<back (primary)>,<back (secondary)>

eg

    big,ōkī,ōkī akai ringo -> Big red apple
    quiet,shizuka,
    am,ごぜん,gozen

The secondary entry for the back is optional and will be displayed below
the primary and in parenthesis.
