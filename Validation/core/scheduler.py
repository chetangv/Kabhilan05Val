import time
import threading
from typing import Callable
from logging import setup_logging, log_test_case

jobs = []

def define_job(job_name: str, job_function: Callable) -> None:
    jobs.append((job_name, job_function))
    log_test_case(f"Defined job: {job_name}")

def schedule_job(job_name: str, interval: int) -> None:
    job = next((job for job in jobs if job[0] == job_name), None)
    if job:
        threading.Thread(target=run_job, args=(job, interval)).start()

def run_job(job: tuple, interval: int) -> None:
    job_name, job_function = job
    while True:
        log_test_case(f"Executing job: {job_name}")
        job_function()  # Call the job function
        time.sleep(interval)

def execute_jobs() -> None:
    for job in jobs:
        run_job(job, 5)  # Run each job with a default interval of 5 seconds

def handle_shutdown() -> None:
    log_test_case("Shutting down scheduler gracefully.")
    # Logic for shutting down jobs


