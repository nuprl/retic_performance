PAPER=dls

all: pdf

pdf: pkg setup texstyle.tex
	scribble ++extra figures \
           ++style texstyle.tex \
           --pdf $(PAPER).scrbl

tex: pkg setup texstyle.tex
	scribble ++style texstyle.tex --latex $(PAPER).scrbl

pkg:
	raco pkg install --skip-installed with-cache

setup:
	raco make ${PAPER}.scrbl

clean:
	rm -r compiled

