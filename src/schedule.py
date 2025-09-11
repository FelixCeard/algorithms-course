from src.job import Job

class Schedule:
    def __init__(self,
                jobs: list[Job] = None, # If not provided, we will expect it to be added later
                time_steps: int = None  # Optional, if not provided, we will use the max deadline of the jobs
                ):
        """
        This class is used to hold and store a schedule.
        Once it's initialized, this object simply stores the jobs.
        You have to call the `solution(...)` method to store the assignments of the jobs to the time steps.
        """
        
        self.jobs = jobs
        
        if time_steps is None and self.jobs is not None:
            self.time_steps = max([job.deadline for job in self.jobs])
        else:
            self.time_steps = time_steps

        self.assignment = []
        # assignment is a list of tuples, where each tuple is the (time_step, job_id)
    
    def jobs_from_file(self, file_path: str):
        with open(file_path, 'r') as file:
            content = file.readlines()

        num_jobs = int(content[0])

        self.jobs = []

        for i in range(1, len(content)):
            stats = content[i].replace('\n', '').split(', ')
            release = int(stats[0])-1
            deadline = int(stats[1])
            processing = int(stats[2])
            reward = int(stats[3])
            penalty = int(stats[4])
            self.jobs.append(Job(release, deadline, processing, reward, penalty, id=i-1))

        self.time_steps = max([job.deadline for job in self.jobs])

    def jobs_to_file(self, file_path: str):
        ...

    def schedule_from_file(self, file_path: str):
        
        with open(file_path, 'r') as file:
            content = file.readlines()
            
        self.assignment = []
        for i in range(len(content)):
            stats = content[i].replace('\n', '').split(', ')

            for j in stats:
                if j == 'null' or j == '' or j == '\n':
                    continue
                
                self.assignment.append((int(j)-1, i))
                self.jobs[i].progress += 1



    def schedule_to_file(self, file_path: str):
        ...