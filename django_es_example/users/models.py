import datetime

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db.models import CharField, DateField, TextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

from django_es_example.users.elastic_models import ElasticUser


@deconstructible
class CustomUsernameValidator(validators.RegexValidator):
    regex = r'^[a-z]{4,}$'
    message = _(
        'Enter a valid username. This value may contain only lower case and more then 4 characters.',
    )
    flags = 0


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    username_validator = CustomUsernameValidator()
    username = CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('More than 4 characters and lower case.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = CharField(_('first name'),
                           max_length=20,
                           blank=False,
                           null=False,
                           help_text=_('Required, less than 20 characters.'))
    birthday = DateField(_('birthday'),
                         blank=True,
                         null=True,
                         # default=datetime.date.today(),
                         help_text=_('Date type: YYYY-MM-DD'))
    address = TextField(_('address'), blank=True, default="")
    description = TextField(_('description'), blank=True, default="")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


@receiver(post_save, sender=User)
def receiver_post_save(sender, **kwargs):
    instance = kwargs.get('instance', '')
    created = kwargs.get('created')
    if isinstance(instance, User) and created:
        dic = instance.__dict__
        u = ElasticUser(**dict(username=dic.get("username"),
                               first_name=dic.get("first_name"),
                               last_name=dic.get("last_name"),
                               address=dic.get("address", ""),
                               birthday=dic.get("birthday", None),
                               description=dic.get("description")))
        u.save(index="elastic_user")
