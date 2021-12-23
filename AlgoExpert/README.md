# AlgoExpert
Here are my submitted codes on AlgoExpert and an executor to test the solutions.

There are two kind of entrypoint to run test.
1. run.py _(depreciated)_
2. go.py

### Prerequisite
```shell
$ pip install -r requirements.txt
```


### Usage:
```shell
$ python go.py -q [question_path]
```
An example to test `heightBalancedBinaryTree` under `binary_trees` category.
```shell
$ python go.py -q binary_trees/heightBalancedBinaryTree.py

Checker mode: default
Question 1:
Test result: Pass!
Time Costs: 0.0 ms
---------------------------------------------------------------------------------------
Question 2:
Test result: Pass!
Time Costs: 0.0 ms
---------------------------------------------------------------------------------------
Examine Report:
> all pass: True
> failed index: []
> total time costs: 0.0 ms
> avg. time costs: 0.0 ms
> profiling memory usage with the last test case...
Filename: D:\repo\Leetcode\AlgoExpert\binary_trees\heightBalancedBinaryTree.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    91     41.3 MiB     41.3 MiB           1   def heightBalancedBinaryTree(tree):
    92     41.3 MiB      0.0 MiB           1       is_balanced, depth = find_depth(tree)
    93     41.3 MiB      0.0 MiB           1       return is_balanced
```


### Usage:
```shell
$ python run.py -c CATEGORY -q QUESTION -s [SOLUTION ...]
```
An example to test `array.nonConstrutibleChange` solutions:
```shell
$ python run.py -c array -q nonConstructibleChange -s 1 2

Timing solution: 1:
> 1.2600421905517578 ms
Timing solution: 2:
> 0.4138946533203125 ms
```
