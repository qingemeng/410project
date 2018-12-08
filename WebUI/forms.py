# forms.py

from wtforms import Form, StringField#, SelectField, validators

class CodeSearchForm(Form):
#    choices = [('Artist', 'Artist'),
#               ('Album', 'Album'),
#               ('Publisher', 'Publisher')]
#    select = SelectField('Search for music:', choices=choices)
    search = StringField('Input your code search here')