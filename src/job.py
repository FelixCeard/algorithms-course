import uuid


class Job:
    def __init__(self,
                release: int,
                deadline: int,
                processing: int,
                reward: int,
                penalty: int,
                id: int = None,
                ):

        """
        This simply stores a job as an object.

        The progress attribute is used to store how many time the job has been worked on. 
        If progress = processing, the job is complete.

        - maybe add is_done as an attribute?
        """

        self.release = release
        self.deadline = deadline
        self.processing = processing
        self.reward = reward
        self.penalty = penalty
        self.id = id if id is not None else str(uuid.uuid4())

        self.progress = 0

    def __str__(self):
        return f"Job(id={self.id})"
    
    def work(self):
        self.progress += 1