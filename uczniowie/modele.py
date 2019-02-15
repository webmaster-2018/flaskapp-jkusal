#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'uczniowie.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE #
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    klasa = CharField()
    rok_naboru = IntegerField()
    rok_matury = IntegerField()
    

class Uczen(BazaModel):
    imie = CharField()
    nazwisko = CharField()
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

def main(args):
    baza.connect()
    baza.create_tables([Klasa, Uczen])


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
