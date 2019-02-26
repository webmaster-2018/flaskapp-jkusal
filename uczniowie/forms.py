# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField("Klasa id")
    klasa = StringField('Nazwa klasy: ', validators=[Required(message="blad_1")])
    rok_naboru = StringField('Rok naboru: ', validators=[Required(message="blad_1")])
    rok_matury = StringField('Rok matury: ', validators=[Required(message="blad_1")])
    
class UczenForm(FlaskForm):
    id = HiddenField()
    imie = StringField('Imię ucznia: ', validators=[Required(message="blad_1")])
    nazwisko = StringField('Nazwisko ucznia: ', validators=[Required(message="blad_1")])
    plec = SelectField('Płeć ucznia: ', coerce=int)
    klasa = SelectField('Klasa: ', coerce=int)
