from text_recognition.test.util import get_client, get_image

if __name__ == '__main__':
    client = get_client()

    # Base 64 text
    # img = "./label_1_b64.txt"
    # image = get_image_b64(img)

    # Image File
    img = "/Users/frankjia/Desktop/Programming/FoodScan-Test/test_assets/images_ingredients/ingredients_9.jpg"
    image = get_image(img)
    print(client.detect_b64(image).text)