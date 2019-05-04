# VKhealth

[![Python 3.5](https://img.shields.io/badge/Python-3.5-blue.svg)](https://python.org)
[![VKhealth | GPL v3](https://img.shields.io/badge/VKhealth-GPL%20v3-blue.svg)](https://github.com/DaniilChizhevskii/vkhealth/blob/master/LICENSE.txt)

Module that shows the health of VKontakte platform.

# Requirements

[![bs4 >= 0.0.1](https://img.shields.io/badge/bs4->=%200.0.1-green.svg)](https://pypi.org/project/bs4/)

[![lxml >= 4.0](https://img.shields.io/badge/lxml->=4.0-green.svg)](https://pypi.org/project/lxml/)

[![requests >= 2.0](https://img.shields.io/badge/requests->=2.0-green.svg)](https://pypi.org/project/requests/)

# Usage

* Install package from [pypi.org](https://pypi.org).
* Import it using `import vkhealth` command.
* Run `vkhealth.get()` method.

# Output Format

Output contains the JSON file that sees like that:

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

# Autor

[![Daniil Chizhevskij](https://img.shields.io/badge/Daniil%20Chizhevskij-VKontakte-orange.svg)](https://vk.com/nochnoj_hichnik)

[![Email address](https://img.shields.io/badge/Daniil%20Chizhevskij-Email%20address-orange.svg)](mailto:daniilchizhevskij@gmail.com)
