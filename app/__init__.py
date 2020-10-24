from flask import Flask

app = Flask(__name__, static_folder=r"E:\Docs\Lia\Python\week12\app\static")

from app import views