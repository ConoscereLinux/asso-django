"""
The membership management, from the single one to the MembersRegister.

"""

# Standard Import

# Site-package Import
from django.db import models

# Project Import
from common import models as cm



class Member(cm.EditInfo, cm.TrashBin):
    """It represents an AAssociation Member
    """
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        related_name = "member",
        verbose_name = _("User"),
        help_text = _("The User of the Member use for Login"))


class Membership(cm.EditInfo, cm.TrashBin):
    """The membership of an user for a particular period.
    """
    
    member = models.ForeignKey(
        'Member',
        on_delete = models.CASCADE,
        related_name = "member_memberships",
        verbose_name = _("Member"),
        help_text = _("The Member for that period"))


class MembersRegister(cm.Base, cm.EditInfo, cm.TrashBin):
    pass


class RegisterEntry(cm.EditInfo, cm.TrashBin):
    pass

