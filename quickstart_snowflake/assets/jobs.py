from dagster import job, op

@op
def say_hello():
    print("Hello from Dagster Cloud!")

@job
def hello_job():
    say_hello()
