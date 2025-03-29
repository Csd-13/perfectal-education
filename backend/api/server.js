const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Perfectal Education API');
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});