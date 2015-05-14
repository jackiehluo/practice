# INSTRUCTIONS

## 1. Race Average
Right now, the program has test data for the "times" array, so replace that with the array you'd like to use!

To run the program, just enter Terminal, go to the directory with the files, and run it with `python RaceAverage.py`. The output will be the average length of time for the races.

## 2. MaxMind GeoLite API
To build the API service, I used Flask, a Python microframework, which has some great tools for this purpose. The service takes the IP address as input in the URL, finds it in the GeoCities-Blocks CSV and gets the location ID, and then finds the location ID in the GeoCities-Location CSV, returning that dictionary and passing it to Jsonify, a great tool in Python that converts dictionaries to JSON data. I used DictReader in the CSV library for that reason.

Dependencies of the program can be installed using `pip` [here](https://pip.pypa.io/en/latest/installing.html). Download "get-pip.py" and run `python get-pip.py`. Then, install Flask using `pip install Flask`.

To run the program, enter Terminal, go to the directory with the files, and run it with "python GeoLiteAPI.py". It should show `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`, so open a new Terminal window and enter the curl command with the URL of your choice. Here are a few examples:

`curl -i http://localhost:5000/202.575.3.6`

`curl -i http://localhost:5000/168.217.6.0`

`curl -i http://localhost:5000/342.866.25.28`