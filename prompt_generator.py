from openai import OpenAI 
client = OpenAI(api_key="your_api_key_input_here")
TESTING_MODE   = True

def generate_prompt(theme,count=1):
    if TESTING_MODE:
        print(f"[TEST MODE ]: {theme},count :{count}")
        fake_prompts = [
            f"{i+1} about {theme}  "for i in range(count)]
        
        for p in fake_prompts:
            print(f"-{p}")
        return fake_prompts
    

    response =client.chat.completions.create(
        model = "gpt-4o-mini",
        messages =[
            {
                 "role": "user",
                "content": f"""Generate {count} unique, creative AI image generation prompts related to "{theme}".
Each prompt should be detailed (style, lighting, mood) and suitable for selling as stock AI art.
Return ONLY the prompts, one per line, no numbering, no extra text."""
            }
        ]
                                            
    )
    test = response.choices[0].message.content 
    prompts = [line.strip() for line in test.split("\n")if line.strip()]

    print(f"Generated {len(prompts)}prompts")
    for p in prompts:
        print(f"-{p}")
    
    return prompts
if __name__ == "__main__":
    theme ="cozy autumn landscapes"
    generate_prompt(theme,count=5)  