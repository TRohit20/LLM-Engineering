# Prompt Engineering

LLM stands for a Large Language Model which is essentially a model trained on large amounts of data such as text, images or video.

## Two types of LLMS
There are two general types of LLMs:
### Base LLM
- The type of LLM that is often trained to predict the next best work based on text-training data, often trained on large amounts of data from the internet or any other data,

### Instruction Tuned LLM
- This is the type of LLM that is trained to follow instructions with good attempts at following those instructions.
- How are these built or trained? They start off with Base LLM, it is further trained and fine-tuned with input and outputs
- Input and outputs are usually instructions and good attempts at following those.
- And are often further trained with Reinforcement Learning with Human Feedback to help system follow instructions.
- Practical applications today mostly use Instruction based LLM.

## Principles of Prompt Engineering
1. Write clear and specific instructions with as much detail and clarity as possible(Including tone, other elements are a plus).
2. Give the LLM some time to think.

### Tactics
1. Use delimiters to clearly indicate distinct parts of the input
  - Delimiters can be any clear punctuation that seperates specific pieces of text from rest of the prompt like: ```, """, < >, `<tag> </tag>`, `:`.
  - It is a helpful technique to prevent prompt injection(Comes in handy when the user is expected to input into the prompt).
2. Ask for a Structured Output( like JSON format when building a public API or HTML or more)
  - This helps when building a API so you can return a JSON object or more specific responses.
3. Ask the model to check whether the conditions are satisfied, check assumptions required to do the task are met instead of assuming they are met.
  - You can consider potential edge cases and how the model should handle them.
