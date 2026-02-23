import os
import subprocess

def execute_command(user_input):
    """
    CRITICAL: Remote Code Execution
    Attacker can inject: ; rm -rf /
    """
    # Using shell=True with user input - EXTREMELY DANGEROUS!
    os.system("ping " + user_input)
    subprocess.call(user_input, shell=True)
    
    # eval/exec on user input - RCE!
    eval(user_input)
    exec(user_input)
