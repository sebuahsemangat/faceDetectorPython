import openai
import pyautogui
openai.api_key = "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"

tema = input("Masukkan tema: ")
inputPrompt = "Buatkan puisi dengan tema '" + tema + "'"
response = openai.Completion.create(
 model="text-davinci-003",
 prompt= inputPrompt,
 temperature=0.7,
 max_tokens=256,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0
)
print(response.choices[0].text)