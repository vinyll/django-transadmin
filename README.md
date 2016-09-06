# Django Transadmin - Translate your text from the admin

Categories: (translation, internationalization, i18n)

[![Build Status](https://api.travis-ci.org/vinyll/django-transadmin.png)](http://travis-ci.org/vinyll/django-transadmin)

Works on Python 3.x and Python 2.6 or more.

Compatible with the default Django template, [Jinja2](http://jinja.pocoo.org/) and [Jingo](https://github.com/jbalogh/jingo)


#### Benefits

Administrate your translations directly from the admin.
Import your translations string from po files.
Compatible with [Jingo](https://github.com/jbalogh/jingo)


#### Quick tour

In a template:

```html
{{ _("String to translate") }}
```

In a python file:

```python
from transadmin.helpers import _

translated_text = _("String to translate")
```

##### Import translation

You can directly create a string to translate from the admin.
When it comes to generate many pages, you may prefer the automation script.

##### Manually

get to your admin (transadmin > Translation) and add:
- source: "String to translate"
- language: "fr"
- trans: "Chaine à traduire"


##### Automation script

Django allows you to generate _po_ files from templates, views and so on:
```bash
django-admin.py makemessages -l fr
```

_Transadmin_ then allows you to import a _po_ file into the database:

```bash
python manage.py transadmin_import my/fr/file.po -l fr
```

This command reads translations from _my/file.po_ and import every string into
the database for _fr_ language.

Your untranslated strings are now ready to get translated from the admin!

> Even though the `transadmin_import` command is safe and preserves
> your existing data. You are highly encouraged to make a backup before running
> such commands.

You can now view your website in French.


## Installation

#### Download

Via pip ![latest version](https://pypip.in/v/django-transadmin/badge.png)

```bash
pip install django-transadmin
```

or the bleeding edge version

```bash
pip install -e git+https://github.com/vinyll/django-transadmin.git#egg=django-transadmin
```

#### update INSTALLED_APPS

In _settings.py_, add _transadmin_ in your INSTALLED_APPS

```python
INSTALLED_APPS = (
	# …,
	'transadmin',
)
```

Congratulations, you're all set!


#### Configuration

A few settings are available:

- `TRANSADMIN_LANGUAGES`: a tuple of tuples for available languages for the admin. Reads the settings.LANGUAGES by default.
- `TRANSADMIN_CONTEXTS`: a tuple of tuples for available context. Free text by default.
- `TRANSADMIN_FALLBACK_LANGUAGE`: a string representing the code of the language
to fallback to if a string is not translated into the current language.
No fallback by default, displays the untranslated text.
