# Python Logger Guide

## Overview
The `logging` module is Python's standard library for recording events during program execution. It's more powerful and flexible than simple `print()` statements.

## Why Use Logging Instead of Print?

1. **Configurability** - Adjust log levels, formats, and destinations without changing code. Turn debugging on/off easily.

2. **Multiple outputs** - Simultaneously log to console, files, email, HTTP endpoints, etc. `print()` only goes to stdout.

3. **Log levels** - Categorize messages by severity (DEBUG, INFO, WARNING, ERROR, CRITICAL) for filtering. `print()` treats everything the same.

4. **Structured output** - Add timestamps, function names, line numbers, process IDs automatically. `print()` requires manual formatting.

5. **Production ready** - Features like log rotation prevent disk space issues. Built-in hierarchy for organizing logs by module.

6. **Performance** - Lazy evaluation means expensive formatting only happens if the log level is enabled. `print()` always executes.

7. **Disable easily** - Turn off debugging logs in production with a config change, not code edits. `print()` requires removing/commenting lines.

8. **Control across modules** - Set logging configuration once at startup; all imported modules respect it automatically.

In short: `logging` is designed for real applications where you need flexibility, organization, and control. `print()` is for quick debugging and temporary output.

## Basic Setup

### Simple Configuration
```python
import logging

# basicConfig() sets up the root logger with default settings
# It configures how all logging messages will be displayed
logging.basicConfig(
    # level=logging.DEBUG means show ALL messages (DEBUG and above)
    # If we used logging.WARNING, we'd only see WARNING, ERROR, CRITICAL
    level=logging.DEBUG,
    
    # format defines how each log message appears
    # %(asctime)s    = timestamp when the message was logged
    # %(name)s       = name of the logger (module name)
    # %(levelname)s  = severity level (DEBUG, INFO, ERROR, etc.)
    # %(message)s    = the actual message you provided
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Now any logging calls will follow the configuration above
logging.debug("Debug message")      # Shows: 2026-01-17 10:45:23,123 - root - DEBUG - Debug message
logging.info("Info message")        # Shows: 2026-01-17 10:45:23,124 - root - INFO - Info message
logging.warning("Warning message")  # Shows: 2026-01-17 10:45:23,125 - root - WARNING - Warning message
logging.error("Error message")      # Shows: 2026-01-17 10:45:23,126 - root - ERROR - Error message
logging.critical("Critical message")# Shows: 2026-01-17 10:45:23,127 - root - CRITICAL - Critical message
```

## Log Levels
| Level | Value | Use Case |
|-------|-------|----------|
| DEBUG | 10 | Detailed info for debugging |
| INFO | 20 | Confirmation things are working |
| WARNING | 30 | Something unexpected (default) |
| ERROR | 40 | Serious problem |
| CRITICAL | 50 | Very serious problem |

## Format Directives
Common placeholders in format strings:
- `%(asctime)s` - Timestamp
- `%(name)s` - Logger name
- `%(levelname)s` - Log level (DEBUG, INFO, etc.)
- `%(message)s` - Log message
- `%(filename)s` - Source filename
- `%(funcName)s` - Function name
- `%(lineno)d` - Source line number
- `%(pathname)s` - Full path of source file
- `%(process)d` - Process ID
- `%(thread)d` - Thread ID

## Logger Objects

### Creating a Logger
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
fh = logging.FileHandler('app.log')
fh.setLevel(logging.ERROR)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.error("This is an error message")
```

## Handlers
Handlers send log records to different destinations:
- `StreamHandler()` - Console output
- `FileHandler(filename)` - Write to file
- `RotatingFileHandler(filename, maxBytes, backupCount)` - Rotate logs by size
- `TimedRotatingFileHandler(filename, when, interval)` - Rotate logs by time
- `SMTPHandler` - Send logs via email
- `HTTPHandler` - Send logs via HTTP

## Formatters
Create custom formats for your logs:
```python
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```

## Rotating Logs

### By Size
```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1 MB
    backupCount=5
)
```

### By Time
```python
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',  # 'S', 'M', 'H', 'D', 'midnight', etc.
    interval=1,
    backupCount=7
)
```

## Configuration from Dictionary

```python
import logging.config

config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)
```

## Configuration from YAML

```python
import logging.config
import yaml

with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
```

`logging_config.yaml`:
```yaml
version: 1
disable_existing_loggers: false

formatters:
  standard:
    format: '%(asctime)s [%(levelname)s] %(name)s: %(message)s'

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: standard
    stream: ext://sys.stdout

  file:
    class: logging.FileHandler
    level: DEBUG
    formatter: standard
    filename: app.log

root:
  level: DEBUG
  handlers: [console, file]
```

## Logging in Different Modules

```python
# module_a.py
import logging
logger = logging.getLogger(__name__)

def do_something():
    logger.debug(f"Doing something in {__name__}")
```

```python
# main.py
import logging
import module_a

logging.basicConfig(level=logging.DEBUG)
module_a.do_something()
```

## Exception Logging

```python
import logging

logger = logging.getLogger(__name__)

try:
    1 / 0
except ZeroDivisionError:
    # Log with full traceback
    logger.exception("An error occurred")
    
    # Or without the exception context
    logger.error("An error occurred", exc_info=True)
```

## Filtering

```python
import logging

class MyFilter(logging.Filter):
    def filter(self, record):
        # Return True to log the record, False to skip it
        return 'sensitive' not in record.getMessage()

logger = logging.getLogger(__name__)
my_filter = MyFilter()
logger.addFilter(my_filter)

logger.info("This is normal")  # Logged
logger.info("This contains sensitive data")  # Not logged
```

## Best Practices
1. Use `__name__` when creating loggers to organize by module
2. Use appropriate log levels for different events
3. Use string formatting (f-strings or %) instead of concatenation for performance
4. Configure logging early in your application
5. Don't log sensitive information (passwords, tokens, PII)
6. Use structured logging for better parsing in production
7. Consider log rotation to manage file sizes
8. Use context managers for transaction logging

## Common Pattern - Production Setup

```python
import logging
import logging.handlers
import os

def setup_logging(log_file='app.log', level=logging.INFO):
    """Setup logging configuration."""
    logger = logging.getLogger()
    logger.setLevel(level)
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=10
    )
    file_handler.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Usage
logger = setup_logging()
logger.info("Application started")
```
