# KobeGPT

## Table of Contents
- [AI Chatbot Project](#ai-chatbot-project)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Setup](#setup)
    - [Requirements](#requirements)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Starting the Chatbot](#starting-the-chatbot)
    - [Interacting with the Chatbot](#interacting-with-the-chatbot)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Description

This project is an AI-powered chatbot designed to simulate conversation with human users. It leverages advanced natural language processing (NLP) techniques to understand and generate human-like responses. The chatbot is capable of handling a wide range of topics and providing informative, entertaining, or support-related responses based on user input.

## Features

- Natural language understanding for various domains.
- Pre-trained on extensive datasets for better response quality.
- Customizable response generation.
- Easy integration with websites, apps, and other platforms.
- Logging and analytics for user interactions.

## Setup

### Requirements

- Python 3.8+
- Pip package installer for Python
- Internet connection for downloading dependencies

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone link
   ```

2. Navigate to project directory
   ```bash
   cd kobegpt
   ```

3. Install the required dependencies:
   ```bash
   pip install streamlit
   pip install --upgrade openai
   ```

4. [Obtain your OpenAI API key](https://platform.openai.com/docs/quickstart?context=python)

5. Insert your OpenAI API key
   ```python
   client = OpenAI(api_key="YOUR_API_KEY_HERE")
   ```

6. Open terminal and run `streamlit run kobegpt.py`

