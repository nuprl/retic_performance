PAPER=dls
PKG=gm-dls-2017

all: pkg setup pdf

pdf: compile texstyle.tex
	scribble ++extra figures \
           ++style texstyle.tex \
           --pdf $(PAPER).scrbl

tex: compile texstyle.tex
	scribble ++style texstyle.tex --latex $(PAPER).scrbl

pkg:
	raco pkg install --skip-installed

setup:
	raco setup ${PKG}

compile:
	raco make ${PAPER}.scrbl

clean:
	rm -r compiled

