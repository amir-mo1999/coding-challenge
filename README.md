# Setup

## Docker Setup

Make sure your Docker engine is running. Then run the following commands:

1. Create a .env file with the following field:

```
COHERE_AI_API_KEY=Check the E-Mail.
```

2. Start the container:

```
docker build -t coding_challenge .
docker run -d -p 4000:4000 coding_challenge
```

3. Navigate to the API documentation: [http://localhost:4000/docs#/](hhttp://localhost:4000/docs#/)

## Local Setup

Make sure you have Python installed on your system. Then run the following commands:

1. Create the virtual environment:

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Create a .env file with the following field:

```
COHERE_AI_API_KEY=Check the E-Mail.
```

3. Start the application:

```
python wsgi.py
```

4. Navigate to the API documentation: [http://localhost:4000/docs#/](hhttp://localhost:4000/docs#/)

# Design Choices

## Project Structure

I structured the project by keeping config files such as Docker or .gitignore files in the root folder, while the actual application lives in its own folder. Within the root folder I created a single entry point to the backend server "wsgi.py". Generally, I tried to structure my project into files and modules, so that each one would have a clear purpose. This would keep the code base clean and not too convoluted.

## API Documentation

FastAPI works hand in hand with the pydantic library to create automated API documentation. Thus, I used the pydantic library to define input and response models for the API route. These models are all neatly visible in the Swagger documentation and provide a easy way to build decent API docs.

## Backend Framework

I chose FastAPI as my backend framework for the following reasons:

- I am quite familiar with the framework
- support for asynchronous routing
- automatic generation of API documentation
- fastest python backend framework
- excellent documentation

## Large Language Model

I chose the external Cohere API because it provides a free tier for testing out the API unlike OpenAI. It also runs much faster since it is an external service and not a local model. The latter can be quite bothersome to set up and run, especially if you are not working on a machine with lots of computational power.
It also provides simple Python bindings to send requests to the API without having to use an actual request library.

## Design of the "correct-text" endpoint

The main work happens in the /correct-text endpoint. It takes a request body containing the to be corrected text and outputs the desired list of triplet, containing the error, the correction and the error-type.

I kept my implementation very simple due to the advised time of two hours. I simply wrote a solid prompt which asks the model to search a text for errors and output a json serializable list of errors. By giving an example in the prompt, I can ensure that the output of the model is in the correct format most of the time.
Large Language Models in general perform a lot better when they are given explicit examples.

As my implementation cannot guarantee that the model outputs a JSON serializable list 100% of the time, I made sure to handle errors accordingly, so that a proper error response would be generated.

Regarding the evaluation of the system, I provide a short draft in bullet points:

- Collect a dataset of texts containing errors, their correction, and error type and compare them against the output of the system
- Measure the execution time of the request for different lengths of inputs under different levels of load
- Analyze the frequency of Errors (for example when output is not JSON serializable)
- Conduct peer reviews on code and documentation quality

Testing:

- Testing with Mock data: For testing one could also collect a dataset like the one mentioned above and write a test that executes the endpoint for the dataset. Then, one can define a tolerable error threshold (e.g. 3%). If the system does not fail more than the threshold allows for, it passes the test.

- Testing Edge Cases: One could write tests for more exotic inputs, such as senseless character sequences that are not texts, empty inputs, texts that are not written in English, Texts with no punctuation characters, sequences of numbers, etc.

# Challenges

## Local Large Language Models

I had a lot of trouble trying to get local LLMs running, since my machine is not the best. The ones I managed to get running, performed way too slowly and it made the development experience very painful.

I overcame this early on by switching to an external LLM.

## Structuring of LLM output

As LLMs produce random results, it can sometimes be difficult to make them generate structured and standardized outputs.

I mostly overcame this issue by providing an example for the desired output in the prompt and by being very clear with my instructions to the model.

## Future improvements or additions you would make if I had more time

- Usage of an LLM framework to better structure the LLM output and not rely solely on the prompt itself
- Writing of tests as outlined in the section above
- Rate limiting on the requests
- Development of a small frontend through which texts can be input and where mistakes are highlighted and their correction is shown (similar to tools like Grammarly)
