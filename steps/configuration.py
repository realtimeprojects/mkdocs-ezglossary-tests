import yaml
import json
import shutil

from radish import given, before

from acre.lib import log


@before.all
def load_config(features, marker):
    shutil.copy("mkdocs.yml.in", "test-doc/mkdocs.yml")


@given('I set the configuration {configitem:QuotedString} to {value:QuotedString}')
def i_see_term(step, configitem, value):
    with open("test-doc/mkdocs.yml", "r") as file:
        cfg = yaml.safe_load(file)
    tree = configitem.split(".")

    for entry in cfg['plugins']:
        if "ezglossary" in entry:
            selector = entry['ezglossary']

    for element in tree[:-1]:
        log.trace(f"selector is: {json.dumps(selector, indent=4)}")

    _mapping = {"true": True,
                "false": False}
    if value in _mapping:
        value = _mapping[value]
    selector[tree[-1]] = value

    with open("test-doc/mkdocs.yml", "w") as file:
        cfg = yaml.dump(cfg, file)
