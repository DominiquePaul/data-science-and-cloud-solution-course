"""
1. Enable the cloud vision API in your cloud console
2. Install the python packages: pip install google-cloud-vision
3. Create new credentials for your application if you have not done so already
    https://console.cloud.google.com/apis/credentials
    https://cloud.google.com/natural-language/docs/how-to

Another useful tutorial
https://codelabs.developers.google.com/codelabs/cloud-vision-api-python/index.html?index=..%2F..index#0
"""
import os
import io
from google.cloud import vision


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/dominiquepaul/Google Drive/DSCS/dscs-unisg-6bdaad1e2ab3.json"

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

image_uri = 'https://rail.cc/photo/location/13309828843f3998b0b8d90a2d94a3541c015b0350_eins.jpg'
detect_labels_uri(image_uri)


def detect_text(uri):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()


    ### for reading files from disk ###
    # with io.open(path, 'rb') as image_file:
    #     content = image_file.read()
    # image = vision.types.Image(content=content)

    ### for reading files from a link ####
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


image_uri = "https://altoona.psu.edu/sites/default/files/styles/photo_gallery_large/http/news.psu.edu/sites/default/files/success-word-cloud.jpg?itok=4_HTmhRg+"
detect_text(image_uri)


"""
Your turn:

1. Come up with three realistic use cases in a simple app, where image
    annotation might be useful.
2. Get labels of an image of your choice using the vision API
3. Modify the functions that instead of printing the labels, they are returned
    when you call the function. Do this for the labels and the text detection
4. Modify your function again, that only the top label is return as a string.
5. Use an image that you have saved on your computer locally. You will need
    to read in the file in a binary format.
5. Now use the Landmark and logo detection API for two different images
    respectively. Write the functions in a way that they take a link as an input
    and return the landmarks/logos names as labels.
6. Add a page to your flask website. The webpage should contain a form where the
    user can enter a link to an image. When the form is submitted a text field
    below shows what is expected to be in the image. Have a look at the code in
    folder one for creating such a page with a form and 'dynamic' content
"""
