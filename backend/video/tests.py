from django.test import TestCase
from django.urls import reverse
from django.conf import settings
import tempfile
import os
from .models import Video
import shutil
import os

def sample_binary_data_for_test():
    # Define the file path and name
    file_path = "sample_video_chunk.bin"

    # Define the size of the binary data chunk (in bytes)
    chunk_size = 1024  # You can adjust this as needed

    # Generate random binary data
    random_data = os.urandom(chunk_size)

    # Write the data to the binary file
    with open(file_path, "wb") as binary_file:
        binary_file.write(random_data)
    
    return binary_file


class AddDataViewTest(TestCase):
    def setUp(self):
        # Create a Video object for testing
        self.video = Video.objects.create()

        # Create a temporary directory for media storage
        self.media_temp_dir = tempfile.mkdtemp()
        settings.MEDIA_ROOT = self.media_temp_dir

    def tearDown(self):
        # Clean up the temporary media directory after the test
        settings.MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')
        shutil.rmtree(self.media_temp_dir)

    def test_add_data(self):
        # Prepare binary data for testing (e.g., a bytes object)
        test_data = sample_binary_data_for_test()

        # Build the URL for the AddDataView, using the video's ID
        url = reverse('add_data', kwargs={'video_id': str(self.video.video_id)})

        # Simulate a POST request with test data
        response = self.client.post(url, data=test_data, content_type='application/octet-stream')

        # Check if the response is as expected (HTTP status code 200 and a success message)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Data added successfully'})
