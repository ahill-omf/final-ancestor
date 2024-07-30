# Check the .code-workspace file's folder value for project and remove it
import argparse
import json
import logging
import os
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
file_path = '/projects/.code-workspace'

# Gather arguments
parser = argparse.ArgumentParser("add_to_code_workspace")
parser.add_argument("project_name", type=str)
parser.add_argument("project_path", type=str)
args = parser.parse_args()

if not args.project_name:
    logging.error("project_name is blank")
    sys.exit(os.EX_DATAERR)

if not args.project_path:
    logging.error("project_path is blank")
    sys.exit(os.EX_DATAERR)

project_name = args.project_name
project_path = os.path.join(args.project_path, project_name)

logging.debug(f"{project_name}")
logging.debug(f"{project_path}")

# Load existing .code-workspace json
with open(file_path) as file:
    workspace = json.load(file)
logging.debug(workspace)

# Check if new project's name or path is present in the folder value
element_exists = False
for index, folder in enumerate(workspace['folders'], start=0):
    logging.debug(folder)
    if folder.get("name") == project_name:
        logging.debug("Matching name found.")
        element_exists = True
        matched_index = index
    if folder.get("path") == project_path:
        logging.debug("Matching path found.")
        element_exists = True
        matched_index = index

if element_exists:
    logging.debug("Element found in folders. Removing")
    workspace['folders'].pop(matched_index)
    
    # Write to file
    json_workspace = json.dumps(workspace, indent=4)
    with open(file_path, 'w') as file:
        file.write(json_workspace)