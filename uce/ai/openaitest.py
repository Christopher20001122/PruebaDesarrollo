import openai
import os
from pydantic import BaseModel

openai.organization = 'org-PYELIbA8LxpnGFiTsMHVkbOV'
openai.api_key = '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'

class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:

    print('[PROCESAafsfdfNDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages= [
            {"role": "system", "content": """Eres un contador del número de vocales, genera una respuesta en la cual se cuenten solo las vocales para cualquier palabra que se te proporcione
            E.G: Bienvenido
            -Esta palabra cuenta con 5 vocales """},
            {"role": "user", "content": prompt}
        ]
    )


    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]