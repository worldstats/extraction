const express = require('express');
const path = require('path');
const app = express();
const cors = require('cors');

app.use(cors());

app.use('/charts',express.static(path.resolve(__dirname,'..','charts')));

app.use('/data',express.static(path.resolve(__dirname,'..','charts')));

app.use('/pages',express.static(path.resolve(__dirname,'..','charts')));

app.use('/data',express.static(path.resolve(__dirname,'..','charts')));

app.use('/raw',express.static(path.resolve(__dirname,'..','charts')));

const PORT = 4000;

app.listen(PORT,()=>{
  console.log(`extraction server is listening on port ${PORT}`);
});
