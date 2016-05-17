**WARNING**: Please do NOT read this if you have not finished this project.

---

#1
find the string at 1af8

(input on $rdi)

#2

- has to be 6 numbers;
- 1st == 4th; 2nd == 5th; 3rd == 6th.
- 1st + 2nd + 3rd != 0

  0|----|----|----|----| #1-4
-16|---- ---- ---- ----| #5
-32|---- ---- ---- ----| #6

Well... So I choose a simple one.  

# 3

- scanf("%d %d", &a, &b)
- b == 0x36e (926), a < 0x7
- no need to go over those switch clauses

so...

# 4

- scanf("%d", &3rd)
- if n > 0: func4(n) recursion until n <=1
- if ret == 37 then OK (which means n == 9)

fun f n = 
	| 1 if n <=1
	| f (n-1) + f(n-2) otherwise

# 5

SYMBOL TABLE:
0000000000401ba0 l     O .rodata	0000000000000040              array.3014
Strings:
4eb1 array.3014

0xf: the index ($eax) has to be limited under 16

There is a hash list you have to find out by trying:
0 1 2 3 4 5 6 7 8 9 a b c d e f
-------------------------------
a 2 e 7 8 c f b 0 4 1 d 3 9 6 boom!

n_i = list[n_(i-1)]

We need to choose a start number (1st param) so that when we get f after exactly 0xc steps, and the sum of all these numbers along the path should add up to the 2nd param. So...

#6
The main func takes use strtol(input, 0, 10) to get my input number(s)

I actually have no idea what this func6 is doing, so I tried to input some random numbers to test its output, and monitor the $rdi, $rdx and $rax. It seems like that the $rax always ends up at pointing to a fixed position. Considering a final comparison between the input and (%rax), so I just go with this number on that position...

#Fin
Obviously, the same problem on the [official website](http://csapp.cs.cmu.edu/3e/students.html) seems much harder than the Coursera one. For example, no subroutines, and that makes challenge 6 a totally different monster.
