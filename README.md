# otus_patterns_hw1
Homework 1: unit testing of quadratic equation solver
Language: Python

CI Status: [![build](https://github.com/mihsamusev/otus_patterns_hw1/actions/workflows/build.yaml/badge.svg)](https://github.com/mihsamusev/otus_patterns_hw1/actions/workflows/build.yaml)

## Tasks
Develop a quadratic equation solver using TDD method and test following functionality:
- No roots obtained solving: $x^2 + 1 = 0$
- Two different roots obtained solving: $x^2 - 1 = 0$
- Two identical roots obtained solving: $x^2 + 2 x + 1 = 0$
    - given discriminant is exactly zero
    - given discriminant is smaller than epsilon
- Divison by 0 due to $a = 0$ throws an error
- Types other than reals throw an error