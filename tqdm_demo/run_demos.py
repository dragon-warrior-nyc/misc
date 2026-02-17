#!/usr/bin/env python3
"""
Main entry point for tqdm demos.
"""
import sys
from tqdm_demo import basic_demo, advanced_demo


def print_menu():
    print("\n" + "=" * 60)
    print("TQDM Demo Suite")
    print("=" * 60)
    print("\nChoose a demo to run:")
    print("  1. Basic demos (simple loops, nested bars)")
    print("  2. Advanced demos (file processing, downloads, custom formats)")
    print("  3. Run all demos")
    print("  q. Quit")
    print("=" * 60)


def main():
    while True:
        print_menu()
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == '1':
            basic_demo.main()
        elif choice == '2':
            advanced_demo.main()
        elif choice == '3':
            print("\n" + "🚀" * 30)
            print("Running ALL demos...")
            print("🚀" * 30)
            basic_demo.main()
            advanced_demo.main()
            print("\n" + "✅" * 30)
            print("All demos finished!")
            print("✅" * 30)
        elif choice == 'q':
            print("\nGoodbye! 👋")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye! 👋")
        sys.exit(0)
