const express = require('express');
const mysql = require('mysql2');
const cors = require("cors");
const path = require('path');

const app = express();
app.use(express.urlencoded({extended: true})); 
app.use(express.json());

app.use(cors());


// Create a MySQL connection pool
const pool = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "suraj",
  database: "video",
});

// Rent a video
app.post('/api/rent', (req, res) => {
    console.log("hello");
  const { customerName, dateOut, dateDueIn } = req.body;

  // Perform validation on the request body

  // Insert the data into the Rent_Info table
  pool.query(
    'INSERT INTO Rent_Info (customer_name, date_out, date_due_in) VALUES (?, ?, ?)',
    [customerName, dateOut, dateDueIn],
    (error, results) => {
      if (error) {
        console.error(error);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // Return a success response
      return res.json({ message: 'Video rented successfully' });
    }
  );
});

// Return a video
app.put('/api/return', (req, res) => {
  const { customerName, returnDate } = req.body;

  // Perform validation on the request body

  // Update the return date in the Rent_Info table
  pool.query(
    'UPDATE Rent_Info SET date_returned = ? WHERE customer_name = ?',
    [returnDate, customerName],
    (error, results) => {
      if (error) {
        console.error(error);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // Return a success response
      return res.json({ message: 'Video returned successfully' });
    }
  );
});

// Get a list of customers who haven't returned the video
app.get('/api/not-returned', (req, res) => {
  // Retrieve the customers who haven't returned the video from the Rent_Info table
  pool.query(
    'SELECT * FROM Rent_Info WHERE date_returned IS NULL',
    (error, results) => {
      if (error) {
        console.error(error);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // Return the list of customers
      return res.json(results);
    }
  );
});

// Get a list of customers with fines charged
app.get('/api/fines', (req, res) => {
  // Retrieve the customers with fines charged from the Rent_Info table
  pool.query(
    'SELECT customer_name, fine FROM Rent_Info WHERE date_returned > date_due_in',
    (error, results) => {
      if (error) {
        console.error(error);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // Return the list of customers with fines
      return res.json(results);
    }
  );
});

// Start the server
app.listen(8000, () => {
  console.log('Server is running on port 8000');
});
