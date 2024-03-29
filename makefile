all: 
	make clean
	python3 src/Mindwave.py
run:
	python3 src/Mindwave.py
clean:
	rm -r journals/*
