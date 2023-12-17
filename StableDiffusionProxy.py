import json
import aiohttp


class StableDiffusionProxy:
    header = {"Content-Type": "application/json"}
    payload = lambda self, prompt, sd_key: json.dumps({
        "key": sd_key,
        "model_id": "midjourney",
        "prompt": f"Generate a prompt for a close-up profile portrait of a (({prompt})), focusing on the facial features and eyes. The image should be large enough to clearly show the details of the face and should not include the body",
        "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "30",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "multi_lingual": "yes",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": None,
        "webhook": None,
        "track_id": None
    })

    def __init__(self, sd_key):
        self.sd_key = sd_key

    async def text_to_image(self, prompt):
        async with aiohttp.ClientSession() as session:
            res = await session.post(url="https://stablediffusionapi.com/api/v4/dreambooth",
                                     data=self.payload(prompt[1:], self.sd_key),
                                     headers=self.header)
            rg = await res.json()
            if "future_links" in rg:
                return rg["future_links"][0]
            elif 'proxy_links' in rg:
                return rg['proxy_links'][0]
            else:
                return None