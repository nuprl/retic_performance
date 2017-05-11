all:
	raco pkg install --skip-installed ../../../dls html-parsing sxml
	racket scrape-PyPI.rkt simplejson requests Jinja2
	raco rp-python -s simplejson requests Jinja2
