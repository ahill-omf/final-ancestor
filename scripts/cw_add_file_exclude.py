# Check the .code-workspace file's folder value for project and remove it
# Add file exclude to .code-workspace to hide files/folders with name starting with "."
import argparse
import json
import logging
import os
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
file_path = '/projects/.code-workspace'

# Load existing .code-workspace json
with open(file_path, 'x') as file:
    workspace = json.load(file)
logging.debug(workspace)

workspace['settings'] = dict()
workspace['settings']['files.exclude'] = dict()
workspace['settings']['files.exclude']['**/.*'] = True

json_workspace = json.dumps(workspace, indent=4)
with open(file_path, 'w') as file:
    file.write(json_workspace)