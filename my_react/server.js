const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.get('/api/hi', (req, res) => {
    res.send({messagge: 'hi'})
});


app.listen(port, () => console.log('listening ' + port));
