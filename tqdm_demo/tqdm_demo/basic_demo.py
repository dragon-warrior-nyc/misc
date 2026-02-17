"""
Basic tqdm demonstrations showing various progress bar styles.
"""
import time
from tqdm import tqdm


def simple_loop():
    """Basic progress bar for a simple loop."""
    print("\n1. Simple Progress Bar")
    print("-" * 50)
    for i in tqdm(range(100), desc="Processing"):
        time.sleep(0.02)


def with_description():
    """Progress bar with dynamic description."""
    print("\n2. Progress Bar with Dynamic Description")
    print("-" * 50)
    for i in tqdm(range(50), desc="Loading"):
        time.sleep(0.03)
        if i == 25:
            tqdm.write("Halfway done!")


def manual_update():
    """Manually updating progress bar."""
    print("\n3. Manual Progress Updates")
    print("-" * 50)
    with tqdm(total=100, desc="Manual updates") as pbar:
        for i in range(10):
            # Simulate some work
            time.sleep(0.1)
            # Update progress bar by 10
            pbar.update(10)


def nested_progress():
    """Nested progress bars."""
    print("\n4. Nested Progress Bars")
    print("-" * 50)
    for i in tqdm(range(3), desc="Outer loop"):
        for j in tqdm(range(30), desc=f"  Inner {i+1}", leave=False):
            time.sleep(0.02)


def main():
    print("=" * 50)
    print("TQDM Basic Demos")
    print("=" * 50)
    
    simple_loop()
    with_description()
    manual_update()
    nested_progress()
    
    print("\n" + "=" * 50)
    print("All demos completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
