# Video Recording API Documentation

This documentation provides details about the endpoints available in the Video Recording API.

## Base URL

The base URL for all API endpoints is `https://example.com/api/`.

## Endpoints

### List Video Recordings

- **URL**: `/api/videos/`
- **HTTP Method**: GET
- **Description**: Retrieve a list of all video recordings.
- **Response**: JSON object containing a list of video recording records.

### Create a Video Recording

- **URL**: `/api/videos/`
- **HTTP Method**: POST
- **Description**: Upload a new video recording.
- **Request**: Send a POST request with video data.
- **Response**: JSON object confirming the successful upload.

### Retrieve a Video Recording

- **URL**: `/api/videos/{pk}/`
- **HTTP Method**: GET
- **Description**: Retrieve details of a specific video recording.
- **Parameters**:
  - `{pk}` (Path Parameter): The unique identifier of the video recording.
- **Response**: JSON object containing the details of the requested video recording.

### Update a Video Recording

- **URL**: `/api/videos/{pk}/`
- **HTTP Method**: PUT or PATCH
- **Description**: Update the details of a specific video recording.
- **Parameters**:
  - `{pk}` (Path Parameter): The unique identifier of the video recording.
- **Request**: Send a PUT or PATCH request with updated video data.
- **Response**: JSON object confirming the successful update.

### Delete a Video Recording

- **URL**: `/api/videos/{pk}/`
- **HTTP Method**: DELETE
- **Description**: Delete a specific video recording.
- **Parameters**:
  - `{pk}` (Path Parameter): The unique identifier of the video recording.
- **Response**: JSON object confirming the successful deletion.

## Additional Formats

You can request API responses in different formats (e.g., JSON) by specifying the format in the URL. Here are the URL patterns for different formats:

- JSON Format: `/api/videos.json`

---
