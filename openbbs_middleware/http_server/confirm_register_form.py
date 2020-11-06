# -*- coding: utf-8 -*-


from flask_security.forms import Form, PasswordField, get_form_field_label, validators, config_value, _datastore, _security, get_message, Field, StringField

from openbbs_middleware import cfg

from .register_form_mixin import RegisterFormMixin
from .utils import validate_user
from .utils import get_ip


class ConfirmRegisterForm(Form, RegisterFormMixin):
    user_id = StringField(
        get_form_field_label("username"), validators=[],
    )

    username = StringField(
        get_form_field_label("username"), validators=[],
    )

    password = PasswordField(
        get_form_field_label("password"), validators=[validators.Optional()]
    )

    jwt = StringField(
        get_form_field_label("jwt"), validators=[],
    )

    def validate(self):
        if not super(ConfirmRegisterForm, self).validate():
            return False

        # XXX hack with user_id data
        if not self.user_id.data and self.username.data:
            self.user_id.data = self.username.data

        # To support unified sign in - we permit registering with no password.
        if not config_value("UNIFIED_SIGNIN"):
            # password required
            if not self.password.data or not self.password.data.strip():
                self.password.errors.append(get_message("PASSWORD_NOT_PROVIDED")[0])
                return False

        if not self.password.data:
            return False

        if self.password.data:
            # We do explicit validation here for passwords
            # (rather than write a validator class) for 2 reasons:
            # 1) We want to control which fields are passed -
            #    sometimes that's current_user
            #    other times it's the registration fields.
            # 2) We want to be able to return multiple error messages.

            rfields = {}
            for k, v in self.data.items():
                if hasattr(_datastore.user_model, k):
                    rfields[k] = v
            if 'password' in rfields:
                del rfields["password"]

            pbad = _security._password_validator(self.password.data, True, **rfields)

            # validate with ptt-server

            user_id = self.user_id.data
            password = self.password.data
            ip = get_ip()

            err, jwt = validate_user(user_id, password, ip)
            if err is not None:
                return False

            self.jwt.data = jwt

        return True
