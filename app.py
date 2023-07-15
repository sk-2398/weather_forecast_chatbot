import requests
import openai
import json


OPENAI_API_KEY = 'ENTER_YOUR_OPENAI_API_KEY'
OPENWEATHER_API_KEY = 'ENTER_YOUR_OPEN_WEATHER_API_KEY'

openai.api_key = OPENAI_API_KEY
from location import extract_location

# function to fetch weather
def get_weather_data(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# OPen Ai integration function
def generate_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    if response['choices'][0]['text']:
        return response['choices'][0]['text'].strip()
    else:
        return "Sorry, I couldn't generate a response. Please try again."

# function to create chatbot logic
def process_input(user_input):
    if 'weather' in user_input.lower():
        location = extract_location(user_input)  # Implement a function to extract the location from the input
        if location:
            weather_data = get_weather_data(location)
            if weather_data:
                # Extract the relevant weather information from the response
                weather_description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp']
                humidity = weather_data['main']['humidity']
                wind = weather_data['wind']['speed']
                # Generate the weather response
                response = f"The weather in {location} is {weather_description}. The temperature is {temperature}°C. Wind speed is {wind} km/h. Humidity is {humidity}."
            else:
                response = "Sorry, I couldn't fetch the weather information. Please try again later."
        else:
            response = "Please provide a valid location."
    else:
        # Use the OpenAI language model to generate a response for non-weather prompts
        response = generate_openai_response(user_input)
    return response



# Function for chatbor prompting
def main():
    print("Welcome to the Weather Chatbot!")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = process_input(user_input)
        print("Chatbot:", response)


if __name__ == '__main__':
    main()






