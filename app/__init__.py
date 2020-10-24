from flask import Flask
import pathlib

cdir = pathlib.Path(__file__).parent

app = Flask(__name__, static_folder=str(cdir/"static"))

from app import views