import subprocess
import shlex

def safe_execute(user_input):
    """
    SAFE: Proper command execution
    Uses subprocess with array arguments (no shell)
    """
    # Whitelist allowed commands
    allowed_commands = ['ls', 'pwd', 'date']
    
    # Parse and validate
    args = shlex.split(user_input)
    if args[0] not in allowed_commands:
        raise ValueError("Command not allowed")
    
    # Execute without shell=True - SAFE!
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
