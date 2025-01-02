# Prompt Engineering

LLM stands for a Large Language Model which is essentially a model trained on large amounts of data such as text, images or video.

A Language model is built by using the supervised learning (x->y) to repeatedly predict the next word.

As you know, models like GPT are in a over-simplified manner = Next TOKEN Generator.

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

GPT is a base LLM of sorts, ChatGPT is a Instruction-tuned LLM.
How to get a Base LLM to be an Instruction-tuned LLM? (Take days based on your resources available)
- Train a base LLM on a lot of data (Depending on the systems/GPU at your disposal, this can take months)
- Further train the model to fine-tune it with examples where the output follows of an input instruction.
- Evaluate the outputs by humans based on certain criteria.
- Further tune the LLM to increase the probability that it generates the more highly rated outputs (Basically RLHF!) - Reinforcement Learning from Human Feedback

System(Sets tone/Behaviour of the assistant) -> Assistant(LLM Responses)
<-> User(Prompts)
```python
messages =  [  
{'role':'system', 
 'content':"""You are an assistant who responds in the style of Dr Drake Ramorey."""},    
{'role':'user', 
 'content':"""Explain to me the cause of Kidney failure for a 040 year old?"""},  
] 
```

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
- System message is the first message usually that sets the behaviour or persona of the chatbot. It's like a high-level instruction in the conv where system is whispering in the ears of the Assistant(model).
- The benefit of system message is for you as a developer, as you have a way to kind of frame the conversation without making the request itself a part of the conversation.(So, User does not know about it)
- Each conversation with a LLM is a standalone interaction which means you need pass in all the messages and relevant information for the model to draw from.
- If you want the model to remember the conversation or earlier messages, that is called context.
- One way to pass the context is to append the user message and assistant messages to the list of messages
```python
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
```

The prompt I had written for the GRE tutor bot:
```python
context = [ {'role':'system', 'content':"""
You are now a GRE tutor who is a specialist at Vocabulary and AWA section. \
Your job is to prepare the user for GRE exam's verbal sections, \
you are a expert and should teach the user everything from new vocabulary words used \
in GRE, to teaching them how to tackle the exam, how to solve each type of question.
Teach the user how to improve their score and get their desried score whatever it might be, teaching from words \
to everything else required must be personalised based on the user and their desired score and state.

So, you should start by asking the user if they want a personalised and detailed plan to study and practise. \
If the user asks you for tips or study plan for verbal, make sure to \
ask the user about enough information such time to prepare, current proficiency with \
vocab and other required details and then personalise a plan to ace \
verbal sections of the exam.
and then ask them if they are good with it or need any changes made, if the user does not need any changes, ask them if they now want to learn new words \
or learn how to tackle question types and practise with real questions.

If the user wants to learn new words, start to teach the user new words, one at a time, each new \
word must be taught using 2 simple yet good examples to help them \
retain the definition and use of particular words. \ Make sure to teach the user a new word everytime with good examples \
Everytime the user moves on to the next word, make sure to subtlely test \
them with previous words you taught them and correct them if they go wrong and teach again in a \
more effective manner. \
After you teach the user 2 words, make sure to test them with actual GRE questions

Keep teaching the user new words and more as per the plan given to them.

Now, if the user wants to just learn how to tackle the question types, then teach them how to tackle each question type \
with practise questions.

"""} ]  # accumulate messages
```

* **Evaluate Inputs**: It might be more efficient to classify your tasks from input and then use the classification of Instruction sets to determine which instructions to use for carrying out the user query. You can do this by defining strict/fixed categories and hard-coding instructions that are relevant for handling tasks under each category.

* **Moderation**: Most LLM providers including OpenAI now support an API called 'Moderation API'. The idea behind the moderation API is to ensure you build the AI system with guardrails and safely without any harmful content or embracing of such. 

- Use Delimiters in your AI powered systems to avoid Prompt injections to prevent users from misusing the service/systems. (You can define your own delimiter). Further make it secure by checking the user input prompt for delimiters and replace them with empty strings.

You can use Moderation API for evaluating the output quality of the system too. Along with other prompting techniques like Chain of thought to thoroughly evaluate the responses from the model, allwowing you to flag answers based on the application use case. 

You can use the model itself to evaluate the answers, then ask to generate a better answer if needed. (But this becomes obsolete with advanced models and increases latency for production applications.) 

## Chain Of Thought

One of the biggest hindrances with AI base models today is reasoning and planning. The exception applies to models like o1 ofc. 
But largely, these base models are next token generators and are quick to answer which in many cases leads to errors. The models do not actually take the time to think through, plan and reason, thereby producing inaccurate answers. 

One way to tackle this issue of planning and reasoning, apart from paying 200$/month for OpenAI's o1 or other equivalent offerings, is 'Chain Of Thought'.

You can use simple tactics like delimiters and effective instructions to reason at each step before making an analysis and respond.

But again, all applications may not intend to showcase the model's reasoning to the user. In such cases, we can use 'Inner monologue', which is a very fancy way to just say that we hide the model's reasoning from the user.

Or, you can use little more sophisticated techniques like "Chain prompting", where you essentially break down complex tasks and split up a task into multiple sub-tasks, while chaining their outputs/prompts for a cohesive response generation. 
This allows you to focus on each sub-task, get quality results for each step and you can also use those outputs as inputs for the next step/task and so on to finally reach the desired state.
The system can be classfied and broken down into sub-tasks, where each sub-task contains instructions related to only a single state of the task. Thereby, reducing the likelihood of errors. And making it easier to handle systems, ensuring model has all the relevant info to carry out the task.
It also reduces cost as you can choose to skip certain chain of prompt or steps based on the classification or need to carry out the task.
This is also easier to test.
Helps overcome context limitations + lower confusion for the model. 
This technique also allows you to use external tools like web search or Databases.
Overall, For complex tasks, you can keep track of the state external to the LLM(in your own code).  

* building a System with AI model in a very simple, starter pack manner can be summarised as:
Evaluate inputs to see if it needs to be flagged -> Use either chain of thought or prompt chaining in order to carry out the task on hand for the application -> Evaluate the Model's responses and return to user if not flagged. 

- Add 'tricky' exmaples opportunistically
- Develop metrics to measure performance
- Ideal to automate the testing process for the development/hold-out set. 