from llm import LLM
from trajectory import Trajectory
class TinyAgent:
    """A minimal, modular and educational agent framework.123"""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.memory = None
        self.tools = None
        self.planner = None

        self.trajectory = Trajectory()

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step."""
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""
        # Placeholder
        return f"Executed action: {action}"


llm = LLM(model="gemma4:e4b")
agent = TinyAgent(llm=llm)
response = agent.run("Hi! How's life?")
print(response)
print(agent.trajectory.runs)


