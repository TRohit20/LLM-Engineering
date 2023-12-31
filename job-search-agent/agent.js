import { initializeAgentExecutorWithOptions } from "langchain/agents";
import { ChatOpenAI } from "langchain/dist/chat_models/openai";
import { SerpAPI } from "langchain/tools";
// import { file} from 'fs'

const tools = [new SerpAPI()];

const llm = new ChatOpenAI({modelName: "gpt-4-turbo", temperature: 0});

const executor = await initializeAgentExecutorWithOptions(tools, llm, {agentType: "openai-functions", verbose: true});

const result = await executor.run("I am a IIT graduate(Fresher with 3 good projects) looking for remote-first software engineer roles with good compensation(in the range of 30 to 40 Lakhs per annum base salary), search the internet to find 10 jobs relevant to my profile, along with description of the companies, information regarding each company to personalise the application and contact information of the hiring manager or cto of the respective company")


// Setup a Cron for the file using the expression: `0 10 * * *`, thereby agent is automated and runs everyday at 10 AM