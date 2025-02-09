# Symbolic Regression with Genetic Programming

## Collaboration

This project was developed with my colleague [fedspi00](https://github.com/fedspi00). Together, we designed and implemented the symbolic regression framework, applying genetic programming techniques to generate mathematical formulas, used to solve several problems.

## Overview

This project implements a symbolic regression framework using genetic programming (GP), an evolutionary computation technique that generates and optimizes mathematical formulas by means of a tree-based structure. The goal of this project is to develop a system that can approximate a given dataset through evolved symbolic expressions, refining them over multiple generations using selection, different types of mutation, recombination, and migration techniques.

## Features and Methodology

This project is designed around a tree-based representation of each mathematical formula, where nodes represent operators, variables, and constants. A genetic programming framework is used to evolve these expressions over generations, improving their ability (fitness) to approximate the dataset through iterative refinements. In addition, to enhance diversity and prevent premature convergence, the algorithm employs an island model, where the population is divided into multiple subpopulations (islands) that evolve independently. Periodically, a migration mechanism allows individuals to move between islands, promoting genetic exchange and preventing premature convergence. This strategy enhances exploration while maintaining computational efficiency. The key features used by the genetic programming in this project are:

- **Tree-based Representation**: Each formula is represented as a tree. Nodes represent operators, variables, and constants. Internal nodes represent mathematical operators (binary and unary operations) while leaves represent input variables and constants.
- **Train-Test Split**: The dataset is split into training and testing sets. The model is trained on the training set and evaluated on the test set to check its generalization.
- **Island Model**: The population is divided into subpopulations (islands) that evolve independently, increasing genetic diversity.
- **Migration Mechanism**: Individuals are periodically transferred between islands to exchange beneficial traits.
- **Mutation Mechanisms**: The structure of individuals is altered to introduce diversity. This includes:
  - **Subtree Replacement**: A subtree is replaced with another randomly generated subtree.
  - **Point Mutation**: A single node in the tree is replaced with a new random node.
  - **Permutation**: The order of the nodes is changed, altering the structure without changing the content.
  - **Hoisting**: A randomly selected subtree is moved to a higher level in the tree, replacing the root node.
  - **Collapsing**: A subtree is collapsed into a single node.
- **Recombination Operations**: Subtrees from different individuals are swapped to combine genetic traits.
- **Fitness Evaluation**: The fitness of each individual is evaluated using the Mean Squared Error (MSE) between the predicted and actual target values.

## Project Structure

The core of this project is built around a modular and extensible design. Key components include:

- **node.py**:

  - Implements the Node class, representing the essential element within an expression tree.
  - Supports binary operators, unary operators, variables, and constants.
  - Includes conversion to a human-readable string representation, which is also directly used in the fitness evaluation.

- **tree.py**:

  - Implements the Tree class, providing functionality for generating, evolving, and evaluating expression trees.
  - Includes methods for random tree generation to ensure diversity in the initial population.
  - Applies various mutation and crossover operations to refine expressions over generations.
  - Evaluates fitness using Mean Squared Error (MSE).

- **sym_reg_gp.ipynb**:

  - Serves as the main entry point of the program, running all symbolic regression tasks to evolve mathematical formulas.
  - Loads datasets and applies symbolic regression using the implemented genetic programming framework.
  - Visualizes results with two key plots: one showing the decrease in fitness (improvement) over generations, and another comparing model predictions to actual data.

## Final Results and Observations

The project successfully evolved symbolic expressions that closely matched the target functions across various test datasets. In many cases, the evolved expressions achieved low MSE, except for problem 2 and 8, indicating that the GP framework was effective in identifying complex mathematical relationships.

## Formulas from Problem 0 to 8

### Problem 0

```markdown
np.minimum(np.add(np.tanh(np.tanh(np.cosh(1.11997858020315))), np.add(np.negative(x[1]), np.add(np.square(0.6528258878453492), x[0]))), np.add(np.negative(np.remainder(np.negative(x[1]), np.multiply(1.7584125144807357, x[1]))), np.add(x[0], np.multiply(x[1], np.tanh(1.7319312973914491)))))
```

### Problem 1

```markdown
np.sin(x[0])
```

### Problem 2

```markdown
np.add(np.multiply(np.multiply(np.cosh(np.add(-2.6000121306461272, -3.2150906456657626)), np.multiply(np.add(x[2], x[2]), np.negative(x[0]))), np.multiply(x[1], np.subtract(np.exp(5.560625554341413), np.cosh(x[0])))), np.multiply(np.multiply(np.square(-4.943296862710281), x[0]), np.square(np.exp(5.369873197780641))))
```

### Problem 3

```markdown
np.add(np.multiply(np.multiply(-4.545991072645782, np.cos(-1.166098590091753)), np.subtract(np.add(x[2], np.exp(x[1])), np.absolute(np.cosh(x[1])))), np.add(np.subtract(np.negative(np.multiply(x[1], 2.055937107636824)), np.add(-4.804168082064881, x[2])), np.add(np.cosh(np.divide(x[0], -1.0814122259190357)), np.subtract(np.absolute(x[0]), np.remainder(x[1], -4.562096723325096)))))
```

### Problem 4

```markdown
np.add(np.add(np.add(np.sin(np.cos(x[1])), np.cos(np.minimum(x[1], x[1]))), np.add(np.cos(x[1]), np.cos(x[1]))), np.add(np.add(np.cos(np.subtract(x[1], 0.010079400223165003)), np.cos(x[1])), np.subtract(np.sinh(np.cos(x[1])), np.add(-3.8176015332518403, np.power(0.5905406461535465, 1.1707846494319254)))))
```

### Problem 5

```markdown
np.multiply(-6.027046665958086e-15, np.power(np.add(np.power(np.divide(x[0], 0.5130358016128974), np.arctan(5.079953468300546)), np.power(0.06510063674299789, np.cos(x[1]))), np.add(np.multiply(np.subtract(5.061849862519098, x[1]), 0.06510063674299789), x[1])))
```

### Problem 6

```markdown
np.add(np.add(x[1], np.maximum(np.subtract(x[1], 0.0715542326500378), np.negative(4.120292756672327))), np.negative(np.subtract(np.minimum(x[0], 4.155045641154721), np.arctan(np.subtract(x[0], x[1])))))
```

### Problem 7

```markdown
np.multiply(np.exp(np.sin(np.cosh(np.minimum(1.8537698499292565, x[1])))), np.power(np.exp(x[1]), np.add(np.tanh(np.maximum(-1.3819979974952137, x[0])), np.minimum(np.maximum(-0.3072630359351072, x[1]), np.maximum(-1.6618842110811194, x[0])))))
```

### Problem 8

```markdown
np.multiply(np.add(np.sinh(np.negative(x[5])), np.sinh(np.cbrt(np.square(x[4])))), np.add(np.multiply(np.multiply(-5.225190448882802, np.add(5.7514722132214136, -0.15288156941239528)), np.add(5.7514722132214136, np.cos(x[5]))), np.multiply(np.absolute(np.add(0.7098169053893928, x[5])), np.tan(np.log(5.393727864805511)))))
```
