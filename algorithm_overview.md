Let our input graph be G. The gist is this:
- Create the following subroutine:
- Produce a spanning tree of G in some way, and call it T.
- Repeatedly remove the largest possible edge in T such that the rest of T still
dominates G and its average pairwise distance decreases. Return T when there are
no more edges whose removal satisfies this criteria.
- Repeat the above process for many different spanning trees of G and take the lowest-cost T
over all of them. Currently, my algorithm uses the MST of G as well as the shortest-paths tree and
BFS tree for each vertex in G.

---

Originally, I wanted to add edges one by one until I had a dominating tree, trying to minimize
the average pairwise distance of connected components along the way. In my naive program, the
algorithm terminated as soon as I had a single connected dominating set. The problem is, the cost of
the subtrees of a dominating tree do not necessarily reflect how optimal the entire dominating tree is.
It’s typical that adding a particular edge seems optimal in the short term but forces costly edge
additions in the long term. Even though I made smaller optimizations, I never found a satisfying way
to connect individual components into a dominating tree while being cost-conscious. If I did, I might
have devoted more time to this method, but I found an alternative that seemed to be more efficient.
I decided to focus on ensuring that I had a dominating tree at every intermediate step in my
algorithm, and then worry about cost. Since any dominating tree is a subtree of a spanning tree,
trimming a spanning tree is a fairly obvious and easy way to guarantee that my output is always
valid. From here, I decided to decide the removal order of edges based on their weights---heavy
edges are the most likely to increase average pairwise distance. At any point, the only removable
edges are the ones incident to leaves. All of this is handled by a priority queue that adds new leaves
and their associated edge weights as the algorithm progresses.
The whole point of this---that is, the key upside of this approach---is that I don’t need to worry
about dominating trees anymore: I can just come up with a decent spanning tree, and my algorithm
will probably make a relatively low-cost dominating tree out of it. The current version of my algorithm
is pretty basic, using shortest-paths trees, BFS trees, and the MST (well, one of them at any rate).
Those have certain characteristics that I figured would lead to a lower average pairwise distance,
such as minimal distance from one source to all other vertices, minimal number of edges from one
source to all other vertices, and minimal total weight of edges. With more time I could generate
random spanning trees--the rest of my algorithm works the exact same way.
My approach is simple to implement and pretty fast---it produces an output for each of the
large input graphs in around 1 minute or less on my laptop. More importantly, it’s easy to make
changes because coming up with new ways to produce spanning trees is much easier than working
with dominating trees. Originally, I only used the BFS trees; adding shortest-paths trees and MST
came later. The improvement in performance was significant and yet it consisted of 2 additional list
comprehensions in one preexisting line of code.
