# Bot Dylan
Best songwriter ever.

## Setup
1. Install [Python 3.7](https://www.python.org/downloads/) (x64 - **important!**).
2. Install [NodeJS](https://nodejs.org/en/).
3. Clone the repository onto your system.
4. Navigate to the repository on your system.

**== Optional but recommended steps:**

Set up the virtual environment.
> `py -m venv env`

Navigate to `env/Scripts` and activate the virtual environment.
> `activate`

**== End of optional steps.**

4. Navigate back to the root directory (`botdylan`) and install required dependencies for the backend.
> `pip install -r requirements.txt`

5. Navigate to the `frontend` directory and install required dependencies for the frontend.
> `npm install`


**If virtual environment is set up, always activate the virtual environment before testing and developing!**

## Running the server
Use a separate terminal to activate each server.

### Activate the backend server
1. Navigate to `backend`.
2. Run the server.
> `py manage.py runserver`

### Activate the frontend server
1. Navigate to `frontend`.
2. Run the server.
> `npm start`

3. Go to http://localhost:3000 on your browser.
