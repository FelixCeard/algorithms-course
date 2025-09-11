import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


from src.schedule import Schedule

def display_schedule(schedule: Schedule):
    """
    Display jobs with their rewards and penalties using matplotlib.
    Uses white background, light blue for scheduled jobs, and red for assignments.
    """
    if not schedule.jobs:
        print("No jobs to display")
        return
        
    max_time_step = schedule.time_steps

    # create a grid with max_time_step columns and len(schedule.jobs) rows
    # 0 = white background, 1 = light blue (job time window), 2 = red (assignment)
    grid = np.zeros((len(schedule.jobs), max_time_step))

    # fill the grid with the jobs (light blue for available time slots)
    for jobid, job in enumerate(schedule.jobs):
        for time_step in range(job.release, job.deadline):
            grid[jobid, time_step] = 1

    # fill the grid with assignments (red for actual scheduled work)
    for time_step, job_id in schedule.assignment:
        # find the job index by job_id
        job_index = next((i for i, job in enumerate(schedule.jobs) if job.id == job_id), None)
        if job_index is not None:
            grid[job_index, time_step] = 2

    # create custom colormap: white, light blue, red
    colors = ['white', 'lightblue', 'red']
    custom_cmap = ListedColormap(colors)

    # display the grid with figsize scaled to the number of jobs and time steps
    height_per_job = 0.6
    width_per_time_step = 0.4
    figsize = (max_time_step * width_per_time_step + 2, len(schedule.jobs) * height_per_job + 2)
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.imshow(grid, cmap=custom_cmap, vmin=0, vmax=2)
    ax.set_xlabel('Time Steps')
    ax.set_ylabel('Jobs')

    
    # Add vertical bars at each time step
    for t in range(max_time_step + 1):
        ax.axvline(x=t - 0.5, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    for jobid, job in enumerate(schedule.jobs):
        ax.axhline(y=jobid + 0.5, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

    # set the x ticks to the reward and penalty of the jobs, bold reward if finished, else bold penalty
    ax.set_yticks(range(len(schedule.jobs)))
    yticklabels = []
    for job in schedule.jobs:
        finished = job.progress == job.processing
        if finished:
            label = rf"($\bf{{{job.reward}}}$, -{job.penalty})"
        else:
            label = rf"({job.reward}, -$\bf{{{job.penalty}}}$)"
        yticklabels.append(label)
    ax.set_yticklabels(yticklabels)

    total_score = sum([job.reward if job.progress == job.processing else -job.penalty for job in schedule.jobs])
    ax.set_title(f'Job Schedule Visualization\nTotal Score: {total_score}')
    
    # Display the processing time centered within the job's time window bar
    for jobid, job in enumerate(schedule.jobs):
        center_x = job.release + (job.deadline - job.release) / 2
        ax.text(center_x, jobid, str(job.processing), ha='center', va='center', color='black', fontsize=10, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, boxstyle='round,pad=0.2'))


    plt.show()