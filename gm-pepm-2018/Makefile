PAPER=gm-pepm-2018
PKG=gm-pepm-2018

pdf: compile texstyle.tex
	scribble ++style texstyle.tex \
           --pdf $(PAPER).scrbl

all: pkg setup pdf

tex: compile texstyle.tex
	scribble ++style texstyle.tex \
           --latex $(PAPER).scrbl

pkg:
	raco pkg install --skip-installed

setup:
	raco setup ${PKG}

test:
	raco test -c ${PKG}

compile:
	raco make ${PAPER}.scrbl

clean:
	rm -r compiled

