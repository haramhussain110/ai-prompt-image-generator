# AI Prompt & Image Generator

A small automation tool that generates creative AI art prompts using GPT, then turns those prompts into images using OpenAI's image model. Built to explore selling AI-generated prompts and stock art on marketplaces like PromptBase and Etsy.

## What it does

1. Takes a theme (like "cozy autumn landscapes")
2. Uses GPT to generate several unique, detailed prompts for that theme
3. Feeds each prompt into an image generation model to create an image
4. Saves everything (prompt, image data, theme) into a CSV so it's easy to review before listing anywhere

## Files

- `prompt_generator.py` — generates prompts using GPT based on a theme
- `image_generator.py` — generates an image from a single prompt
- `run_pipeline.py` — connects both together and saves results to a CSV
- `generated_prompts.csv` — sample output from a real run

## Built with

- Python
- OpenAI API (GPT for prompts, image generation for art)
- CSV for organizing output

## How to run it

```bash
pip install openai
python run_pipeline.py
```

You'll need your own OpenAI API key set in the script (not included here for security reasons).

## A note on testing

Both `prompt_generator.py` and `image_generator.py` have a `TESTING_MODE` flag. When it's on, the scripts print fake data instead of calling the real API — useful for testing the logic without spending any API credits.

## Why I built this

I wanted to learn how to integrate AI APIs into an automation pipeline, and explore whether AI-generated prompts/art could be sold on marketplaces. While building it, OpenAI deprecated the DALL-E-3 model mid-project, which was a good real-world lesson in handling API changes and debugging unexpected errors. It's mainly a learning and portfolio project — not a guaranteed income source.

---

Built by Haram Hussain while learning Python automation and AI API integration.
