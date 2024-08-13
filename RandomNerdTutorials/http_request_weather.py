# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details: https://RandomNerdTutorials.com/raspberry-pi-pico-w-http-requests-micropython/

import network
import time
import requests

# Wi-Fi credentials
ssid = 'HGW-63F404'
password = '101-2022615'

api_key = '9b7229c8592d440ba27120611240908'
location ='Samara'

# Request URL
url = f'https://api.weatherapi.com/v1/current.json?q={location}+&key={api_key}'

def init_wifi(ssid, password):# Init Wi-Fi Interface
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Connect to your network
    wlan.connect(ssid, password)
    # Wait for Wi-Fi connection
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print(f'Waiting for Wi-Fi connection...{connection_timeout}')
        time.sleep(1)
    # Check if connection is successful
    if wlan.status() != 3:
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True
    

if init_wifi(ssid, password):
    try:
        # Make the request
        response = requests.get(url)
        #Print the response code
        print('Response code: ', response.status_code)
        
        # Get response content
        weather = response.json()
        # Close the request
        response.close()
        
        # Print bulk weather data
        print('Weather JSON: ', weather)
        
        # Get specific weather data
        weather_description = weather['current']['condition']['text']
        print('Current weather: ', weather_description)
        
        # Temperature and humidity
        temperature_c = weather['current']['temp_c']
        temperature_f = weather['current']['temp_f']
        humidity = weather['current']['humidity']
        print(f'Temperature in Celsius: {temperature_c:.2f}')
        print(f'Temperature in Fahrenheit: {temperature_f:.2f}')
        print(f'Humidity (%): {humidity:.2f}')              
        
        # Precipitation
        precipitation = weather['current']['precip_mm']
        print(f'Precipitation in mm: {precipitation}')              
        
        # Wind
        wind_speed = weather['current']['wind_kph']
        print('Wind speed in kph:', wind_speed)
        # wlan.disconnect()
    except Exception as e:
        # Handle any exceptions during the request
        print('Error during request:', e)

    


