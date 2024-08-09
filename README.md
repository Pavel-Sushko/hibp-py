![python versions](https://img.shields.io/pypi/pyversions/hibp-py.svg?logo=python&logoColor=white) ![package versions](https://img.shields.io/pypi/v/hibp-py.svg)

![pypi version](https://github.com/Pavel-Sushko/hibp-py/actions/workflows/python-publish.yml/badge.svg) ![python application](https://github.com/Pavel-Sushko/hibp-py/actions/workflows/python-app.yml/badge.svg) ![dependency review](https://github.com/Pavel-Sushko/hibp-py/actions/workflows/dependency-review.yml/badge.svg)

# hibp-py

hibp-py is a Python library that facilitates the analysis and tracking of breaches posted to haveibeenpwned.

## Installation

1. Install from pip: `python -m pip install hibp-py`

## Basic Usage

```bash
$ python -m hibp_py -h
Welcome to HIBP Python!
usage: __main__.py [-h] [-iL INPUT_LIST] [-o OUTPUT] [-D ACTIVE_DIRECTORY] [-e EMAIL_CONFIG]

options:
  -h, --help            show this help message and exit
  -iL INPUT_LIST, --input-list INPUT_LIST
                        Input list of emails or haveibeenpwned JSON file
  -o OUTPUT, --output OUTPUT
                        Output file name
  -D ACTIVE_DIRECTORY, --active-directory ACTIVE_DIRECTORY
                        Active Directory domain
  -e EMAIL_CONFIG, --email-config EMAIL_CONFIG
                        Email configuration file
```

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## License

hibp-py is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use it for personal or commercial use.
