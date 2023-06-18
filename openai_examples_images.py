import os
import openai

from io import BytesIO
from PIL import Image

from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

def basic_prompt_img_input() -> str:
    """
    Generates an image based on user input using OpenAI's image generation API.

    Returns:
        str: URL of the generated image.

    Raises:
        ValueError: If the value of 'n' is not between 1 and 10 (inclusive).
        ValueError: If the value of 'size' is not 1, 2, or 3.
        openai.error.OpenAIError: If an error occurs during the API request.
        KeyboardInterrupt: If the execution is interrupted by the user.
        Exception: If any other unexpected error occurs during the API request.

    Usage:
        - Prompts the user to enter a number between 1 and 10 as 'n' for number of images to create.
        - Prompts the user to enter a size option: 1 for 256x256, 2 for 512x512, or 3 for 1024x1024.
        - Prompts the user to enter a custom prompt.
        - Calls the OpenAI image generation API with the provided input.
        - Returns the URL of the generated image.

    Example:
        >>> basic_prompt_img_input()
        Enter a number between 1 and 10: 5
        Enter size (1-256x256; 2-512x512; 3-1024x1024): 2
        Enter your prompt: "A beautiful sunset over the ocean"
        'https://generated-image-url.com/abc123'
    """

    n: int = int(input("Enter the number of images to create (between 1 and 10): "))
    if not 1 <= n <= 10:
        raise ValueError("Invalid value for 'n'. Must be between 1 and 10 (inclusive).")
    
    size: int = int(input("Enter size (1-256x256; 2-512x512; 3-1024x1024): "))
    valid_sizes = {"256x256", "512x512", "1024x1024"}
    if size not in (1, 2, 3):
        raise ValueError("Invalid value for 'size'. Must be 1, 2, or 3.")
    
    prompt: str = input("Enter your prompt: ")

    try:
        response: dict = openai.Image.create(
            prompt = prompt,
            n = n,
            size = valid_sizes[size]
        )
        image_url: str = response['data'][0]['url']
        return image_url
    
    except openai.error.OpenAIError as e:
        return e.http_status, e.error
    
    except KeyboardInterrupt as e:
        return e.error
    
    except Exception as e:
        return e.error


def basic_prompt_img(n: int = 1, size: str = "1024x1024") -> str:
    """
    Generates an image using OpenAI's image prompt API.

    Args:
        n (int, optional): Number of images to generate. Must be between 1 and 10 (inclusive). Defaults to 1.
        size (str, optional): Size of the generated image. Must be one of "256x256", "512x512", or "1024x1024". Defaults to "1024x1024".

    Returns:
        str: URL of the generated image.

    Raises:
        ValueError: If the value of `n` is not between 1 and 10 (inclusive).
        ValueError: If the value of `size` is not one of "256x256", "512x512", or "1024x1024".
        openai.error.OpenAIError: If an error occurs during the API request.
        KeyboardInterrupt: If the execution is interrupted by the user.
        Exception: If any other unexpected error occurs during the API request.

    Usage:
        - Enter your desired prompt when prompted.
        - The function will generate an image based on the prompt using OpenAI's image prompt API.
        - The URL of the generated image will be returned.

    Example:
        >>> basic_prompt_img(n=3, size="512x512")
        Enter your prompt: "A colorful sunset over a calm lake"
        'https://generated-image-url.com/abc123'
    """

    if not 1 <= n <= 10:
        raise ValueError("Invalid value for 'n'. Must be between 1 and 10 (inclusive).")
    
    valid_sizes = {"256x256", "512x512", "1024x1024"}
    if size not in valid_sizes:
        raise ValueError("Invalid value for 'size'. Must be one of '256x256', '512x512', or '1024x1024'.")
    
    prompt: str = input("Enter your prompt: ")

    try:
        response: dict = openai.Image.create(
            prompt = prompt,
            n = n,
            size = size
        )
        image_url: str = response['data'][0]['url']
        return image_url
    
    except openai.error.OpenAIError as e:
        return e.http_status, e.error
    
    except KeyboardInterrupt as e:
        return e.error
    
    except Exception as e:
        return e.error


def basic_mask_img(n: int = 1, size: str = "1024x1024") -> str:
    """
    Generates an edited image using OpenAI's image editing API.

    Args:
        n (int, optional): Number of edited images to generate. Must be between 1 and 10 (inclusive). Defaults to 1.
        size (str, optional): Size of the generated image. Must be one of "256x256", "512x512", or "1024x1024". Defaults to "1024x1024".

    Returns:
        str: URL of the generated edited image.

    Raises:
        ValueError: If the value of `n` is not between 1 and 10 (inclusive).
        ValueError: If the value of `size` is not one of "256x256", "512x512", or "1024x1024".
        openai.error.OpenAIError: If an error occurs during the API request.
        KeyboardInterrupt: If the execution is interrupted by the user.
        Exception: If any other unexpected error occurs during the API request.

    Usage:
        - When prompted, you can either provide a custom prompt or enter "default" to use a predefined prompt and image/mask paths.
        - If you enter "default" as the prompt, the function will use a predefined prompt, image path, and mask path.
        - If you enter a custom prompt, you will be prompted to enter the image path and the mask path.
        - The function will generate an edited image based on the prompt, image, and mask using OpenAI's image editing API.
        - The URL of the generated edited image will be returned.

    Example:
        >>> basic_mask_img(n=3, size="512x512")
        Enter your prompt: "A beautiful landscape with mountains"
        Enter image path: "images/mountatin_landscape.jpg"
        Enter mask path: "images/mask.jpg"
        'https://generated-edited-image-url.com/abc123'
    """

    if not 1 <= n <= 10:
        raise ValueError("Invalid value for 'n'. Must be between 1 and 10 (inclusive).")
    
    valid_sizes = {"256x256", "512x512", "1024x1024"}
    if size not in valid_sizes:
        raise ValueError("Invalid value for 'size'. Must be one of '256x256', '512x512', or '1024x1024'.")

    prompt: str = input("Enter your prompt: ")
    
    if prompt.lower == "default":
        prompt: str = "A sunlit indoor lounge area with a pool containing a flamingo"
        link_img: str = "images/sunlit_lounge.png"
        link_mask: str = "images/mask.png"

    else:
        link_img: str = input("Enter image path")
        link_mask: str = input("Enter mask path")

    try:
        response: dict = openai.Image.create_edit(
            image = open(link_img, "rb"),
            mask = open(link_mask, "rb"),
            prompt = prompt,
            n = n,
            size = size
        )
        image_url: str = response['data'][0]['url']
        return image_url
    
    except openai.error.OpenAIError as e:
        return e.http_status, e.error
    
    except KeyboardInterrupt as e:
        return e.error
    
    except Exception as e:
        return e.error


