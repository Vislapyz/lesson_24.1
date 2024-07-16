import re

from rest_framework.exceptions import ValidationError


class TitleValidator:

    def __init__(self, feild):
        self.feild = feild

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9\.\-\ ]+$')
        tmp_val = dict(value).get(self.feild)
        if not bool(reg.match(tmp_val)):
            raise ValidationError("Title is not ok")
