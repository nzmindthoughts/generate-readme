from jinja2 import Template
import argparse
import json
from pathlib import Path

GENERATE_DIR = Path(__file__).parents[0]
ROOT_DIR = Path(GENERATE_DIR).parents[0]
JINJA_TEMPLATE_DIR = ROOT_DIR / 'jinja'
CONFIG_DIR = ROOT_DIR / 'config'
CONFIG_FILE_NAME = 'project_info.json'

def load_file(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
    return data

def get_render_variables(file):
    output = {}
    filedata = load_file(file)
    obj = json.loads(filedata)
    output['group'] = obj['ApplicationGroup']
    output['name'] = obj['ApplicationName']
    output['networktype'] = obj['ApplicationNetworkType']
    output['primary'] = obj['ApplicationPrimaryStakeholder']
    output['secondary'] = obj['ApplicationSecondaryStakeholder']
    output['devaccountnumber'] = obj['DevAccountNumber']
    output['testaccountnumber'] = obj['TestAccountNumber']
    output['stagingaccountnumber'] = obj['StagingAccountNumber']
    output['prodaccountnumber'] = obj['ProdAccountNumber']
    output['class'] = obj['OrgAccountClass']
    output['devorgpath'] = obj['DevOrgPath']
    output['testorgpath'] = obj['TestOrgPath']
    output['stagingorgpath'] = obj['StagingOrgPath']
    output['prodorgpath'] = obj['ProdOrgPath']
    output['costcenter'] = obj['CostCenter']
    return output

def main():
    templatesource = load_file(str(JINJA_TEMPLATE_DIR)+"/README.j2")
    template = Template(source=templatesource)
    template_variables = get_render_variables(str(CONFIG_DIR)+"/"+str(CONFIG_FILE_NAME))
    readme_contents = template.render(template_variables)
    with open(str(ROOT_DIR)+"/README.md", "w") as readme:
        readme.write(readme_contents)
    
if __name__ == "__main__":
    main()