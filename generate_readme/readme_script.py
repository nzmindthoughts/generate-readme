from jinja2 import Template
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description='Accept application environment')
parser.add_argument('--aws_environment', type=str, help='Environment of AWS account in which templates will be deployed', required=True)
args = vars(parser.parse_args())

ENVIRONMENT_NAME = args['aws_environment']
GENERATE_DIR = Path(__file__).parents[0]
ROOT_DIR = Path(GENERATE_DIR).parents[0]
JINJA_TEMPLATE_DIR = ROOT_DIR / 'jinja'
CONFIG_DIR = ROOT_DIR / 'config'
CONFIG_FILE_NAME = 'account_info.'+ENVIRONMENT_NAME+'.json'

def load_file(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
    return data

def get_render_variables(file):
    output = {}
    filedata = load_file(file)
    obj = json.loads(filedata)
    output['alias'] = obj['AccountAlias']
    output['env'] = obj['ApplicationEnvironment']
    output['group'] = obj['ApplicationGroup']
    output['AppId'] = obj['ApplicationId']
    output['name'] = obj['ApplicationName']
    output['networktype'] = obj['ApplicationNetworkType']
    output['primary'] = obj['ApplicationPrimaryStakeholder']
    output['secondary'] = obj['ApplicationSecondaryStakeholder']
    output['rootemail'] = obj['RootEmail']
    output['accountnumber'] = obj['AccountNumber']
    output['class'] = obj['OrgAccountClass']
    output['orgpath'] = obj['OrgPath']
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