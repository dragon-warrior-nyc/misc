# Python Debugger (pdb) Guide

## Overview
`pdb` is Python's built-in interactive debugger. It allows you to step through code, set breakpoints, inspect variables, and evaluate expressions at runtime.

## Starting the Debugger

### Method 1: Direct Entry Point
```python
import pdb

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    pdb.set_trace()  # Debugger pauses here
    average = total / len(numbers)  # Inspect 'total' and 'average' here
    return average

# Run this and interact with debugger
result = calculate_average([10, 20, 30])
```

When execution reaches the line with `pdb.set_trace()`, you get an interactive prompt:
```
> /path/to/script.py(9)calculate_average()
-> average = total / len(numbers)
(Pdb) p total          # Print total variable (p = print command)
60
(Pdb) total            # Can also just type the variable name directly
60
(Pdb) p len(numbers)   # Check list length
3
(Pdb) p average        # Variable doesn't exist yet
*** NameError: name 'average' is not defined
(Pdb) n                # 'n' = next: Execute current line, stay in debugger at next line
> /path/to/script.py(10)calculate_average()
-> return average
(Pdb) p average        # Now it exists
20.0
(Pdb) c                # 'c' = continue: Resume execution until next breakpoint or end (exits debugger)
```

### Method 2: Post-Mortem Debugging
```python
import pdb
import traceback
try:
    # Your code here
    risky_function()
except Exception as e:
    traceback.print_exc()
    pdb.post_mortem()
```
Debug after an exception occurs.

### Method 3: Command Line
```bash
python -m pdb your_script.py
```
Start the debugger immediately when running your script.

### Method 4: Breakpoint (Python 3.7+)
```python
breakpoint()
```
More concise alternative to `pdb.set_trace()`.

## Essential Commands

| Command | Short | Description |
|---------|-------|-------------|
| `help` | `h` | List all commands or help for a specific command |
| `list` | `l` | Show current code lines |
| `next` | `n` | Execute current line, move to next line in current function |
| `step` | `s` | Step into function calls |
| `continue` | `c` | Resume execution until next breakpoint |
| `break` | `b` | Set a breakpoint |
| `breakpoints` | | Show all breakpoints |
| `clear` | | Remove breakpoints |
| `print` | `p` | Print a variable value |
| `pp` | | Pretty-print a variable |
| `where` | `w` | Show stack trace |
| `up` | `u` | Move up one stack frame |
| `down` | `d` | Move down one stack frame |
| `return` | `r` | Execute until function returns |
| `jump` | `j` | Jump to another line (in same function) |
| `interact` | | Start an interactive Python shell |
| `quit` / `exit` | `q` | Exit the debugger |

## Setting Breakpoints

### Unconditional Breakpoint
```python
import pdb

def calculate(x, y):
    pdb.set_trace()  # Stops here every time
    return x + y
```

### Breakpoint by Line Number
In the debugger:
```
(Pdb) break 42          # Break at line 42 of current file
(Pdb) break file.py:10  # Break at line 10 of file.py
(Pdb) break func_name   # Break at first line of function
```

### Conditional Breakpoint
```
(Pdb) break 42, x > 10  # Break at line 42 only if x > 10
```

## Inspecting Variables

```
(Pdb) print x              # Print variable x
(Pdb) p locals()           # Print all local variables
(Pdb) p globals()          # Print all global variables
(Pdb) pp my_dict           # Pretty-print dictionary
(Pdb) print type(variable) # Check variable type
(Pdb) print len(my_list)   # Check length
```

## Navigating Code

### Examine Code
```
(Pdb) list           # Show 11 lines around current location
(Pdb) list 20,30     # Show lines 20-30
(Pdb) list file.py   # Show code in different file
```

### Stack Navigation
```
(Pdb) where          # Show full stack trace
(Pdb) up             # Go to caller's frame (up stack)
(Pdb) down           # Go to called function (down stack)
(Pdb) frame N        # Jump to frame N
```

## Execution Control

```
(Pdb) step          # Step into functions (go deeper)
(Pdb) next          # Step over functions (stay at same level)
(Pdb) continue      # Resume until breakpoint or end
(Pdb) return        # Execute until current function returns
(Pdb) jump 45       # Jump to line 45 (same function only)
```

## Practical Debugging Workflow

### Finding a Bug in a Loop
```python
# my_script.py
data = [1, 2, 3, 4, 5]
result = 0

for i, val in enumerate(data):
    breakpoint()  # Stop at each iteration
    result += val
    print(f"Iteration {i}: result = {result}")
```

### Debugging Function Parameters
```python
def process(name, count):
    breakpoint()  # Inspect what was passed
    for i in range(count):
        print(f"{name}: {i}")

process("Test", 3)
```

Then use `p name` and `p count` to inspect arguments.

### Conditional Debugging
```python
# Only debug when condition is true
def analyze_data(data):
    if len(data) > 100:
        breakpoint()  # Only stop for large datasets
    return sum(data)
```

## Useful Tricks

### Execute Python Expressions
```
(Pdb) print [x*2 for x in range(10)]
(Pdb) print sum([1, 2, 3, 4])
(Pdb) x = 42  # Set variable value
```

### Interactive Shell Within Debugger
```
(Pdb) interact
# Now you have full Python REPL access
>>> import numpy as np
>>> arr = np.array([1, 2, 3])
>>> exit()  # Back to pdb
(Pdb)
```

### Create Alias for Repeated Commands
```
(Pdb) alias ll list %:; list   # Create alias 'll' for repeated lists
(Pdb) ll                        # Execute it
```

### Disable/Enable Breakpoints
```
(Pdb) breakpoints             # List all breakpoints with IDs
(Pdb) disable 1               # Disable breakpoint 1
(Pdb) enable 1                # Re-enable breakpoint 1
(Pdb) clear 1                 # Delete breakpoint 1
```

## Tips & Best Practices

1. **Use breakpoint() over pdb.set_trace()** - More modern and concise (Python 3.7+)
2. **Remove debugger statements before committing** - Use `git grep` to find them
3. **Combine with logging** - Not every problem needs step-by-step debugging
4. **Use pp() for complex objects** - Much more readable than print()
5. **Use where** first when entering an exception - Understand the call stack
6. **Step into library code selectively** - Use `next` to skip implementation details
7. **Check locals() and globals()** - Quick overview of variable state
8. **Test the fix before exiting** - Try your fix in the interactive shell with `interact`

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| Breakpoint never hit | Check file path, line numbers, and conditions |
| Can't modify variables | Use assignment: `(Pdb) x = new_value` |
| Too much output | Use `pp()` instead of `print()` for formatting |
| Lost in frames | Use `where` to see stack, then `up`/`down` |
| Want to exit quickly | Press `q` then `Enter` |

## Resources
- [Official pdb Documentation](https://docs.python.org/3/library/pdb.html)
- [pdb Commands Reference](https://docs.python.org/3/library/pdb.html#debugger-commands)
