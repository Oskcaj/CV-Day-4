import requests
import os

def download_image():
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # URL of the image (using a placeholder Superman with glasses image URL)
    image_url = "https://raw.githubusercontent.com/your-username/your-repo/main/images/superman_glasses.jpg"
    
    try:
        # Send a GET request to the URL
        response = requests.get(image_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the image
            with open('images/superman_glasses.jpg', 'wb') as f:
                f.write(response.content)
            print("Image successfully downloaded!")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_image() 