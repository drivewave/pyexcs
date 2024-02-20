from openai import OpenAI
from colorama import Fore, Style

class Pyexcs:
    
    def __init__(self, api_key, lang):
        self.api_key = api_key
        self.lang = lang

    def return_solution(self, e):
        print(f'{Fore.RED}Error:{Style.RESET_ALL} {e}')
        client = OpenAI(api_key=self.api_key)
        rules = f'What does this error mean?\n\n{str(e)}\n\n Explain in: {self.lang} without line breaks.'
        translation = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "system", "content": rules}])
        r = ''      
        for choice in translation.choices:
            r += choice.message.content
        print(f'{Fore.YELLOW}Solution:{Style.RESET_ALL} {r}')

    def handle_errors(self, func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                self.return_solution(e)
        return wrapper