# Video Recording API Documentation

This documentation provides details about the endpoints available in the Video Recording API.

## Base URL

The base URL for all API endpoints is `http://archiflow.pythonanywhere.com/`.

## Endpoints

## Create Video

- **Endpoint:** `/create/`
- **HTTP Method:** POST
- **Description:** Start a new video recording session and obtain a unique video ID for the session.
- **Request Body:** None
- **Response:**
  - Status Code: 200 OK
  - Body: JSON Object
    - `video_id` (string): Unique ID for the newly created video session.

## Add Data to Video

- **Endpoint:** `/add_data/<uuid:video_id>/`
- **HTTP Method:** POST
- **Description:** Continuously send video data in chunks to an existing video recording session.
- **URL Parameter:**
  - `video_id` (UUID): Unique ID of the video recording session.
- **Request Body:** Binary video data chunk.
- **Response:**
  - Status Code: 200 OK
  - Body: JSON Object
    - `message` (string): Confirmation message.

## Complete Job

- **Endpoint:** `/complete_job/<uuid:video_id>/`
- **HTTP Method:** POST
- **Description:** Signal the completion of a video recording session and initiate processing.
- **URL Parameter:**
  - `video_id` (UUID): Unique ID of the video recording session.
- **Request Body:** None
- **Response:**
  - Status Code: 200 OK
  - Body: JSON Object
    - `message` (string): Confirmation message.

## Check Video Status

- **Endpoint:** `/check_status/<uuid:video_id>/`
- **HTTP Method:** GET
- **Description:** Retrieve the current status of a video recording session.
- **URL Parameter:**
  - `video_id` (UUID): Unique ID of the video recording session.
- **Response:**
  - Status Code: 200 OK
  - Body: JSON Object
    - `status` (string): Current status of the video (e.g., 'recording', 'processing', 'complete').

## Get Videos

- **Endpoint:** `/video/<uuid:video_id>/`
- **HTTP Method:** GET
- **Description:** Retrieve a list of video files stored in the specified directory.
- **Request Body:** None
- **Response:**
  - Status Code: 200 OK
  - Body: JSON Object
    - `completed_videos` (array of strings): List of completed video file names.

---
