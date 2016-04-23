from flask import Flask
import logging

app = Flask(__name__)
if app.debug:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s', datefmt='%H:%M:%S')
else:
    logging.basicConfig(level=logging.INFO, format='%(levelname)s <%(asctime)s> : %(message)s', datefmt='%d.%m.%Y %H:%M:%S')


from app import views, data
data.load_song()
