# tree-structure

### Folder structure
- The project consist of two parts `src` which contains source code.
`tests` includes execution of source code.
- In the `src` directory, there is a `traverse` folder that each module logic source code is here.  
- Also, `traverse` has 4 `.py` files that are `base.py`, `breadth-first.py`, `deep_first.py` and `zigzag.py`
- There is no dependency package in this project. Therefore no need any `requirements.in` or `requirements.txt`.

### Design Pattern
- In the `traverse`, `base.py` is a `Abstract Base Class`. 
- According to base class structure, other traverse logics is implemented same structure. 
- Thanks to `Abstract Pattern`, isolation of concrete class provides control the classes of object that an application crates.

### Test Case
- In order to test each application module.
- In terminal, you should run these commands seperately:  
  `python3 tests/test_breadth_first.py`
  `python3 tests/test_deep_first.py`
  `python3 tests/test_zigzag.py`


### Module Logics
- As you see the diagrams that is below, represents the logic of `breadth-first.py`, `deep_first.py` and `zigzag.py`. Each one implements its own logic.

#### Deep-First Diagram

![deep-first](https://github.com/zeki-kadiroglu/tree-structure/blob/main/diagrams/deep-first.png)

- The diagram above displays each step of `deep-first search`, it respectively follows this order: `Root 3 4 5 10 2 6 9 11 12 7 8 1`

#### Breadth-First Diagram
![breadth-first](https://github.com/zeki-kadiroglu/tree-structure/blob/main/diagrams/breadth-first.png)

- The diagram above displays each step of `breadth-first search`, it respectively follows this order: `Root 3 2 1 4 5 10 6 7 8 9 11 12`

#### ZigZag Diagram
![zigzag diagram](https://github.com/zeki-kadiroglu/tree-structure/blob/main/diagrams/zigzag.png)

- The diagram above displays each step of `zigzag search`, it respectively follows this order: `Root 1 3 2 4 5 10 6 7 8 9 11 12`


