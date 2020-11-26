# -*- coding: utf-8 -*-

import uuid

from .confirm_register_form import ConfirmRegisterForm
from flask import request
from flask_security.forms import PasswordField, get_form_field_label, validators, EqualTo, NextFormMixin, config_value, _datastore, get_message

from openbbs_middleware import cfg


class RegisterForm(ConfirmRegisterForm, NextFormMixin):
    password_confirm = PasswordField(
        get_form_field_label("retype_password"),
        validators=[
            EqualTo("password", message="RETYPE_PASSWORD_MISMATCH"),
            validators.Optional(),
        ],
    )

    csrf_token = uuid.uuid4()

    def validate(self):
        if not super(RegisterForm, self).validate():
            return False

        if not config_value("UNIFIED_SIGNIN"):
            # password_confirm required
            if not self.password_confirm.data or not self.password_confirm.data.strip():
                self.password_confirm.errors.append(
                    get_message("PASSWORD_NOT_PROVIDED")[0]
                )
                return False

        return True

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        if not self.next.data:
            self.next.data = request.args.get("next", "")
