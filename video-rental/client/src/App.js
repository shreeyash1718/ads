import React, { useState, useEffect } from 'react';
import axios from 'axios';


function App() {
  const [customerName, setCustomerName] = useState('');
  const [dateOut, setDateOut] = useState('');
  const [dateDueIn, setDateDueIn] = useState('');
  const [returnDate, setReturnDate] = useState('');
  const [notReturnedList, setNotReturnedList] = useState([]);
  const [finesList, setFinesList] = useState([]);
  const [rentMessage, setRentMessage] = useState('');
  const [returnMessage, setReturnMessage] = useState('');

  useEffect(() => {
    fetchNotReturnedList();
    fetchFinesList();
  }, []);

  const rentVideo = (e) => {
    e.preventDefault();
    console.log("hello-f");
    axios
      .post('/api/rent', {
        customerName,
        dateOut,
        dateDueIn,
      })
      .then((response) => {
        setRentMessage(response.data.message);
        resetRentForm();
        fetchNotReturnedList();
      })
      .catch((error) => {
        console.error(error);
        alert('An error occurred. Please try again.');
      });
  };

  const returnVideo = (e) => {
    e.preventDefault();

    axios
      .put('/api/return', {
        customerName,
        returnDate,
      })
      .then((response) => {
        setReturnMessage(response.data.message);
        resetReturnForm();
        fetchNotReturnedList();
      })
      .catch((error) => {
        console.error(error);
        alert('An error occurred. Please try again.');
      });
  };

  const fetchNotReturnedList = () => {
    axios
      .get('/api/not-returned')
      .then((response) => {
        setNotReturnedList(response.data);
      })
      .catch((error) => {
        console.error(error);
        alert('An error occurred. Please try again.');
      });
  };

  const fetchFinesList = () => {
    axios
      .get('/api/fines')
      .then((response) => {
        setFinesList(response.data);
      })
      .catch((error) => {
        console.error(error);
        alert('An error occurred. Please try again.');
      });
  };

  const resetRentForm = () => {
    setCustomerName('');
    setDateOut('');
    setDateDueIn('');
  };

  const resetReturnForm = () => {
    setCustomerName('');
    setReturnDate('');
  };

  return (
    <div>
      <h1>Video Rental System</h1>

      <h2>Rent a Video</h2>
      <form onSubmit={rentVideo}>
        <label htmlFor="customerName">Customer Name:</label>
        <input
          type="text"
          id="customerName"
          value={customerName}
          onChange={(e) => setCustomerName(e.target.value)}
          required
        />

        <label htmlFor="dateOut">Date Out:</label>
        <input
          type="date"
          id="dateOut"
          value={dateOut}
          onChange={(e) => setDateOut(e.target.value)}
          required
        />

        <label htmlFor="dateDueIn">Due Date:</label>
        <input
          type="date"
          id="dateDueIn"
          value={dateDueIn}
          onChange={(e) => setDateDueIn(e.target.value)}
          required
        />

        <button type="submit">Rent Video</button>
      </form>

      {rentMessage && <p>{rentMessage}</p>}

      <h2>Return a Video</h2>
      <form onSubmit={returnVideo}>
        <label htmlFor="customerName">Customer Name:</label>
        <input
          type="text"
          id="customerName"
          value={customerName}
          onChange={(e) => setCustomerName(e.target.value)}
          required
        />

        <label htmlFor="returnDate">Return Date:</label>
        <input
          type="date"
          id="returnDate"
          value={returnDate}
          onChange={(e) => setReturnDate(e.target.value)}
          required
        />

        <button type="submit">Return Video</button>
      </form>

      {returnMessage && <p>{returnMessage}</p>}

      <h2>List of Customers Who Haven't Returned the Video</h2>
      {notReturnedList.length > 0 ? (
        <ul>
          {notReturnedList.map((customer) => (
            <li key={customer.customer_name}>{customer.customer_name}</li>
          ))}
        </ul>
      ) : (
        <p>No customers have outstanding videos.</p>
      )}

      <h2>List of Customers with Fines</h2>
      {finesList.length > 0 ? (
        <ul>
          {finesList.map((customer) => (
            <li key={customer.customer_name}>
              {customer.customer_name} - Fine: {customer.fine}
            </li>
          ))}
        </ul>
      ) : (
        <p>No customers have fines charged.</p>
      )}
    </div>
  );
}

export default App;

