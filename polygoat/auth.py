from flask import Blueprint, render_template, request, flash, session

import mysql.connector

auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
  return render_template("home.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  return render_template("sign_up.html")


@auth.route('/login', methods=['Get', 'Post'])
def login():
  return render_template("login.html")


@auth.route('/logout')
def logout():
  return "<p>logout</p>"


@auth.route('/chatroom')
def chat():
  return "<p>let's chat</p>"
