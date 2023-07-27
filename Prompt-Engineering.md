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

### Tactics for Principle 1
1. Use delimiters to clearly indicate distinct parts of the input
  - Delimiters can be any clear punctuation that seperates specific pieces of text from rest of the prompt like: ```, """, < >, `<tag> </tag>`, `:`.
  - It is a helpful technique to prevent prompt injection(Comes in handy when the user is expected to input into the prompt).
2. Ask for a Structured Output( like JSON format when building a public API or HTML or more)
  - This helps when building a API so you can return a JSON object or more specific responses.
3. Ask the model to check whether the conditions are satisfied, check assumptions required to do the task are met instead of assuming they are met.
  - You can consider potential edge cases and how the model should handle them.
4. Few shot prompting- Providing successful examples of completion tasks and then ask the model to perform the task.

### Tactics for Principle 2
If a model is making reasoning errors by rushing to a in correct conclusion, Try reframing the query to request a chain or series of relevant reasoning before the model provides its final answer. (You can even ask the model to think longer)

1. Specify the steps required to complete a task,
Example prompt:
```python
prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Italian summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
```
2. Instruct the model to work out its own solution before rushing to a conclusion.
   Ask it to solve the problem or find the solution by itself first and then come to a conclusion or provide one. Give specifics or so.

## Model limitations
- It doesn't know the boundaries of its knowledge so it might answer obscure topics or give out plausible answers which are not true. This is called Hallucination.
- **One way to reduce hallucinations or come through to instruct the model to first find any relevant information, answer the questions or request made based on those relevant info and have a way to trace their way back to source documents.**

## Iterative Prompt Development
**Idea ---> Implement the prompt ---> Experimental result ---> Error Analysis ---> Refine the idea and/or the prompt ---> Repeat**

- There is no perfect prompt especially for your applications.
- To iterate, find out what is lacking in the response, what is the target and keep iterating the prompt to get closer and closer to the desired output
- Clarify instructions and give it the space/time to think
- Being a good at prompt engineering does not mean you need to be great at writing perfect prompts in one attempt, rather having a process to iterate and get the right prompt.
- For sophisticated or more complex prompts, You can refine your prompts against a batch of examples or data such as to test how prompts perform, find average performance or so. BUT, this is usually done only when a application is more mature and you have those metrics to drive those incremental last few steps to improve prompts.
- How can you train or test against multiple examples? Use a for loop over a array of examples maybe? Try it out, put your programming fundamentals to use. 

### Summarizing Text
- You can summarise text based on words, character count or sentences limit etc.
- You can also summarise with a focus on certain purpose or flow(Like a particular group in the business)
- Summaries might involve topics we do not require or relate to the prompt or concern, In such cases, you can use 'Extract' instead of summary.

## Inferences
The kind of tasks where the model takes the text or data and does some kind of analysis on it such as sentiment analysis, extracting labels or names etc.
For instance, you can get the sentiment out of a review or tweets using the sentiment prompt. You can use the output for processing maybe.

You can use this to extract specific information which actually a part of NLP, Let's say you ask to extract certain information, then ask for the format of the output to be JSON, then you can use the output which is of JSON format can be easily stored in a python dictionary or list of dictionaries and used for further processing.

**You can do both the above cases and more inferences with data within just a single prompt**

You can also give it a long piece of text and prompt the model to infer the topics of the conversation or in the conversation. You can also use a LLM to index into a list of topics.
```python
prompt = f"""
Determine five topics that are being discussed in the \
following text, which is delimited by triple backticks.

Make each item one or two words long. 

Format your response as a list of items separated by commas.

Text sample: '''{conversation}'''
"""
response = get_completion(prompt)
print(response)
```
## Transforming
You can use a LLM to transform your input into a desired output.
- LLMs are trained on many languages and sources to varying degrees of proficiency.
- You can translate text from one language to another.
- You can also do multiple translations at once. (Maybe a Universal Translator)
- You can also translate text based on the relation such as formal or informal
- Similar to above, you can transform the tone of the text such as the way you mail a company is different from the way you text your friend and more.
- You can also tranform between formats such as from JSON to HTML or from HTML to JSON (Prompt should describe how the input and output are supposed to be).
- You can also use LLMs to do spell check or grammar check or proofread.
- You can ask the model to follow a style guide, change tone and address certain level of users and also have the output in a markdown format and more.

## Expanding
The LLM can also be used to take smaller pieces of text and use it to write or respond with longer messages or content using another parameter of the moedel called temperature. But you need to use this in a responsible way.
- For instance, you can be sending mails as customer service using sentiments by prompting among the lines as " You are a AI customer service bot, do ...."
```python
prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
```
- Temperature is simply defined the degree of randomness, higher the temperature, higher the randomness and risk.
- In standard application where reliability and predictability is crucial, use 0 which is default, increase as per your choice if you want some creativity or randomness.
- You get more varying outputs with more variations when you have higher temperature. 0 has less variations in output.
- 
## Building a ChatBot using LLM
Even ChatGPT is a web UI that lets user have conversations with it. Similarly you can build custom chatbots like Customer Service Assistant, Tutor, planner or Order taker for a restaurant etc based on your application. 
- Chat models like chatGPT are trained to take series of messages as input and return a model generated message as output.
- Applications like chatGPT are trained to take a series of messages from user as input and return a model generated message as output.
- To create a chatbot, you can have a list of messages that can passed to the model from various roles such as "system"(Usually the first message), "user", "assistant" and so on.
