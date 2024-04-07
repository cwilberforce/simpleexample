from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def sender(task):
    task.run(task=send_command, command="show cdp neighbors detail")

results = nr.run(task=sender) 
print_result(results)
