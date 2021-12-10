# AlgoExpert
Here are my submitted codes on AlgoExpert and an executor to test the solutions.

There are two kind of entrypoint to run test.
1. run.py _(depreciated)_
2. go.py


### Usage:
```shell
$ python go.py -q [question_path]
```
An example to test `heightBalancedBinaryTree` under `binary_trees` category.
```shell
$ python go.py -q binary_trees/heightBalancedBinaryTree.py

Question 1:
Test result: Pass!
---------------------------------------------------------------------------------------
Question 2:
Test result: Pass!
---------------------------------------------------------------------------------------
> 0.7116794586181641 ms
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
