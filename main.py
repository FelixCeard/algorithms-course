from fire import Fire
from src.schedule import Schedule
from src.display import display_schedule

def main(path_jobs: str, path_assignment: str):
    schedule = Schedule()
    schedule.jobs_from_file(path_jobs)
    schedule.schedule_from_file(path_assignment)
    display_schedule(schedule)

if __name__ == "__main__":
    Fire(main)