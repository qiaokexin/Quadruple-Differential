This repository contains supplementary material of the paper 
# Quadruple Differential Distinguishers and MILP-based Automatic Searching Methods. 



The structure of the folder is as follows
- [AES](#AES)
	- [2r](#2r)
		- [lp](#lp)
		- [sol](#sol)
	- [3r](#3r)
		- [lp](#lp)
		- [sol](#sol)
	- [4r](#4r)
		- [lp](#lp)
		- [sol](#sol)
	- [5r](#5r)
		- [lp](#lp)
		- [sol](#sol)
	- [CRAFT](#CRAFT)
	- [LBlock](#LBlock)
		
All the experiments are executed on a laptop with 8 logic processors, 11th Gen Intel(R) Core(TM) i7-1160G7 @ 1.20GHz 2.11 GHz, 16G RAM.    
	 

[AES] folder contains results corresponding to `Table XI` in the paper. [2r] folder contains MILP instances in [lp] and corresponding solution files in [sol] with r=2. In [lp], `AES_2r_collide1_case0.lp` corresponds to the instance with r=2, with 0-th (|K|,|I|,|J|) case and outputs collides on one column. In [sol], `AES_2r_collide1_case0_0.sol` represents the 0-th solution file. For r=3 and r=4, the rule goes the same. For r=3 and colliding on 3 columns cases, as there are too many solution files we only give the output of the programm `runGurobi.py` where we collect and do some statistics on the top 700 optimal solutions. To reproduce the results, Gurobi optimizer and python interface need to be installed. Then run

```sh
python runGurobi.py
```
Change lp file directories and settings in `runGurobi.py` to test other instances.

[CRAFT] folder contains the verification codes to verify the quadruple distinguishers we found. To run the programm, MPI package need to be installed and change the library path and include path in Makefile according to your installation. Run `mingw32-make` (in Windows) to compile the C++ codes. 

To test 6-round by running on 8 processors, run

```sh
mpiexec -n 8 CRAFT_Quadruple_MPI_RNG 6
```
You get a summary of number of quaries and number of right quadruples on each process, total queries, number of total right quadruples and the probability. We also reserved codes (commented in current version) for comparison with full round CRAFT as random permutation. 
```
[+] Proc 0
[+] PRNG initialized to 0xD19EC404

 Quaries on each process = 2^(8.000000)
 0 proc:     Right = 2^(8.000000)
 1 proc:     Right = 2^(8.000000)
 2 proc:     Right = 2^(8.000000)
 3 proc:     Right = 2^(8.000000)
 4 proc:     Right = 2^(8.000000)
 5 proc:     Right = 2^(8.000000)
 6 proc:     Right = 2^(8.000000)
 7 proc:     Right = 2^(8.000000)

                              Total queries = 2^(11.000000)
CRAFT:     Number of total right quadruples = 2^(11.000000)
           Probability of right quadruples  = 2^(-0.0000)
 time on clock(): 0.002


[+] Proc 6
[+] PRNG initialized to 0xD19EC40A
[+] Time : 0.000394
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 4
[+] PRNG initialized to 0xD19EC408
[+] Time : 0.000409
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 2
[+] PRNG initialized to 0xD19EC406
[+] Time : 0.000359
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 7
[+] PRNG initialized to 0xD19EC40B
[+] Time : 0.000415
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)

[+] Time : 0.000403
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 5
[+] PRNG initialized to 0xD19EC409
[+] Time : 0.000405
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 1
[+] PRNG initialized to 0xD19EC405
[+] Time : 0.000408
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 3
[+] PRNG initialized to 0xD19EC407
[+] Time : 0.000401
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)

```

Results on 7-round：

```
[+] Proc 0
[+] PRNG initialized to 0xD19EE056

 Quaries on each process = 2^(8.000000)
 0 proc:     Right = 2^(8.000000)
 1 proc:     Right = 2^(8.000000)
 2 proc:     Right = 2^(8.000000)
 3 proc:     Right = 2^(8.000000)
 4 proc:     Right = 2^(8.000000)
 5 proc:     Right = 2^(8.000000)
 6 proc:     Right = 2^(8.000000)
 7 proc:     Right = 2^(8.000000)

                              Total queries = 2^(11.000000)
CRAFT:     Number of total right quadruples = 2^(11.000000)
           Probability of right quadruples  = 2^(-0.0000)
 time on clock(): 0.003


[+] Proc 1
[+] PRNG initialized to 0xD19EE057
[+] Time : 0.000440
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)

[+] Time : 0.000414
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 7
[+] PRNG initialized to 0xD19EE05D
[+] Time : 0.000439
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 2
[+] PRNG initialized to 0xD19EE058
[+] Time : 0.000435
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 6
[+] PRNG initialized to 0xD19EE05C
[+] Time : 0.000433
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 3
[+] PRNG initialized to 0xD19EE059
[+] Time : 0.000433
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 5
[+] PRNG initialized to 0xD19EE05B
[+] Time : 0.000424
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)


[+] Proc 4
[+] PRNG initialized to 0xD19EE05A
[+] Time : 0.000274
[+] CRAFT:         Number of right quadruples = 2^(8.000000)
[+]           Probability of right quadruples = 2^(-0.0000)
```

Results on 8-round:

```
[+] Proc 0
[+] PRNG initialized to 0xD19EEA06

 Quaries on each process = 2^(16.000000)
 0 proc:     Right = 2^(13.506308)
 1 proc:     Right = 2^(13.512123)
 2 proc:     Right = 2^(13.535883)
 3 proc:     Right = 2^(13.534303)
 4 proc:     Right = 2^(13.511629)
 5 proc:     Right = 2^(13.535761)
 6 proc:     Right = 2^(13.505067)
 7 proc:     Right = 2^(13.521478)

                              Total queries = 2^(19.000000)
CRAFT:     Number of total right quadruples = 2^(16.520373)
           Probability of right quadruples  = 2^(-2.4796)
 time on clock(): 0.103

[+] Time : 0.101380
[+] CRAFT:         Number of right quadruples = 2^(13.506308)
[+]           Probability of right quadruples = 2^(-2.4937)


[+] Proc 1
[+] PRNG initialized to 0xD19EEA07
[+] Time : 0.102427
[+] CRAFT:         Number of right quadruples = 2^(13.512123)
[+]           Probability of right quadruples = 2^(-2.4879)


[+] Proc 6
[+] PRNG initialized to 0xD19EEA0C
[+] Time : 0.098035
[+] CRAFT:         Number of right quadruples = 2^(13.505067)
[+]           Probability of right quadruples = 2^(-2.4949)


[+] Proc 7
[+] PRNG initialized to 0xD19EEA0D
[+] Time : 0.100957
[+] CRAFT:         Number of right quadruples = 2^(13.521478)
[+]           Probability of right quadruples = 2^(-2.4785)


[+] Proc 5
[+] PRNG initialized to 0xD19EEA0B
[+] Time : 0.098529
[+] CRAFT:         Number of right quadruples = 2^(13.535761)
[+]           Probability of right quadruples = 2^(-2.4642)


[+] Proc 2
[+] PRNG initialized to 0xD19EEA08
[+] Time : 0.097905
[+] CRAFT:         Number of right quadruples = 2^(13.535883)
[+]           Probability of right quadruples = 2^(-2.4641)


[+] Proc 3
[+] PRNG initialized to 0xD19EEA09
[+] Time : 0.099072
[+] CRAFT:         Number of right quadruples = 2^(13.534303)
[+]           Probability of right quadruples = 2^(-2.4657)


[+] Proc 4
[+] PRNG initialized to 0xD19EEA0A
[+] Time : 0.100430
[+] CRAFT:         Number of right quadruples = 2^(13.511629)
[+]           Probability of right quadruples = 2^(-2.4884)
```

Results on 9-round:

```
[+] Proc 0
[+] PRNG initialized to 0xD19EEA06

 Quaries on each process = 2^(16.000000)
 0 proc:     Right = 2^(13.506308)
 1 proc:     Right = 2^(13.512123)
 2 proc:     Right = 2^(13.535883)
 3 proc:     Right = 2^(13.534303)
 4 proc:     Right = 2^(13.511629)
 5 proc:     Right = 2^(13.535761)
 6 proc:     Right = 2^(13.505067)
 7 proc:     Right = 2^(13.521478)

                              Total queries = 2^(19.000000)
CRAFT:     Number of total right quadruples = 2^(16.520373)
           Probability of right quadruples  = 2^(-2.4796)
 time on clock(): 0.103

[+] Time : 0.101380
[+] CRAFT:         Number of right quadruples = 2^(13.506308)
[+]           Probability of right quadruples = 2^(-2.4937)


[+] Proc 1
[+] PRNG initialized to 0xD19EEA07
[+] Time : 0.102427
[+] CRAFT:         Number of right quadruples = 2^(13.512123)
[+]           Probability of right quadruples = 2^(-2.4879)


[+] Proc 6
[+] PRNG initialized to 0xD19EEA0C
[+] Time : 0.098035
[+] CRAFT:         Number of right quadruples = 2^(13.505067)
[+]           Probability of right quadruples = 2^(-2.4949)


[+] Proc 7
[+] PRNG initialized to 0xD19EEA0D
[+] Time : 0.100957
[+] CRAFT:         Number of right quadruples = 2^(13.521478)
[+]           Probability of right quadruples = 2^(-2.4785)


[+] Proc 5
[+] PRNG initialized to 0xD19EEA0B
[+] Time : 0.098529
[+] CRAFT:         Number of right quadruples = 2^(13.535761)
[+]           Probability of right quadruples = 2^(-2.4642)


[+] Proc 2
[+] PRNG initialized to 0xD19EEA08
[+] Time : 0.097905
[+] CRAFT:         Number of right quadruples = 2^(13.535883)
[+]           Probability of right quadruples = 2^(-2.4641)


[+] Proc 3
[+] PRNG initialized to 0xD19EEA09
[+] Time : 0.099072
[+] CRAFT:         Number of right quadruples = 2^(13.534303)
[+]           Probability of right quadruples = 2^(-2.4657)


[+] Proc 4
[+] PRNG initialized to 0xD19EEA0A
[+] Time : 0.100430
[+] CRAFT:         Number of right quadruples = 2^(13.511629)
[+]           Probability of right quadruples = 2^(-2.4884)
```

Results on 10-round:

```
[+] Proc 0
[+] PRNG initialized to 0xD1A66394

 Quaries on each process = 2^(32.000000)
 0 proc:     Right = 2^(-inf)
 1 proc:     Right = 2^(-inf)
 2 proc:     Right = 2^(0.000000)
 3 proc:     Right = 2^(-inf)
 4 proc:     Right = 2^(-inf)
 5 proc:     Right = 2^(0.000000)
 6 proc:     Right = 2^(-inf)
 7 proc:     Right = 2^(-inf)

                              Total queries = 2^(35.000000)
CRAFT:     Number of total right quadruples = 2^(1.000000)
           Probability of right quadruples  = 2^(-34.0000)
 time on clock(): 12063.5

[+] Time : 12053.677600
[+] CRAFT:         Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 1
[+] PRNG initialized to 0xD1A66395
[+] Time : 12048.608903
[+] CRAFT:         Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 7
[+] PRNG initialized to 0xD1A6639B
[+] Time : 12057.809894
[+] CRAFT:         Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 2
[+] PRNG initialized to 0xD1A66396
[+] Time : 12048.206285
[+] CRAFT:         Number of right quadruples = 2^(0.000000)
[+]           Probability of right quadruples = 2^(-32.0000)


[+] Proc 6
[+] PRNG initialized to 0xD1A6639A
[+] Time : 12047.656034
[+] CRAFT:         Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 3
[+] PRNG initialized to 0xD1A66397
[+] Time : 12062.896487
[+] CRAFT:         Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 5
[+] PRNG initialized to 0xD1A66399
[+] Time : 12039.559938
[+] CRAFT:         Number of right quadruples = 2^(0.000000)
[+]           Probability of right quadruples = 2^(-32.0000)


[+] Proc 4
[+] PRNG initialized to 0xD1A66398
[+] Time : 12063.532009
[+] CRAFT:         Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)
```

[LBlock] folder contains the verification codes to verify the quadruple distinguishers we found. To run the programm, MPI package need to be installed and change the library path and include path in Makefile according to your installation. Run `mingw32-make` (in Windows) to compile the C++ codes. 

To test 9-round by running on 8 processors, run

```sh
mpiexec -n 8 LBlock_Quadruple_MPI_RNG 9
```
You get a summary of number of quaries and number of right quadruples on each process, total queries, number of total right quadruples and the probability. For comparison we use full round LBlock as random permutation. 

```
[+] Proc 0
[+] PRNG initialized to 0xD1ABECBA

 Quaries on each process = 2^(16.000000)
 0 proc:     Right = 2^(8.076816)
 0 proc: randRight = 2^(1.000000)
 1 proc:     Right = 2^(8.055282)
 1 proc: randRight = 2^(0.000000)
 2 proc:     Right = 2^(8.066089)
 2 proc: randRight = 2^(0.000000)
 3 proc:     Right = 2^(8.154818)
 3 proc: randRight = 2^(0.000000)
 4 proc:     Right = 2^(8.108524)
 4 proc: randRight = 2^(-inf)
 5 proc:     Right = 2^(8.038919)
 5 proc: randRight = 2^(-inf)
 6 proc:     Right = 2^(8.154818)
 6 proc: randRight = 2^(0.000000)
 7 proc:     Right = 2^(7.894818)
 7 proc: randRight = 2^(-inf)

                              Total queries = 2^(19.000000)
LBlock:    Number of total right quadruples = 2^(11.070792)
           Probability of right quadruples  = 2^(-7.9292)
 RandPerm: Number of total right quadruples = 2^(2.584963)
            Probability of right quadruples = 2^(-16.4150)
 time on clock(): 0.231

[+] Time : 0.222836
[+] LBlock:        Number of right quadruples = 2^(8.076816)
[+]           Probability of right quadruples = 2^(-7.9232)

[+] RandPerm:      Number of right quadruples = 2^(1.000000)
[+]           Probability of right quadruples = 2^(-15.0000)


[+] Proc 7
[+] PRNG initialized to 0xD1ABECC1
[+] Time : 0.221787
[+] LBlock:        Number of right quadruples = 2^(7.894818)
[+]           Probability of right quadruples = 2^(-8.1052)

[+] RandPerm:      Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 6
[+] PRNG initialized to 0xD1ABECC0
[+] Time : 0.228040
[+] LBlock:        Number of right quadruples = 2^(8.154818)
[+]           Probability of right quadruples = 2^(-7.8452)

[+] RandPerm:      Number of right quadruples = 2^(0.000000)
[+]           Probability of right quadruples = 2^(-16.0000)


[+] Proc 2
[+] PRNG initialized to 0xD1ABECBC
[+] Time : 0.228351
[+] LBlock:        Number of right quadruples = 2^(8.066089)
[+]           Probability of right quadruples = 2^(-7.9339)

[+] RandPerm:      Number of right quadruples = 2^(0.000000)
[+]           Probability of right quadruples = 2^(-16.0000)


[+] Proc 3
[+] PRNG initialized to 0xD1ABECBD
[+] Time : 0.227331
[+] LBlock:        Number of right quadruples = 2^(8.154818)
[+]           Probability of right quadruples = 2^(-7.8452)

[+] RandPerm:      Number of right quadruples = 2^(0.000000)
[+]           Probability of right quadruples = 2^(-16.0000)


[+] Proc 5
[+] PRNG initialized to 0xD1ABECBF
[+] Time : 0.227326
[+] LBlock:        Number of right quadruples = 2^(8.038919)
[+]           Probability of right quadruples = 2^(-7.9611)

[+] RandPerm:      Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)


[+] Proc 1
[+] PRNG initialized to 0xD1ABECBB
[+] Time : 0.218853
[+] LBlock:        Number of right quadruples = 2^(8.055282)
[+]           Probability of right quadruples = 2^(-7.9447)

[+] RandPerm:      Number of right quadruples = 2^(0.000000)
[+]           Probability of right quadruples = 2^(-16.0000)


[+] Proc 4
[+] PRNG initialized to 0xD1ABECBE
[+] Time : 0.216918
[+] LBlock:        Number of right quadruples = 2^(8.108524)
[+]           Probability of right quadruples = 2^(-7.8915)

[+] RandPerm:      Number of right quadruples = 2^(-inf)
[+]           Probability of right quadruples = 2^(-inf)
```
