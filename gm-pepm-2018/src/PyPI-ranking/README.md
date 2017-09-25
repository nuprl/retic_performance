PyPI-ranking
===

This directory contains code from three Python libraries,
 referenced in "Section 6: Threats to Validity".

The libraries are:

- `simplejson`
- `requests`
- `Jinja2`


Organization
---

- `Makefile` : a script for reproducing the claims in Section 6
- `README.md` : this file
- `scrape-PyPI.rkt` : scrape `PyPI.html` for rankings
- `PyPI.html` : the PyPI package ranking
  - all package are within the top 20
  - accessed 2017-05-11
- `simplejson/` : code,
  - from the master branch of `https://github.com/simplejson/simplejson`
  - commit `09e6e009878587ce7d65651dc35cf1f276f5dbd9`
  - the `simplejson/` subfolder
  - accessed 2017-05-09
- `requests/` : code,
  - from the master branch of `https://github.com/kennethreitz/requests/`
  - commit `508d47dc6e7458f2db3bc3b3bf629e0bdb1b798a`
  - the `requests/` subfolder
  - accessed 2017-05-09
- `Jinja2/` : directory
  - from the master branch of `https://github.com/pallets/jinja`
  - commit `d905cf0b6c6121d900ea384f72970b862c879bc7`
  - the `jinja2/` subfolder
  - accessed 2017-05-09


Claims
---

Section 6 of the paper claims that the libraries are:
- small
- popular
- have X many functions and methods, where X is:
  - `simplejson` : over 50
  - `requests` : over 200
  - `Jinja2` : over 600

To reproduce these claims, run `make` in the current directory.


Expected Output
---

```
$ make
raco pkg install --skip-installed ../../../dls html-parsing sxml
racket scrape-PyPI.rkt simplejson requests Jinja2
- simplejson is ranked 1st
- requests is ranked 4th
- Jinja2 is ranked 16th
raco rp-python -s simplejson requests Jinja2
simplejson
- 7 modules
- 22 functions
- 6 classes
- 26 methods
requests
- 15 modules
- 59 functions
- 40 classes
- 149 methods
Jinja2
- 26 modules
- 136 functions
- 146 classes
- 503 methods
```