def basic_variation_img(img_path: str = "images/corgi_and_cat_paw.png", n: int = 1, size: str = "1024x1024") -> str:
    """
    Generates a variation of an image using OpenAI's image variation API.

    Args:
        img_path (str, optional): Path to the image file. Defaults to "images/corgi_and_cat_paw.png".
        n (int, optional): Number of image variations to generate. Must be between 1 and 10 (inclusive). Defaults to 1.
        size (str, optional): Size of the generated image. Must be one of "256x256", "512x512", or "1024x1024". Defaults to "1024x1024".

    Returns:
        str: URL of the generated image.

    Raises:
        ValueError: If the value of `n` is not between 1 and 10 (inclusive).
        ValueError: If the value of `size` is not one of "256x256", "512x512", or "1024x1024".
        openai.error.OpenAIError: If an error occurs during the API request.
        KeyboardInterrupt: If the execution is interrupted by the user.
        Exception: If any other unexpected error occurs during the API request.


    Usage:
        - Provide the path to the image file (or use the default path).
        - Specify the number of variations to generate (`n`) and the size of the variations (`size`).
        - The function will generate image variations based on the provided image using OpenAI's image variation API.
        - The URL of the generated image will be returned.

    Example:
        >>> basic_variation_img(img_path="images/dog.jpg", n=3, size="512x512")
        'https://generated-image-url.com/abc123'
    """

    if not 1 <= n <= 10:
        raise ValueError("Invalid value for 'n'. Must be between 1 and 10 (inclusive).")
    
    valid_sizes = {"256x256", "512x512", "1024x1024"}
    if size not in valid_sizes:
        raise ValueError("Invalid value for 'size'. Must be one of '256x256', '512x512', or '1024x1024'.")

    try:
        response: dict = openai.Image.create_variation(
            image = open(img_path, "rb"),
            n = n,
            size = size
        )
        image_url: str = response['data'][0]['url']
        return image_url
    
    except openai.error.OpenAIError as e:
        return e.http_status, e.error
    
    except KeyboardInterrupt as e:
        return e.error
    
    except Exception as e:
        return e.error


def basic_variation_in_mem_img(byte_stream: BytesIO, n: int = 1, size: str = "1024x1024") -> str:
    """
    Generates a variation of an image using OpenAI's image editing API.

    Args:
        img_data (BytesIO): BytesIO object containing the image data.

    Returns:
        str: URL of the generated variation image.

    Raises:
        openai.error.OpenAIError: If an error occurs during the API request.
        ValueError: If `img_data` is None or does not contain valid image data.
        Exception: If any other unexpected error occurs during the API request.

    Usage:
        - Provide a BytesIO object containing the image data.
        - Calls the OpenAI image editing API with the provided image data.
        - Returns the URL of the generated variation image.

    Example:
        >>> img_data = BytesIO(some_image_bytes)
        >>> basic_variation_in_mem_img(img_data)
        'https://generated-variation-image-url.com/abc123'
    """

    try:
        if byte_stream is None or not isinstance(byte_stream, BytesIO):
            raise ValueError("Invalid value for 'img_data'. Must provide a BytesIO object.")

        byte_array = byte_stream.getvalue()
        response = openai.Image.create_variation(
            image = byte_array,
            n = n,
            size = size
        )

        image_url: str = response['data'][0]['url']
        return image_url

    except openai.error.OpenAIError as e:
        return e.http_status, e.error

    except Exception as e:
        return e
    

def basic_operation_img(png_path: str = "images\logo_openai.png", n: int = 1, size: str = "1024x1024") -> str:
    # Operating on image data


    # Read the image file from disk and resize it
    image = Image.open(png_path)
    width, height = 256, 256
    image = image.resize((width, height))

    # Convert the image to a BytesIO object
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()

    try:
        response = openai.Image.create_variation(
            image=byte_array,
            n=n,
            size=size
        )

        image_url: str = response['data'][0]['url']
        return image_url

    except openai.error.OpenAIError as e:
        return e.http_status, e.error

    except Exception as e:
        return e

if __name__ == '__main__':
    # basic_prompt_img_input()
    # basic_prompt_img()
    # basic_mask_img()
    # basic_variation_img()
    # basic_variation_in_mem_img(byte_stream=)
    # basic_operation_img()
