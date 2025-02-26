# PIPELINE-PROCESSOR-DESIGN

 COMPANY NAME : CODTECH IT SOLUTIONS

 NAME : PRATHIKSHA R

 INTERN ID : CT08RWF

 DOMAIN : VLSI

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

DESCRIPTION : 

In this task, we simulate a 4-stage pipelined processor using Python. The goal is to understand how instructions move through different stages and how basic operations like addition, subtraction, and loading values into registers are performed efficiently.

Understanding the Pipeline Stages
A pipeline processor divides instruction execution into four key stages:

1️⃣ Fetch: Retrieves the instruction from memory.
2️⃣ Decode: Interprets the instruction and extracts relevant components.
3️⃣ Execute: Performs the operation (arithmetic or memory-related).
4️⃣ Write Back: Stores the result in the appropriate register.

This system ensures that multiple instructions are processed at the same time—one instruction may be in the execution stage, while another is being decoded, and a new one is being fetched.

How the Code Works
1. Defining the Processor
The code is structured using a class named PipelineProcessor, which represents the processor. It contains:
✅ A queue (deque) to manage incoming instructions.
✅ A pipeline with 4 stages, represented as a list.
✅ A register file, which stores values for different registers (R1, R2, R3, R4).

The processor supports three operations:

ADD: Adds two registers and stores the result in a destination register.
SUB: Subtracts one register value from another.
LOAD: Loads an immediate value into a register.
2. Fetching the Instruction
Fetching means retrieving an instruction from memory and placing it in the pipeline for processing. The function fetch() loads an instruction into the first stage of the pipeline.

python
Copy
Edit
def fetch(self, instruction):
    self.pipeline[0] = instruction
Example:
If the instruction is "LOAD R1 10 0", it is placed in the fetch stage of the pipeline.

3. Decoding the Instruction
Decoding extracts the operation type (ADD, SUB, LOAD) and the registers involved from the instruction.

python
Copy
Edit
def decode(self):
    if self.pipeline[1]:  
        instruction = self.pipeline[1].split()
        return instruction  
    return None
For "ADD R3 R1 R2", this function separates:

Operation: ADD
Destination Register: R3
Source Registers: R1, R2
4. Executing the Instruction
This stage performs the actual operation based on the decoded instruction.

python
Copy
Edit
def execute(self, instruction):
    if instruction:
        op, dest, src1, src2 = instruction[0], instruction[1], instruction[2], instruction[3]
        if op == 'ADD':
            self.registers[dest] = self.registers[src1] + self.registers[src2]
        elif op == 'SUB':
            self.registers[dest] = self.registers[src1] - self.registers[src2]
        elif op == 'LOAD':
            self.registers[dest] = int(src1)
For "ADD R3 R1 R2", the result is stored as:

𝑅
3
=
𝑅
1
+
𝑅
2
R3=R1+R2
5. Writing Back the Result
After execution, the final result is written back to the register file.

python
Copy
Edit
def write_back(self, instruction):
    if instruction:
        print(f"Writing back: {instruction[1]} = {self.registers[instruction[1]]}")
This function ensures that the computed values are stored in the correct destination register.

6. Running the Pipeline
The run() function executes multiple instructions in the pipeline one after another, ensuring that different instructions occupy different stages at the same time.

python
Copy
Edit
def run(self, instructions):
    for instr in instructions:
        self.fetch(instr)  # Load new instruction
        self.pipeline_step()  # Move instructions through the pipeline
        time.sleep(0.5)  # Simulating a clock cycle delay

    # Ensure all instructions complete execution
    for _ in range(3):
        self.pipeline_step()
        time.sleep(0.5)
Each instruction moves through the four pipeline stages step by step, simulating how a real processor works.

7. Example Instructions Used
The processor executes the following sample instructions:

python
Copy
Edit
instructions = [
    "LOAD R1 10 0",
    "LOAD R2 20 0",
    "ADD R3 R1 R2",
    "SUB R4 R2 R1"
]
These instructions will:

Load 10 into R1
Load 20 into R2
Add R1 and R2, storing the result in R3
Subtract R1 from R2, storing the result in R4
8. Expected Output
The pipeline processor prints results to confirm execution:

yaml
Copy
Edit
Writing back: R1 = 10
Writing back: R2 = 20
Writing back: R3 = 30
Writing back: R4 = 10
This means the processor correctly executed all operations.



