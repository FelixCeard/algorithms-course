#!/usr/bin/env python3

"""
Demo script to showcase the job visualization functionality.
"""

from src.generate import Generator
from src.display import display_schedule

def demo_visualization():
    """Demonstrate the job visualization with different scenarios."""
    
    print("🎯 Job Visualization Demo")
    print("=" * 50)
    
    generator = Generator()
    
    # Create a schedule with some jobs
    print("\n📊 Generating sample jobs...")
    schedule = generator.generate(
        num_jobs=5,
        num_time_steps=15,
        percentage_overlap=0.4
    )
    
    
    # Show the visualization
    display_schedule(schedule)

if __name__ == "__main__":
    demo_visualization()
