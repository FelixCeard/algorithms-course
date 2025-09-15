"""
Bruteforce the best schedule by using a simple brute force algorithm.
"""

from src.schedule import Schedule
from src.job import Job
from itertools import product
import copy
from tqdm import tqdm

def calculate_score(jobs: list[Job]) -> int:
    """
    Calculate the total score for a given job assignment.
    Score = sum(reward for completed jobs) - sum(penalty for incomplete jobs)
    """
    total_score = 0
    for job in jobs:
        if job.progress == job.processing:  # Job completed
            total_score += job.reward
        else:  # Job incomplete
            total_score -= job.penalty
    return total_score

def is_valid_assignment(jobs: list[Job], assignment: list[tuple[int, int]]) -> bool:
    """
    Check if an assignment is valid given job constraints.
    assignment: list of (time_step, job_id) tuples
    """
    # Reset job progress for validation
    for job in jobs:
        job.progress = 0
    
    # Sort assignment by time step to process in chronological order
    sorted_assignment = sorted(assignment)
    
    # Track work on each job
    for time_step, job_id in sorted_assignment:
        # Find the job
        job = next((j for j in jobs if j.id == job_id), None)
        if job is None:
            return False
        
        # Check if time step is within job's available window
        if time_step < job.release or time_step >= job.deadline:
            return False
        
        # Check if job is already completed
        if job.progress >= job.processing:
            return False
        
        # Work on the job
        job.progress += 1
    
    return True

def count_total_assignments(jobs: list[Job], time_steps: int) -> int:
    """
    Calculate the total number of possible assignments.
    This is used for the progress bar.
    """
    total_combinations = 1
    
    for t in range(time_steps):
        choices = 1  # Option to do nothing
        # Add all jobs that could potentially be worked on at this time step
        for job in jobs:
            if job.release <= t < job.deadline:
                choices += 1
        total_combinations *= choices
    
    return total_combinations

def generate_all_assignments(jobs: list[Job], time_steps: int):
    """
    Generate all possible assignments of jobs to time steps.
    This is the brute force part - we try every combination.
    """
    # For each time step, we can either do nothing (None) or work on any job
    choices_per_timestep = []
    
    for t in range(time_steps):
        choices = [None]  # Option to do nothing
        # Add all jobs that could potentially be worked on at this time step
        for job in jobs:
            if job.release <= t < job.deadline:
                choices.append(job.id)
        choices_per_timestep.append(choices)
    
    # Generate all combinations using itertools.product
    for assignment_choice in product(*choices_per_timestep):
        # Convert to assignment format: list of (time_step, job_id) tuples
        assignment = []
        for time_step, job_id in enumerate(assignment_choice):
            if job_id is not None:
                assignment.append((time_step, job_id))
        
        yield assignment

def bruteforce(schedule: Schedule) -> Schedule:
    """
    Bruteforce the best schedule by checking every possible assignment.
    Returns the schedule with the optimal assignment.
    """
    if not schedule.jobs:
        return schedule
    
    # Calculate total number of assignments for progress bar
    total_expected = count_total_assignments(schedule.jobs, schedule.time_steps)
    
    best_assignment = []
    best_score = float('-inf')
    best_jobs = None
    
    total_assignments = 0
    valid_assignments = 0
    
    print(f"Starting brute force search...")
    print(f"Expected total assignments to check: {total_expected:,}")
    print(f"Jobs: {len(schedule.jobs)}, Time steps: {schedule.time_steps}")
    print()
    
    # Try all possible assignments with progress bar
    with tqdm(total=total_expected, desc="Searching assignments", unit="assignments") as pbar:
        for assignment in generate_all_assignments(schedule.jobs, schedule.time_steps):
            total_assignments += 1
            pbar.update(1)
            
            # Create a copy of jobs to test this assignment
            test_jobs = copy.deepcopy(schedule.jobs)
            
            # Check if assignment is valid
            if is_valid_assignment(test_jobs, assignment):
                valid_assignments += 1
                score = calculate_score(test_jobs)
                
                if score > best_score:
                    best_score = score
                    best_assignment = assignment.copy()
                    best_jobs = copy.deepcopy(test_jobs)
                    
                    # Update progress bar description with current best score
                    pbar.set_postfix({
                        'best_score': best_score,
                        'valid_found': valid_assignments
                    })
    
    print(f"\nBrute force completed:")
    print(f"  Total assignments tried: {total_assignments:,}")
    print(f"  Valid assignments found: {valid_assignments:,}")
    print(f"  Best score: {best_score}")
    
    # Update the schedule with the best assignment
    schedule.assignment = best_assignment
    
    # Update job progress for the final result
    if best_jobs:
        for i, job in enumerate(schedule.jobs):
            job.progress = best_jobs[i].progress

    return schedule
    