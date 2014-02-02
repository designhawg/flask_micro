#!/Users/grooves/.virtualenvs/flask_micro/bin/python

import os
import sys

if sys.platform == 'win32':
	pybabel = 'flask\\Scripts\\pybabel'
else:
	pybabel = '/Users/grooves/.virtualenvs/flask_micro/bin/pybabel'

os.system(pybabel + ' compile -d app/translations')