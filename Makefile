CXX = gcc
CXXFLAGS = -w -g

os: 
	gcc -c -w -g -o anaylzer.o analyzer.c
	gcc -c -w -g -o parser.o parser.c
	gcc -c -w -g -o entry.o entry.c
	gcc -c -w -g -o main.o main.c

OBJECTS = analyzer.o parser.o entry.o

main: $(OBJECTS) main.o
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
	rm *.o main

