import json
import aiohttp


class StableDiffusionProxy:
    __header = {"Content-Type": "application/json"}
    __payload = lambda self, prompt: json.dumps({
        "key": self.__sd_key,
        "prompt": f"Generate a prompt for a close-up profile portrait of a (({prompt})), focusing on the facial features and eyes. The image should be large enough to clearly show the details of the face and should not include the body",
        "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "safety_checker": "no",
        "enhance_prompt": "yes",
        "seed": None,
        "guidance_scale": 7.5,
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": None,
        "webhook": None,
        "track_id": None
    })

    def __init__(self, sd_key: str):
        self.__sd_key = sd_key

    async def text_to_image(self, prompt: str) -> str:
        async with aiohttp.ClientSession() as session:
            res = await session.post(url="https://stablediffusionapi.com/api/v3/text2img",
                                     data=self.__payload(prompt),
                                     headers=self.__header)
            rg = await res.json()
            if "output" in rg:
                return rg["output"][0]
            else:
                return ""