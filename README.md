# RERA Authentication System

This project is a separate authentication system for verifying RERA IDs using the Surepass API. It consists of a frontend built with HTML, CSS, and JavaScript and a backend implemented using Flask.

## Features
- Verify RERA ID using the Surepass API
- User-friendly and stylish UI
- Backend validation with Flask
- Handles errors and invalid RERA IDs gracefully

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- Flask
- Flask-CORS (for handling cross-origin requests)
- A Surepass API key

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/aryanrbenakatti/RERA-authentication-system.git
   ```

2. **Install dependencies:**
   ```sh
   pip install flask flask-cors requests
   ```

3. **Configure API Key:**
   - Open `server.py`
   - Replace `YOUR_SUREPASS_API_KEY` with your actual API key

## Running the Project
### Start the Backend
```sh
python server.py
```
By default, the backend runs on `http://127.0.0.1:5000/`

### Start the Frontend
Simply open `index.html` in a browser.

## API Endpoints
### `POST /verify_rera`
#### Request:
```json
{
  "rera_id": "RERA123456"
}
```
#### Response (Valid ID):
```json
{
  "verified": true,
  "details": { "name": "ABC Builders", "state": "Maharashtra" }
}
```
#### Response (Invalid ID):
```json
{
  "verified": false,
  "message": "Invalid RERA ID"
}
```

## Troubleshooting
1. **Not Found Error (404)**
   - Ensure `server.py` is running.
   - Check if the API route is correct (`/verify_rera`).
   - Verify that the frontend's `fetch` URL matches the backend.

2. **CORS Issues**
   - Ensure Flask-CORS is installed and enabled in `server.py`:
     ```python
     from flask_cors import CORS
     CORS(app)
     ```

3. **Invalid API Key**
   - Double-check the Surepass API key in `server.py`.

## Future Enhancements
- Add authentication for users
- Store verification history
- Support additional states

## License
This project is open-source and free to use.

