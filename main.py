<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', path='/images/favicon.png') }}" />
    <link rel="stylesheet" href="{{ url_for('static', path='/styles.css') }}" />
    <title>Sample Page</title>
  </head>
  <body>
    <h1>Random Number Generator</h1>
    <p>
      Hello, this is just a test backend app for getting random number in the range of 0 to the number of your choice
      using FastAPI.
    </p>
    <p>This is the example usage of the app in your application in JavaScript:</p>
    <pre>
const random_number = 99
url = `https://test-fastapi-app.vercel.app/${random_number}`


const handleData = async () => {
    try {
      const response = await fetch(url);
      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.log(error);
    }
  };

handleData()
    </pre>
    <p>Or you can test it right in your browser:</p>
    <p>https://test-fastapi-app.vercel.app/random number</p>
  </body>
</html>
