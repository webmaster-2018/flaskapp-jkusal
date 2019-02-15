# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')
    
@app.route('/listak')
def listak():
    """Lista klas"""
    klasy = Klasa.select()
    return render_template('listak.html')
    
@app.route('/listau')
def listau():
    """Lista uczniów"""
    uczniowie = Uczen.select()
    return render_template('listau.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

