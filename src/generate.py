from src.job import Job
from src.schedule import Schedule

import random

class Generator:
    def __init__(self, 
                # what variation we want to use
                # Currently implemented:
                #  - Vanilla
                #     - Like in the task description
                variation: str = "vanilla", 

                # parameters for the generation of the jobs
                max_reward: int = 10,
                max_penalty: int = 10,
                max_processing_time: int = None,  # Optional, if not provided, we will restrict it to 1/3 of the total time steps
                min_processing_time: int = 1,  
                ):

        self.variation = variation

        self.max_reward = max_reward
        self.max_penalty = max_penalty
        self.max_processing_time = max_processing_time
        self.min_processing_time = min_processing_time

    def generate(self, 
                num_jobs: int,
                num_time_steps: int,
                percentage_overlap: float = 0.0,  # this is not a true value, but rather a target value we should aim for
                ensure_no_gap: bool = True  # if True, we will ensure that there is no gap between the jobs
                ) -> Schedule:
        
        # generate the jobs sequentially
        jobs = []

        release = 0
        deadline = random.randint(1, num_time_steps//3)
        processing_time = random.randint(self.min_processing_time, deadline - release)
        if self.max_processing_time is not None:
            processing_time = min(processing_time, self.max_processing_time)
        reward = random.randint(1, self.max_reward)
        penalty = random.randint(1, self.max_penalty)
        jobs.append(Job(release, deadline, processing_time, reward, penalty))

        for i in range(1, num_jobs-1):
            ...

        # generate a schedule
        schedule = Schedule(jobs)

        return schedule
