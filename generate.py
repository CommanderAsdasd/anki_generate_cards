# -*- coding: utf-8 -*-
import genanki

print(genanki)



# забить что такое питоновое property

question = "1"
answer = "2"

my_deck = genanki.Deck(
  2059400110,
  'Country Capitals')

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


MyNote = genanki.Note(
  model=my_model,
  fields=[str(question), str(answer)])

MyNote.guid = genanki.guid_for(1, 2)
MyNote.sort_field = "null"

# class MyNote(genanki.Note):
#   self.model = None
#   @property
#   def guid(self):
#     return genanki.guid_for(self.fields[0], self.fields[1])
  
my_deck.add_note(MyNote)



genanki.Package(my_deck).write_to_file('outfiles/output.apkg')

print(dir(MyNote))