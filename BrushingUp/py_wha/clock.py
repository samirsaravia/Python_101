from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', seconds=10)

sched.start()
