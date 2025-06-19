# Firestore Python CRUD Example

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations and search functionality using Google Firestore with Python.

## Features
- Create, read, update, and delete user documents
- List all users
- Search users by field
- Delete all users in the collection

## Requirements
- Python 3.8+
- Google Cloud credentials with Firestore access
- `firebase-admin` and `google-cloud-firestore` Python packages
- [uv](https://github.com/astral-sh/uv) package manager

## Setup
1. Install dependencies using [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install firebase-admin google-cloud-firestore
   ```
2. Set up your Google Cloud credentials (e.g., set `GOOGLE_APPLICATION_CREDENTIALS` environment variable).
3. Update the Firestore `database_id` in `main.py` if needed.

## Usage
Run the main script:
```bash
python main.py
```

The script will:
- Delete all users
- Add several example users
- List users
- Read, update, and delete users
- Search users by a field

## Example Code
See `main.py` for all CRUD and search functions:
- `create_user(user_id, user_data)`
- `read_user(user_id)`
- `update_user(user_id, update_data)`
- `delete_user(user_id)`
- `list_users()`
- `search_users_by_field(field, value)`
- `delete_all_users()`

---

**Note:** This is a simple example for educational purposes. For production, handle errors and authentication securely.
