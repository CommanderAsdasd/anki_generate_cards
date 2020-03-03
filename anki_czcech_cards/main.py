import genanki, random
import sys
# import pdb


def gen_deck(deckname):

    my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        deckname)

    return my_deck

def gen_card(deck, front, back):
    my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],

    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Question}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

    my_note = genanki.Note(
    model=my_model,
    fields=[front, back])

    deck.add_note(my_note)
    return deck

def write_base(deck, filename):
    genanki.Package(deck).write_to_file(filename)

def parse_data(file_name):
    curr_deck = None
    with open(file_name, 'r') as file_obj:
        for line in file_obj:
            if line[0] == "*":
                if not curr_deck:
                    curr_deck = gen_deck(line[1::])
                else:
                    print("saving deck...")
                    write_base(curr_deck, "{}.apkg".format(line[1::]))
                    curr_deck = gen_deck(line[1::])
            elif line != "\n":
                front = line.split("-")[0]
                back = line.split("-")[1].replace("\n","")
                gen_card(curr_deck, front, back)



parse_data(sys.argv[1])
