## Inspiration
Financial literacy is a crucial problem that affects individuals of all ages and walks of life. There is a worldwide need to improve financial literacy, and this app can serve as a valuable tool for educating and assisting users in making informed financial decisions. It addresses the global need for accessible, user-friendly solutions, and helps users make informed financial decisions. 

## What it does
We have integrated three functionalities to meet various financial requirements. Each component (FinProf, FinViz, and FinFiles) has a specific function. 

The FinProf module employs GPT-4 language processing technology for financial advice. It makes use of prompt engineering techniques to concentrate on financial matters, ensuring a specialized approach to financial knowledge and expertise whilst limiting the output of the model. 

The FinViz module enables users to convert raw financial data, primarily from Excel spreadsheets, into visually intuitive representations using libraries like matplotlib, seaborn, etc. It provides a variety of visualization options, such as pie charts, graphs, etc., allowing users to gain a deeper understanding of their financial data.

The Finfiles module allows for a comprehensive analysis of uploaded financial documents. Employing cutting-edge natural language processing capabilities and principles of Retrieval Augmented Generation (RAG), it extracts pertinent information and provides concise, contextually relevant answers to user-generated queries, thereby streamlining the process of document comprehension and interpretation.

## How we built it
This FinMap project was project was built on this carefully chosen set of technologies and tools, such as Streamlit for intuitive web interface development to the utilization of OpenAI's powerful language models. We used prompt engineering to concentrate on financial data, it involves the strategic design of prompts, which serve as the input to the model, to guide its responses towards the domain of finance. This meticulous process restricts the scope of generated output to the realm of financial knowledge and expertise. we incorporated an innovative technique known as Retrieval-Augmented Generation (RAG) to extract and generate pertinent data exclusively aligned with the content of the user-provided document. 
This group effort led to the creation of a set of complex tools for financial management that could change the way financial decisions are made. This application is also hosted onto Streamlit Community Cloud.

## Challenges we ran into
1. Some of us were new to git and streamlit, so it was hard to figure out how to put our code together with github and understand the documentation of streamlit.
2. Streamlit's restrictive styling made it difficult for us to design the application that was visually attractive. 
3. Integration of multiple technologies (Streamlit, OpenAI) into an overall application was a little complex and it required a careful coordination and planning.
4. During the development of FinFiles - the data generated from the file was too big not letting us query it using an LLM (Due to token limit).

## Accomplishments that we're proud of
1. Even though we had trouble dealing with the token limit and not being able to generate any response, we overcame that using Retrieval-Augmented Generation (RAG) technique.
2. Fixing the bugs we found and finishing the project in the time we were given.
3. Learning and growing as a team of developers.

## What we learned
1. Learned how to work as a team.
2. We learned Streamlit for building interactive web applications.
3. Working with OpenAI's advanced language models and prompt engineering methods and getting a deep understanding of natural language processing (NLP).
4. Managing and analyzing financial data, including extraction from documents and visualization using Excel data.
5. Working through problems like git, bugs and design gave us important skills for addressing issues.
6. Deepened our understanding on financial matters

## What's next for FinMap : Navigating the world of numbers
1. We can improve the styling by adding additional widgets and components.
2. LLMs can be used in "FinViz" to visualise data - keywords can be extracted from the users' query and these keywords can be used to visualise data, giving them the freedom to visualise whatever they are curious about.
3. Add more prompts to the model so that it gives data based on what type of user (Beginner or Experienced/Professional) is requesting data. 
4. Adding more personas to "FinProf" like a persona of a Real Estate agent or someone who is knowledgable in Medicine among others.  
