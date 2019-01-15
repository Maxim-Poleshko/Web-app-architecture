"""Display developers using '/' route"""
from flask import Flask

APP = Flask(__name__)

class Developer:
    """Devepoers instance"""
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.programming_language = str(programming_language)

    def __str__(self):
        return '{first_name} {last_name} - {programming_language}'.format(first_name=self.first_name,
                                                                          last_name=self.last_name,
                                                                          programming_language=self.programming_language)

@APP.route('/')
def developer_controller():
    """Return str developers,using format"""
    fedor_dev = Developer('Fessssdor', 'Fedorov', 'Python')
    return f'{fedor_dev}'
