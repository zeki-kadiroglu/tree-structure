# tree-structure

### Folder structure
- The project consist of two parts `src` which contains source code.
`tests` includes execution of source code.
- In the `src` directory, there is `traverse` folder that each module logic source code is here.  
- Also, in `traverse` has 4 `.py` files that are `base.py`, `breadth-first.py`, `deep_first.py` and `zigzag.py`
- There is no dependency package in this project. Therefore no need any `requirements.in` or `requirements.txt`.

### Design Pattern
- In the `traverse`, `base.py` is a `Abstract Base Class`. 
- According to base class structure, other traverse logics is implemented same structure. 
- Thanks `Abstract Pattern`, isolation of concrete class provides control the classes of object that an application crates.


### Module Logics
- As you see the diagrams that is below, represents the logic of `breadth-first.py`, `deep_first.py` and `zigzag.py`. Each one implements its own logic.

