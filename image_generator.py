from openai import OpenAI
client = OpenAI(api_key="you_api_key")
TESTING_MODE = True
def generate_image(prompt):
        if TESTING_MODE:
        #fake reponse without cost ,just for checking 
            print(f"[Test Mode]:{prompt}")
            fake_url="https://fake-test-url.com/image.png"
            print(f"[TEST MODE] fake image url :{fake_url}")
            return fake_url

                    #real api key use first off testing mode
        response = client.images.generate(
            model="gpt-image-1",
            prompt = prompt,
            size="1024x1024",
            quality="medium",
            n=1
            )
        image_url = response.data[0].url
        print(f" Real image Generated :{image_url}")
        return image_url
if __name__==  "__main__":
    test_prompt = "A cozy cabin in the mountains during golden hour, digital art style"
    generate_image(test_prompt)    