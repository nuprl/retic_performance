TALK=nepls.rkt

all: show

compile:
	raco make -v nepls.rkt

preview: compile
	slideshow --right-half-screen ${TALK}

test: compile
	raco test nepls.rkt

show: compile
	slideshow ${TALK}

pdf: compile
	slideshow --condense --pdf ${TALK}
