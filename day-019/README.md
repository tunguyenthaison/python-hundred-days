# python-hundred-days

## Day 019: Instance, State and Higher Order functions

---
- Functions as inputs $\to$ only pass the name of the function!

```python
    def function_a(something):
        # do this with something
        # then do this
        # finally do this
    
    def function_b():
        # do this

    function_a(function_b)
```

