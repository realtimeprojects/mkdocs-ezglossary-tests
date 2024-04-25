import time
import subprocess
import signal

from radish import before, after, world

from acre.lib import log
from acre.playwright import Browser


@before.all
def start_server(features, marker):
    log.trace(f"Starting mkdocs server {marker}")
    world.mkdocs = subprocess.Popen('mkdocs serve', shell=True, cwd="test-doc/")
    time.sleep(5)
    assert world.mkdocs.returncode is None, "process start failed"


@after.all
def stop_server(features, marker):
    log.trace("Stopping mkdocs server")
    world.mkdocs.send_signal(signal.SIGINT)
    world.mkdocs.wait()
    rc = world.mkdocs.returncode
    assert rc == 0, f"mkdocs server existe with return code {rc}"


@before.each_feature
def start_browser(feature):
    Browser.start()
