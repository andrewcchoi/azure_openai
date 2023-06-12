# azure_openai
azure open ai projects.

![Project Logo](images\logo_openai.png) <!-- Replace this URL with your own PNG logo image -->

## Description

Exploring utilization of Azure Open AI:

- Curious how to use Azure Open AI with Python

## Table of Contents (Optional)

If your README is very long, add a table of contents to make it easy for users to find what they need.

- [azure\_openai](#azure_openai)
  - [Description](#description)
  - [Table of Contents (Optional)](#table-of-contents-optional)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Folder Structure](#folder-structure)
  - [Roadmap](#roadmap)
  - [Credits](#credits)
  - [Contributing](#contributing)
  - [Code of Conduct](#code-of-conduct)

## Prerequisites
you will need your own Azure resource for Open AI, speech recognition, and setup your environment variables.
- An Azure subscription - Create one for free
- Must have access granted to DALL-E and OpenAI Services in the desired Azure subscription. Currently, access to this service is granted only by application. You can apply for access to Azure OpenAI by completing the form at https://aka.ms/oai/access. 
- Create an Azure OpenAI Service resource in the East US region in the Azure Portal. 
- Deploy a [model](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models) in your Azure OpenAI resource. 
- For more information about model deployment, see the [resource deployment guide](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource).
- Get the Azure OpenAI resource key and endpoint. After your Azure OpenAI resource is deployed, select Go to resource to view and manage keys. For more information about Cognitive Services resources, see [Get the keys for your resource](https://learn.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account#get-the-keys-for-your-resource).
- [Create a Speech resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices) in the Azure portal.
- Get the Speech resource key and region. After your Speech resource is deployed, select Go to resource to view and manage keys. For more information about Cognitive Services resources, see [Get the keys for your resource](https://learn.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account#get-the-keys-for-your-resource).

$^{1}$ GPT-4 models are currently only available by request. Existing Azure OpenAI customers can [apply for access by filling out this form](https://aka.ms/oai/get-gpt4).

## Installation

To install and run this project, you need to have Python 3.7 or later installed on your system. This project used Python 3.10. You will need to create and activate a virtual environment using the venv module. A virtual environment is an isolated Python environment that allows you to install packages without affecting the global Python installation. To create and activate a virtual environment, follow these steps:

- Open a terminal and navigate to the project directory.
- Run the following command to create a virtual environment named env (you can use any name):

  - On Windows: `py -3.10 -m venv venv`
  - On Linux or macOS: `python3.10 -m venv venv`

- Run the following command to activate the virtual environment:

  - On Windows: `venv\Scripts\activate`
  - On Linux or macOS: `source venv/bin/activate`

- You should see (venv) at the beginning of the terminal prompt indicating that the virtual environment is active.

- Run the following command to install the required packages into the virtual environment:

  - On Windows, Linux or macOS: 
    ```sh 
    pip install -r requirements.txt
    ```

  This will install all the packages listed in the requirements.txt file. You can also install any other packages you need using pip.

## Usage

To use this project, you can run the python files in the repository. To run a script, follow these steps:

- Make sure the virtual environment is active (you should see (venv) at the beginning of the terminal prompt).
- Run the following command:

  - On Windows: `python <python file>.py`
  - On Linux or macOS: `python3 <ptyhonfile>.py`

- The script will print prompt the user for an input.

Brief description of the files:

- quickstart-dalle: quickstart script to utilize Dall-E with predefined input.
- quickstart-gpt: quickstart script to utilize chat gpt with predifined input.
- how-to-basic-conversation-loop: Allows for a continuous conversation with ChatGPT without token limits.
- how-to-manage-conversation-loop: Allows for a continuous conversation with OpenAI with token limits.
- tutorial-openai-speech: Allows to utilize Azure speech recognition with ChatGPT.

## Folder Structure

Here is an example of how your project folder structure might look like:

    azure_openai
    ├── images
    │   ├── logo_openai.png
    ├── venv
    │   ├── include
    │   ├── lib
    │   ├── scripts
    │   ├── share
    │   └── pyvenv.cfg
    ├── .env
    ├── .gitignore
    ├── how-to-basic-conversation-loop.py
    ├── how-to-manage-conversation-loop.py
    ├── LICENSE
    ├── notebook.ipynb
    ├── quickstart-dalle.py
    ├── quickstart-gpt.py
    ├── README.md
    ├── requirements.txt
    └── tutorial-openai-speech.py

The env folder contains the virtual environment files. The README.md file contains this documentation. The requirements.txt file contains the list of packages required for this project.

<!-- ## Demo

Here is a demo of how this project works:

![Demo GIF](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif) Replace this URL with your own demo GIF or video -->

## Roadmap

- [ ] provide demo gif
- [ ] deploy web app
  - [ ] Chat GPT
  - [ ] DALL-E
  - [ ] Speech
  
## Credits

Here are some links to useful resources that I used:

- [Quickstarts: Get started using ChatGPT and GPT-4 with Azure OpenAI Service - Microsoft](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-python) 
- [Quickstarts: Get started generating images using Azure OpenAI Service - Microsoft](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/dall-e-quickstart?pivots=rest-api) 
- [How to: Creating a basic conversation loop - Microsoft](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt?pivots=programming-language-chat-completions#creating-a-basic-conversation-loopn) 
- [How to: Manage conversations - Microsoft](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt?pivots=programming-language-chat-completions#managing-conversations) 
- [Tutorials: Speech to Speech Chat - Microsoft](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/openai-speech?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext&tabs=windows&pivots=programming-language-python) 
- [How to specify python version used to create virtual environment? - Stack Overflow](https://stackoverflow.com/questions/45293436/how-to-specify-python-version-used-to-create-virtual-environment) 
- [How to create a venv with a different python version? - Stack Overflow](https://stackoverflow.com/questions/70422866/how-to-create-a-venv-with-a-different-python-version) 


## Contributing

Not accepting contributions at the moment.

Please follow the code of conduct and the coding style guidelines when contributing.

## Code of Conduct

This project adheres to the Contributor Covenant code of conduct. By participating, you are expected to uphold this code. 
