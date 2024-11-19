class FormatedText:
    @staticmethod
    def formatMarkdownV2(text: str) -> str:
        if not isinstance(text, str):
            raise TypeError(f"Invalid type: {type(text)}. Expected str.")
        if not text:
            return text
        
        replacements = {
            '_': r'\_', '[': r'\[', ']': r'\]', '(': r'\(', ')': r'\)',
            '~': r'\~', '`': r'\`', '>': r'\>', '#': r'\#', '+': r'\+',
            '-': r'\-', '=': r'\=', '|': r'\|', '{': r'\{', '}': r'\}',
            '.': r'\.', '!': r'\!'
        }
        
        for symbol, replacement in replacements.items():
            text = text.replace(symbol, replacement)
    
        return text