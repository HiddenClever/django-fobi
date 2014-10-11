__title__ = 'fobi.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'RESTRICT_PLUGIN_ACCESS', 'FORM_ELEMENT_PLUGINS_MODULE_NAME',
    'FORM_HANDLER_PLUGINS_MODULE_NAME', 'FORM_CALLBACKS_MODULE_NAME',
    'THEMES_MODULE_NAME', 'DEFAULT_THEME', 'DISPLAY_AUTH_LINK',
    'WAIT_BETWEEN_TEST_STEPS', 'WAIT_AT_TEST_END', 'THEME_FOOTER_TEXT',
    'FORM_IMPORTER_PLUGINS_MODULE_NAME', 'CUSTOM_THEME_DATA',
    'DEBUG',
)

from django.utils.translation import ugettext

gettext = lambda s: s

# **************************************************************
# **************************************************************
# *************************** Core *****************************
# **************************************************************
# **************************************************************

# If set to True, plugins would be only accessible by the white-listed user(s) or group(s). If set to False, all
# users have the same access rights to all plugins.
RESTRICT_PLUGIN_ACCESS = True

# Name of the module in which the fobi form field plugins are registered.
FORM_ELEMENT_PLUGINS_MODULE_NAME = 'fobi_form_elements'

# Name of the module in which the fobi form handler plugins are registered.
FORM_HANDLER_PLUGINS_MODULE_NAME = 'fobi_form_handlers'

# Name of the module in which the fobi form importer plugins are registered.
FORM_IMPORTER_PLUGINS_MODULE_NAME = 'fobi_form_importers'

# Name of the module in which the fobi form calacks are registered.
FORM_CALLBACKS_MODULE_NAME = 'fobi_form_callbacks'

# Name of the module in which the fobi themes are discovered.
THEMES_MODULE_NAME = 'fobi_themes'

# Default theme
DEFAULT_THEME = 'bootstrap3'

DISPLAY_AUTH_LINK = True

WAIT_BETWEEN_TEST_STEPS = 2
WAIT_AT_TEST_END = 4

DEBUG = False

# **************************************************************
# **************************************************************
# ************************ Theme related ***********************
# **************************************************************
# **************************************************************
CUSTOM_THEME_DATA = {}
THEME_FOOTER_TEXT = '&copy; django-fobi example site 2014'

# **************************************************************
# **************************************************************
# *********************** Plugin related ***********************
# **************************************************************
# **************************************************************

DEFAULT_MAX_LENGTH = 255

FORM_HANDLER_PLUGINS_EXECUTION_ORDER = (
    'http_repost',
    'mail',
    # The 'db_store' is left out intentionally, since it should
    # be the last plugin to be executed.
)
