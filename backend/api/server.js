const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use('/auth', require('./routes/auth'));
app.use('/ai_assistant', require('./routes/ai_assistant'));

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});