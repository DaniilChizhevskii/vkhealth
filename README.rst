VKhealth
========

|Python 3.5| |GPL v3|

Module that shows the health of VKontakte platform.

Requirements
============

|bs4 >= 0.0.1|

|lxml >= 4.0|

|requests >= 2.0|

Usage
=====

-  Install package from `pypi.org`_.
-  Import it using ``import vkhealth`` command.
-  Run ``vkhealth.get()`` method.

Output Format
=============

Output contains the JSON file that sees like that:

::

   {

     'module_name_1': {

       'working': true/false,

       'ping': 1 [s],

       'uptime': 100.0 [%]

     },

     'module_name_2': {

       'working': true/false,

       'ping': 1 [s],

       'uptime': 100.0 [%]

     }
     ...
   }

Autor
=====

|Daniil Chizhevskij|

|Email address|

.. _pypi.org: https://pypi.org

.. |Python 3.5| image:: https://img.shields.io/badge/Python-3.5-blue.svg
   :target: https://python.org
.. |GPL v3| image:: https://img.shields.io/badge/VKhealth-GPL%20v3-blue.svg
   :target: https://github.com/DaniilChizhevskii/vkhealth/blob/master/LICENSE.txt
.. |bs4 >= 0.0.1| image:: https://img.shields.io/badge/bs4-%3E=%200.0.1-green.svg
   :target: https://pypi.org/project/bs4/
.. |lxml >= 4.0| image:: https://img.shields.io/badge/lxml-%3E=4.0-green.svg
   :target: https://pypi.org/project/lxml/
.. |requests >= 2.0| image:: https://img.shields.io/badge/requests-%3E=2.0-green.svg
   :target: https://pypi.org/project/requests/
.. |Daniil Chizhevskij| image:: https://img.shields.io/badge/Daniil%20Chizhevskij-VKontakte-orange.svg
   :target: https://vk.com/nochnoj_hichnik
.. |Email address| image:: https://img.shields.io/badge/Daniil%20Chizhevskij-Email%20address-orange.svg
   :target: mailto:daniilchizhevskij@gmail.com
