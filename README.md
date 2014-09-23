the-log-book
============
algorithms associated with logarithms
============

In early September 2014 Bernie J asked me to write up an algorithm for computing
logarithms that I had told him about in conversation some years ago.
I was learning Python, so I decided it would be a good exercise.
I wrote up a loopy something with a bunch of while and /=, and -=, and so forth.
I came across a discussion of Haskell and functional programming, with quicksort
given as an example.
I thought, I know all about this; that is how I usually program, in Mathematica.
I went back to the algorithm.
One thing that had bothered me was the apparent discontinuity between getting
the mantissa and getting the fractional part of the log.
Maybe the functional style would clarify that.
I think it did that and more.

The entry updnLog is the result. It may need a short article explaining why it
works beyond the comments in the script. I had to really think about what the
loopy algorithm was doing.

As a check on the clarity of the algorithm, I made a tiny number of changes
(mainly / -> - and 1 -> 0) to turn it into a dividing algorithm,
updnDiv, which is much like long division. After all, it was the analogy
   "division is to subtraction as taking logarithm is to division"
that I think was part of the original idea of the logarithm algorithm.

The updnLog script seems to indeed cut the idea down to its essence;
resolves the seeming discontinuity;
visibly uses basic logarithm properties;
and makes clear the above analogy (you could call it the long logarithm
algorithm).

I also learned while doing all this that this algorithm with base 2, the binary
logarithm, is well-known; it is on wikipedia.
Though I have not seen it in the economical form of updnLog.

I wonder what the built-in log and power functions of standard programming
languages use as their main logarithm.
I always assumed it was the natural logarithm, using series constructions.
But it now seems plausible that the binary logarithm could beat that for time.

It is interesting to me, too, that the existence of such non-natural logarithm
algorithms says we don't absolutely need the natural logarithm.