As a Cold War spy, you managed to get your hands onto several hidden communication wires of your foe! Now, you must decide on which of these wires you must tap into, since you know that some of them are inactive.

In your last operation, you were able to recover a map of the enemy communication network. The network consists of stations and wires in between these stations. You know that each of the wires have been tagged with a unique threat level, and active lines are selected as the following.

Every pair of stations must be connected with some path of active wires.
The total of the threat levels of the active wires must be minimum.
You have decided that tapping into inactive wires is too much of a risk. Hence, you must decide whether if the wires you have found are active, and you must do it fast, before you are spotted!



On the first line, three integers a, b, c

a: total number of stations
b:total number of wires
c: total number of wires you have found

On the next m lines, three integers x, y, z

x,y: the stations between which the wire runs
z: the threat level of this wire

On the next f lines, two integers
the stations between which the wire you have uncovered runs.
Note that all wires have a unique threat level, and the network is simple and connected. The uncovered wires will be wires that are present in the network.

Output Format

On "yes" or "no" on each  line, signifying whether if you must select the given wire. The order of output must be same with the order in which the uncovered wires are given.

Sample Input

4 4 2

0 1 1

1 2 3

2 3 100

3 0 24

0 3

3 2

Sample Output

yes

no

Explanation

In this network of four stations and four wires, the only inactive wire is the one running between the stations  2 and 3.