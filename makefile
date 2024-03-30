all: 
	python3 src/Mindwave.py
run:
	make clean
	python3 src/Mindwave.py
clean:
	rm -r journals/*
