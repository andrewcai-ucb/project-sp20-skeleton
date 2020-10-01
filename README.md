FOR EMPLOYERS:

In this project, our task was to find solutions to the NP-hard telecommunications problem, with vertices representing cities that we need to communicate efficiently. From the spec: 

Formally, let G = (V,E) be a positive weighted, connected, undirected graph. We would like to find a subgraph T of
G such that:
1. Every vertex v ∈ V is either in T or adjacent to a vertex in T.
2. T is a tree.
3. The average pairwise distance between all vertices in T is minimized. 
*In particular, we were graded based on how well we generally minimized this quantity over a large number of distinct small, medium, and large graphs relative to other students' submissions. Although teams were allowed, I was one of the top 20 teams as a solo student.

------------

# CS 170 Project Spring 2020

Take a look at the project spec before you get started!

Requirements:

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
  - These are the functions run by the autograder to validate submissions

------------

Instructions: 

Simply run python max_st.py once---as of this submission my algorithm is purely deterministic.
