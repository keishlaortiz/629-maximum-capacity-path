I compiled and executed the program in build.tamu.edu that has installed the version 2.6.9 of Python

Command to compile and run the program:

python test.py

NOTE: To write the output to a file uncomment line 151:
sys.stdout = open("output5.txt","w")

NOTE: Running time of the entire program depends on V_NUM (number of vertices)

In test.py:
Change the number of vertices in line 15, currently is:
V_NUM = 1000

Also the program runs the algorithms 5 times for a 5-pairs of graphs. You can
change line 139 to speed up the compilation and execution:

TIMES = 5

Example:
TIMES = 5

V_NUM = 1000
Time: 43 s aprox

v_NUM = 2000
Time: 4 min aprox

v_NUM = 3000
Time: 10 min aprox

V_NUM = 4000
Time: 24 min aprox

V_NUM = 5000
Time: 39 min aprox

It takes so long because of the dense graphs