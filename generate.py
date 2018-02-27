# -*- coding: utf-8 -*-
import genanki

print(genanki)



# забить что такое питоновое property

Questions = ["False","class","finally","is","return",
"None","continue","for","lambda","try","True","def","from","nonlocal","while","and","del","global","not","with",
"as","elif","if","or","yield","assert","else","import","pass"," break","except","in","raise"]

deckName = "Python keywords"

my_deck = genanki.Deck(2059400111,str(deckName))

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

for i, string in enumerate(Questions):
  MyNote = genanki.Note(model=my_model,fields=[str(Questions[i]), " "])
  MyNote.guid = genanki.guid_for(1, 2)
  MyNote.sort_field = "null"
  my_deck.add_note(MyNote)

# class MyNote(genanki.Note):
#   self.model = None
#   @property
#   def guid(self):
#     return genanki.guid_for(self.fields[0], self.fields[1])


genanki.Package(my_deck).write_to_file('outfiles/{0}.apkg'.format(str(deckName)))