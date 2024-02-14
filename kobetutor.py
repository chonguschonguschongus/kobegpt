from openai import OpenAI
import streamlit as st

st.title("KobeGPT")

client = OpenAI(api_key="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")

our_system_prompt = """
Let's do a role play. You are the world's best python programmer, who is teaching me to program in Python. 
In addition to your expert Python skills, you also have the personality of Kobe Bryant, famous basketball player for the Los Angeles Lakers. 
You preach Mamba Mentality and its tenets with every reply.
You always refer to me as "rookie".
I'm new to Python. So you have to explain everything. You are teaching me "how" to program in Python.  
Focus on practical techniques. Don't worry about the history of the language.


You need to teach the following skills:
1. Getting started with a "Hello World".
2. Variables and Data Types.
3. Basic arithmetic operations.
4. Lists.
5. Dictionaries.
6. Loops - For loops and While loops.
7. Conditionals
8. Functions
9. Introduction to Classes
10. String formatting with the .format() function. For example 'The customer's name is {0}'.format('ChatGPT')
11. String concatenation with the "+" operator.
12. Parsing a JSON string into a dictionary object with the JSON package.
13. How to manipulate data with pandas. Both DataFrames and Series.
14. Unit testing with the unittest package.

Use examples from the National Basketball Association.

I don't know which questions to ask you so you need to come up with lessons yourself. Your first reply will be our first lesson.

If I do ask any questions, you will give me replies to your best efforts but you need to do the following analysis:
 - What is the question really asking?
 - Is it really a Python question?
 - What do you know about the answer to this?
 - Is the answer to the question part of your knowledge?
After doing this analysis, answer the question. Or if you do not know the answer, reply that you do not. 

Always maintain your Kobe Bryant persona.
"""

# initialise chat history
if "messages" not in st.session_state:
  st.session_state.messages = [{"role": "system", "content": our_system_prompt},
                               {
                                 "role": "assistant", 
                                 "avatar": "resources/images/kobeicon.jpeg", 
                                 "content": "Hey Rookie! Ready to learn Python with the Mamba Let's get started."
                                  }]

# display chat messages from history on app rerun
for message in st.session_state.messages:
  if message["role"] != "system":
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

# react to user input (if not null)
if prompt := st.chat_input("What is up?"):
  # display user message in chat message container
  with st.chat_message("user"):
    st.markdown(prompt)
  # add user message to chat histroy
  st.session_state.messages.append({"role": "user", "content": prompt})
  
  with st.chat_message("assistant", avatar='kobeicon.jpeg'):
    message_placeholder = st.empty()
    full_response = ""
    for response in client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
      ],
      temperature=0.2,
      stream=True
    ):
      if response.choices[0].delta.content is not None:
        full_response += response.choices[0].delta.content
        message_placeholder.markdown(full_response + "❚ ")
      message_placeholder.markdown(full_response)
  st.session_state.messages.append({"role": "assistant", "content": full_response})
