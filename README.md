# Monopoles
<h2>John Lewis<br/>Portland State University<br/>CS441<br/>HW #1</h2>
<p>This program sorts <i><b>m</b></i> numbers (monopoles) into <i><b>n</b></i> sets (rooms) while
avoiding any triples in a given set such that for any <i><b>X,Y,Z, X+Y=Z</b></i></p>
<h3>To Run: [python | python3] monodfs.py m n</h3>
<h2>Homework Description</h2>
<h3>Monopoles: Problem Statement</h3>

Given: n rooms. A set 1..m of monopoles to place.

Find: A list S of n sets with the following properties:

<ol>
  <li>Each monopole is placed:</li> 
  <pre>union S = {1..m}</pre>
  <li>No monopole is in two places:</li>
  <pre>forall i in {1..m}
    exists unique j in {1..n} .
        i in S[j]</pre>
        
  <li>Sums exclude monopoles:</li>
  <pre>forall i in {1..n} .
   for all j, k in S[i] .
       j ≠ k and j in S[i] and k in S[i] → j + k not in S[i]</pre>
</ol>
<h2>Thought Process</h2>
<p>The first attempt at this was a depth first search implementation with limited use of the needed
  <br/>heuristics to "prune" possible branches. Further heuristics will allow the program to solve
  <br/>four room solutions that currently take large resources.
<br/><br/>
The program screens the input to make sure the monopoles are greater than or equal to the number of
rooms and tells the user the solution is trivial if they are equal.
<br/><br/>
Since adding 1 to any room leads to all the same results ({{1}{}} == {{0}{1}}), a 1 is added to room 1 which cuts the
possible branches in half from the start for 2 rooms. I realized that this saves a lot on 2 rooms
but doesn't continue to buy as much with the addition of more rooms since 2 could go in any of the
new rooms except the room with a 1 with no difference in results ({{1}{2}{0} == {1}{0}{2}). Unfortunately I struggled enough
just implementing the depth first search successfully that I wasn't able to get to using this
powerful heuristic
<br/><br/>
From here the program simply tries inserting the numbers that are allowed (not X+Y=Z) and "undoing" an add if it lead to a
dead end. Only one copy of the "rooms" list is kept in memory and the recursion basically increments and decrements the 
monopole integer being added. Using this "do-undo" method saves on the memory use in this full dfs implementation.
<br/><br/>
This implementation also goes through the entire DFS instead of stopping at the first so the captured solution is the last
one found, not the first solution.</p>
<h3>This program successfully finds the solution to 23 3 = sat, 24 3 = unsat cases in under a second but takes longer than
  I cared to wait on 4 room cases greater than 15.</h3>
