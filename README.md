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

You can automatically import a po file in some language:

```python
`python manage.py extract_translations -l fr locale/fr/messages.po`
```
> the extract_translations does not override or delete exising strings.

Or do it manually:

get to your admin (transadmin > Translation) and add:
- source: "String to translate"
- language: "fr"
- trans: "Chaine à traduire"


View your website in French.


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
