!pip install docker
import docker
import re

class DockerSandbox:
    def __init__(self):
        self.client = docker.from_env()

    def run_code(self, code: str, tests: str) -> dict:
        """
        Combines code and tests, runs them in a container, returns stdout/stderr.
        """
        # Combine implementation and tests
        full_script = f"{code}\n\n{tests}"

        try:
            # Run ephemeral container (auto-remove after run)
            # Using python:3.9-slim for speed
            container = self.client.containers.run(
                "python:3.9-slim",
                command=["python", "-c", full_script],
                mem_limit="128m",  # Limit memory for safety
                detach=False,      # Wait for result
                stdout=True,
                stderr=True,
                remove=True        # Auto-delete container
            )
            return {"output": container.decode("utf-8"), "error": None, "success": True}

        except docker.errors.ContainerError as e:
            # Container returned non-zero exit code (Runtime Error / Test Fail)
            return {
                "output": e.stdout.decode("utf-8") if e.stdout else "",
                "error": e.stderr.decode("utf-8"),
                "success": False
            }
        except Exception as e:
            return {"output": "", "error": str(e), "success": False}