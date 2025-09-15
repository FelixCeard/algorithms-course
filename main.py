from fire import Fire
from src.schedule import Schedule
from src.display import display_schedule
from src.bruteforce import bruteforce

def main(path_jobs: str, path_assignment: str, save_to_file: bool = False):
    schedule = Schedule()
    schedule.jobs_from_file(path_jobs)

    # print("Bruteforcing...")
    # schedule = bruteforce(schedule)

    schedule.schedule_from_file(path_assignment)
    schedule.schedule_to_file('bruteforce_assignment.txt')

    display_schedule(schedule, save_to_file=save_to_file)

if __name__ == "__main__":
    Fire(main)