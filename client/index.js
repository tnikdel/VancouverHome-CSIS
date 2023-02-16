const cors = require('cors');

// Require express packeges.
const express = require('express');
//Request for Flask 
const request = require('request');

// Define the server.
const app = express();
// Set server.
app.use('/static', express.static('public'));
app.use(express.static("public"));

// third-party middleware
app.use(cors());

//Flask 
app.get('/website', function(req, res) {
    res.sendFile(__dirname + "/public/html/website.html");
    request('http://127.0.0.1:5000', function (error, response, body) {
        console.error('error:', error); // Print the error
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); // Print the data received
        res.send(body); //Display the response on the website
      });      
});


//----

app.get("/", function (req, res) {
    res.sendFile(__dirname + "/public/html/index.html");
})

app.get("/prediction", function (req, res) {
    res.sendFile(__dirname + "/public/html/prediction.html");
})

app.get("/contact", function (req, res) {
    res.sendFile(__dirname + "/public/html/contact.html");
})

app.get("/dashboard", function (req, res) {
    res.sendFile(__dirname + "/public/html/dashboard.html");
})

app.get("/about", function (req, res) {
    res.sendFile(__dirname + "/public/html/about.html");
})

app.get("/login", function (req, res) {
    res.sendFile(__dirname + "/public/html/Login.html");
})

app.get("/register", function (req, res) {
    res.sendFile(__dirname + "/public/html/Register.html");
})

app.get("/website", function (req, res) {
    res.sendFile(__dirname + "/public/html/templates/website.html");
})

const port = process.env.myPort || 4000;
app.listen(port, function (req, res) {
    console.log(`The server is listening to port ${port}`);
})