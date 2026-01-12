from typing import TypedDict, Optional

class AgentState(TypedDict):
    requirement: str      # The user's request
    code: str             # The current python code
    tests: str            # The unit tests
    error: Optional[str]  # Capture stderr if failed
    output: Optional[str] # Capture stdout
    iterations: int       # Iteration counter
    success: bool         # Did it pass?