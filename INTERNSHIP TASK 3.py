import time
from collections import deque

# Define pipeline stages
class PipelineProcessor:
    def __init__(self):
        self.instructions = deque()  # Queue to hold instructions
        self.pipeline = [None] * 4  # 4 pipeline stages
        self.registers = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0}  # Register file

    def fetch(self, instruction):
        """Fetch stage: Load instruction into the pipeline."""
        self.pipeline[0] = instruction

    def decode(self):
        """Decode stage: Parse instruction and prepare for execution."""
        if self.pipeline[1]:
            instruction = self.pipeline[1].split()
            return instruction
        return None

    def execute(self, instruction):
        """Execute stage: Perform arithmetic or memory operations."""
        if instruction:
            op, dest, src1, src2 = instruction[0], instruction[1], instruction[2], instruction[3]
            if op == 'ADD':
                self.registers[dest] = self.registers[src1] + self.registers[src2]
            elif op == 'SUB':
                self.registers[dest] = self.registers[src1] - self.registers[src2]
            elif op == 'LOAD':
                self.registers[dest] = int(src1)  # Load immediate value into register

    def write_back(self, instruction):
        """Write Back stage: Store results into registers."""
        if instruction:
            print(f"Writing back: {instruction[1]} = {self.registers[instruction[1]]}")

    def pipeline_step(self):
        """Simulate one clock cycle of the pipeline."""
        # Move instructions through the pipeline stages
        self.pipeline[3] = self.pipeline[2]  # WB
        self.pipeline[2] = self.pipeline[1]  # EX
        self.pipeline[1] = self.pipeline[0]  # ID
        self.pipeline[0] = None  # Fetch gets new instruction

        if self.pipeline[3]:
            self.write_back(self.decode())
        if self.pipeline[2]:
            self.execute(self.decode())
        if self.pipeline[1]:
            self.decode()

    def run(self, instructions):
        """Run the processor with given instructions."""
        for instr in instructions:
            self.fetch(instr)
            self.pipeline_step()
            time.sleep(0.5)  # Simulating clock cycle delay

        # Ensure remaining instructions complete execution
        for _ in range(3):
            self.pipeline_step()
            time.sleep(0.5)

# Example instruction set
instructions = [
    "LOAD R1 10 0",
    "LOAD R2 20 0",
    "ADD R3 R1 R2",
    "SUB R4 R2 R1"
]

# Run the pipeline processor
processor = PipelineProcessor()
processor.run(instructions)
