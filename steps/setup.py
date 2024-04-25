import os
import time
import signal
import subprocess

from radish import before, after, world

from acre.lib import log, settings
from acre.playwright import Browser


@before.all
def start_server(features, marker):
    mkdocs_cmd = 'mkdocs serve'
    mkdocs_cmd += f" -a {settings.mkdocs.address}"
    log.trace(f"Starting mkdocs server [{mkdocs_cmd}]")
    mkdocs_cmd = 'ls ../.acre-env/bin/'
    log.trace(f"PATH: {os.environ['PATH']}")
    world.mkdocs = subprocess.Popen(mkdocs_cmd, cwd="test-doc/", shell=True)
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
