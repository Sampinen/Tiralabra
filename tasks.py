#pylint: skip-file
from invoke import task
from subprocess import call
from sys import platform

# Taskit kopioitu Ohjelmistotekniikka kurssilla tekemästäni tedostosta
@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    """Runs coverage tests"""
    ctx.run("coverage run --branch -m pytest", pty=True)


@task
def coverage_report(ctx):
    """Returns coverage report"""
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))

@task
def lint(ctx):
    """Checks the quality of the code"""
    ctx.run("pylint src", pty=True)
