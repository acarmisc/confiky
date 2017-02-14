Confiky
=======

Description
-----------

Confiky read one or more ``.ini`` file and create a ``Confiky`` object with ``ini`` sections as sub class
and file settings as attributes.

Usage
-----

Library must be importated as ::

    from confiky import Confiky

Then you can tell where to find settings ::

    config = Confiky(files=['foo/settings.ini', '/etc/bar.ini'])

You can limit sections by doing ::

    config = Confiky(files=['foo/settings.ini', '/etc/bar.ini'], required_sections=['server', 'email])

To see all sections readed ::

    config.sections

To access one specific setting ::

    # config.section_name.attribute_name
    mail_server = config.email.host

You can validate your config file by doing ::

    >>> config.validate(sections=['foo'], fields=['test1', 'test2', 'test3'])
    >>> {'fields_found': 3, 'sections_found'=1, all_found=True}

A shortcut is also present ::

    >>> config.is_validate(sections=['foo'], fields=['test1', 'test2', 'test3'])
    >>> True

If you want to see all your settings ::

    config.explain()

