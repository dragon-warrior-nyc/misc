"""
Advanced tqdm demonstrations for practical use cases.
"""
import time
from tqdm import tqdm


def process_files():
    """Simulate processing multiple files."""
    print("\n1. File Processing Simulation")
    print("-" * 50)
    files = [f"file_{i}.txt" for i in range(50)]
    
    for filename in tqdm(files, desc="Processing files", unit="file"):
        # Simulate file processing
        time.sleep(0.05)


def download_simulation():
    """Simulate downloading with byte units."""
    print("\n2. Download Simulation (with byte units)")
    print("-" * 50)
    total_size = 1024 * 1024 * 10  # 10 MB
    chunk_size = 1024 * 100  # 100 KB chunks
    
    with tqdm(total=total_size, unit='B', unit_scale=True, 
              unit_divisor=1024, desc="Downloading") as pbar:
        downloaded = 0
        while downloaded < total_size:
            # Simulate download chunk
            time.sleep(0.05)
            chunk = min(chunk_size, total_size - downloaded)
            downloaded += chunk
            pbar.update(chunk)


def custom_format():
    """Progress bar with custom format."""
    print("\n3. Custom Format Progress Bar")
    print("-" * 50)
    
    bar_format = '{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'
    
    for i in tqdm(range(100), desc="Custom format", bar_format=bar_format):
        time.sleep(0.02)


def with_postfix():
    """Progress bar with dynamic postfix information."""
    print("\n4. Progress Bar with Postfix Stats")
    print("-" * 50)
    
    with tqdm(total=100, desc="Training") as pbar:
        for epoch in range(100):
            # Simulate some metrics
            loss = 1.0 / (epoch + 1)
            accuracy = min(0.99, epoch * 0.01)
            
            pbar.set_postfix(loss=f"{loss:.4f}", accuracy=f"{accuracy:.2%}")
            pbar.update(1)
            time.sleep(0.03)


def main():
    print("=" * 50)
    print("TQDM Advanced Demos")
    print("=" * 50)
    
    process_files()
    download_simulation()
    custom_format()
    with_postfix()
    
    print("\n" + "=" * 50)
    print("All advanced demos completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
