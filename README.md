SeatSync-Seat-Booking-System-
The SeatSync Seat Booking System is a web-based application developed using the Flask framework in Python, designed to provide a simple and efficient solution for managing seat reservations. This project simulates real-world booking systems such as movie ticket booking, bus reservations, or event seating, where users can view seat availability 🎟️ SeatSync – Seat Booking System the code has being given in python.py file

📌 Overview

SeatSync is a simple and efficient web-based seat booking system built using Flask (Python). It allows users to register, log in, and book available seats through an interactive and visually appealing interface. The project demonstrates core web development concepts such as authentication, session management, and dynamic UI rendering.

🚀 Features

👤 User Registration & Login
🔐 Secure Password Hashing (SHA-256)
💺 Real-Time Seat Availability Display
🎟️ Book & Cancel Seats
🛑 Prevents Double Booking
👑 Admin Privileges (cancel any seat)
🎨 Stylish UI with colors and animations
📱 Mobile-friendly interface
🛠️ Tech Stack

Backend: Python, Flask
Frontend: HTML, CSS
Database: JSON (file-based storage)
📂 Project Structure

SeatSync/ │── app.py # Main Flask application │── data.json # Database (auto-created) │── README.md # Project documentation

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/seatsync.git cd seatsync

2️⃣ Install Dependencies

pip install flask

3️⃣ Run the Application

python app.py

4️⃣ Open in Browser

http://127.0.0.1:5000/login

👉 For Cloud/Mobile:

app.run(host="0.0.0.0", port=5000, debug=True)

🔑 Default Admin Login

Username: admin Password: admin123

💡 How It Works

Users register and log in securely
Seats are displayed with color codes:
🟢 Green → Available
🔴 Red → Booked
🟡 Yellow → Your seat
Clicking a seat books it instantly
Users can cancel their own bookings
Admin can cancel any booking
📸 Screenshots

(Add screenshots here after running the project)

🔮 Future Enhancements

🌐 Deploy online (Heroku / Render)
📱 Fully responsive mobile UI
⚡ Real-time updates (AJAX/WebSockets)
🎫 Multiple seat booking per user
💳 Payment integration
🤝 Contributing

Feel free to fork this repository and contribute improvements!

📄 License

This project is open-source and available under the MIT License.
