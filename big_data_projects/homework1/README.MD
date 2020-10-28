# Big Data Programming
## Lab 1 report  

#### Authors: Modupe Lekena, Suzanne Zhen, Dylan Smith

### Details:
This source implements both questions 1 and 2 from the first lab assignment. Starting from the logstat2 solution,
we have modified the mapper to optionally filter input based on user parameters and we have modified reducer 
to sort results and return the top three ip address for per hour.

### How 2 run:
- to run, call `./test.sh`
- interface: ` test.sh [{0..9}-{0..9}]` - example `./test.sh 1-5`
- question 1 results are produced when run without parameters passed
- question 2 results are produced by passing a hour range via the input parameters.
