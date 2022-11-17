from zefactor.run.runner_manager import RunnerManager

class Boot:

  def __init__(self):
    pass;

  def boot(self):

    runner = RunnerManager()
    runner.run()

if __name__ == "__main__":
  boot = Boot()
  boot.boot()
