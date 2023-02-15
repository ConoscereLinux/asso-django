"""Some useful stuff."""

# Standard Import
import datetime

# Site-package Import

# Project Import

def current_year():
    """Return the current year.
    
    Used for default value in models.
    
    Returns (int): the current year at the moment of the call
    """
    
    return datetime.date.today().year

def current_date():
    """Return the current year.
    
    Used for default value in models.
    
    Returns (int): the current year at the moment of the call
    """
    return datetime.date.today()