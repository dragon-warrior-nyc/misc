# TQDM Demo Project

A comprehensive demonstration of [tqdm](https://github.com/tqdm/tqdm) - a fast, extensible progress bar library for Python.

## What is tqdm?

tqdm (from Arabic *taqaddum* تقدّم meaning "progress") is a library that provides smart progress meters for Python. It lets you wrap any iterable with a progress bar, showing a visual indicator of your loop's progress.

### Key Features

- 🚀 **Simple to use**: Just wrap any iterable with `tqdm()`
- ⚡ **Fast**: Minimal overhead
- 🎨 **Customizable**: Tons of options for appearance and behavior
- 📊 **Smart**: Automatically estimates time remaining
- 🔧 **Versatile**: Works with loops, downloads, file processing, and more

## Prerequisites

Python 3.11 or higher and uv installed:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

## Quick Start

### 1. Clone or create the project directory

```bash
cd tqdm_demo
```

### 2. Create and activate virtual environment

```bash
# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Run the demos

```bash
# Interactive menu to choose demos
python run_demos.py

# Or run specific demo files directly
python -m tqdm_demo.basic_demo
python -m tqdm_demo.advanced_demo
```

## Demo Overview

### Basic Demos (`basic_demo.py`)

1. **Simple Progress Bar** - Basic loop with progress indicator
2. **Dynamic Description** - Progress bar with changing descriptions
3. **Manual Updates** - Manually control progress updates
4. **Nested Progress Bars** - Multiple progress bars for nested loops

### Advanced Demos (`advanced_demo.py`)

1. **File Processing** - Simulate processing multiple files with custom units
2. **Download Simulation** - Progress bar with byte units (MB, GB, etc.)
3. **Custom Format** - Customize the progress bar appearance
4. **Dynamic Stats** - Show live statistics (loss, accuracy) during processing

## Common Use Cases

### Basic Loop
```python
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.01)
```

### File Processing
```python
from tqdm import tqdm

files = ['file1.txt', 'file2.txt', 'file3.txt']
for filename in tqdm(files, desc="Processing"):
    process_file(filename)
```

### Manual Control
```python
from tqdm import tqdm

with tqdm(total=100) as pbar:
    while work_to_do:
        do_work()
        pbar.update(10)  # Update by 10 units
```

### Download with Byte Units
```python
from tqdm import tqdm

with tqdm(total=file_size, unit='B', unit_scale=True, 
          unit_divisor=1024) as pbar:
    for chunk in download_chunks():
        pbar.update(len(chunk))
```

## tqdm Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `desc` | Description prefix | `desc="Downloading"` |
| `total` | Total iterations expected | `total=100` |
| `unit` | String for iteration units | `unit='file'` |
| `unit_scale` | Auto-scale units (K, M, G) | `unit_scale=True` |
| `leave` | Keep bar after completion | `leave=False` |
| `bar_format` | Custom bar format | See docs |
| `postfix` | Dict of stats to display | `postfix={'loss': 0.5}` |

## Tips & Tricks

1. **Disable progress bar**: Set `disable=True` for production or set environment variable `export TQDM_DISABLE=1`

2. **Write messages without breaking the bar**: Use `tqdm.write()` instead of `print()`

3. **Get current rate**: Access `pbar.format_dict['rate']`

4. **Use with list comprehensions**:
   ```python
   results = [process(x) for x in tqdm(items)]
   ```

5. **Pandas integration**:
   ```python
   from tqdm.auto import tqdm
   tqdm.pandas()
   df.progress_apply(lambda x: x**2)
   ```

## Project Structure

```
tqdm_demo/
├── pyproject.toml           # Project configuration
├── run_demos.py             # Interactive demo launcher
├── tqdm_demo/               # Package directory
│   ├── __init__.py          # Package initialization
│   ├── basic_demo.py        # Basic tqdm demonstrations
│   └── advanced_demo.py     # Advanced use cases
└── README.md                # This file
```

## Learn More

- [Official Documentation](https://tqdm.github.io/)
- [GitHub Repository](https://github.com/tqdm/tqdm)
- [PyPI Package](https://pypi.org/project/tqdm/)

## Why Use tqdm?

- **Better UX**: Users can see progress instead of staring at a blank screen
- **Debugging**: Identify slow iterations or bottlenecks
- **Professional**: Makes CLI tools look polished and modern
- **Minimal code**: Often just one line: `for item in tqdm(items):`

Enjoy exploring tqdm! 🚀
