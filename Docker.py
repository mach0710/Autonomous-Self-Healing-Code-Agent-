import subprocess
import sys

# REPLACE the previous execute_node with this one:

def execute_node(state: AgentState):
    print("--- EXECUTING (VIA SUBPROCESS) ---")
    
    # Combine code and tests
    full_script = f"{state['code']}\n\n{state['tests']}"
    
    # Write to a temporary file
    with open("temp_script.py", "w") as f:
        f.write(full_script)
        
    try:
        # Run the script using the system's python
        # capture_output=True captures stdout/stderr
        result = subprocess.run(
            [sys.executable, "temp_script.py"],
            capture_output=True,
            text=True,
            timeout=5  # Safety timeout
        )
        
        if result.returncode == 0:
            print(" Success!")
            return {"output": result.stdout, "error": None, "success": True}
        else:
            print(f" Failed: {result.stderr}")
            return {"output": result.stdout, "error": result.stderr, "success": False}
            
    except Exception as e:
        print(f"System Error: {str(e)}")
        return {"output": "", "error": str(e), "success": False}