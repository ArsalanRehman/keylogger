const express = require('express')
const fs = require('fs')
const bodyParser = require('body-parser')
const app = express()
const port = 3002

// Middleware to parse JSON request bodies
app.use(bodyParser.json())

// Define the file to store keys
const logFile = 'keys.txt'

// POST route to receive and store keys
app.post('/api/keys', (req, res) => {
  const { keys } = req.body
  console.log(keys)

  if (!keys) {
    return res.status(400).send({ message: 'No keys provided in the request' })
  }

  // Append the keys to the file
  fs.appendFile(logFile, keys + '\n', (err) => {
    if (err) {
      console.error('Error writing to file:', err)
      return res.status(500).send({ message: 'Failed to store keys' })
    }

    console.log('Keys stored successfully:', keys)
    res.status(200).send({ message: 'Keys stored successfully' })
  })
})

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`)
})
