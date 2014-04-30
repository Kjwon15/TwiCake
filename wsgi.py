import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app as application

application.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
application.config.update(
    consumer_key='o7vgHO8hRGPl62L9xokp76Fan',
    consumer_secret='DuBOE39WluGJeRdUtz3sXAN7pjPr4mtoaRJYe5IueIRaeOejID'
)

application.debug = True
