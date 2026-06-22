import csv
import os
from prompt_generator import generate_prompt
from image_generator import generate_image

output_csv= "F:/promptseller/generated_prompts.csv"

def run_pipeline(theme,count=5):
    print(f"Starting pipeline for theme {theme}\n")

    os.makedirs(os.path.dirname(output_csv),exist_ok=True)

    #step 1 :gpt say prompt generate krwana 
    prompts = generate_prompt(theme,count=count)


    results=[]
    for i ,prompt in enumerate(prompts):
        print(f"\n processing prompt {i+1}/{len(prompt)}---")
        image_url=generate_image(prompt)

        results.append({"prompt":prompt,
                        "image_url":image_url,
                        "theme":theme                        
        })

    file_exits = os.path.exists(output_csv)
    with open(output_csv,"a",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames = ["prompt","image_url","theme"])
        if not file_exits:
            writer.writeheader()
        writer.writerows(results)
    print(f"pipeline completed saved in {output_csv}")
    return results
if __name__ =="__main__":
    theme="cozy autumn landscapes"
    run_pipeline(theme,count=5)