# -*- coding: utf-8 -*-
import re

def escape_markdown_v2(text: str) -> str:
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    escaped_text = text
    for char in special_chars:
        escaped_text = escaped_text.replace(char, f'\\{char}')
    return escaped_text

def escape_markdown_data(data: dict) -> dict:
    return {
        k: escape_markdown_v2(str(v)) if k != 'image_file_id' else v 
        for k, v in data.items()
    }

def format_and_escape_markdown(template: str, **kwargs) -> str:
    formatted_text = template.format(**kwargs)
    return escape_markdown_v2(formatted_text)

def escape_html(text: str) -> str:
    if text is None:
        return ""
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def to_html(text: str) -> str:
    if text is None:
        return ""
    text = escape_html(text)
    text = re.sub(r'\*(.*?)\*', r'<b>\1</b>', text)
    text = re.sub(r'_(.*?)_', r'<i>\1</i>', text)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    return text

import re

def escape_html(text: str) -> str:
    if text is None:
        return ""
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def format_html(template: str, **kwargs) -> str:
    try:
        escaped_kwargs = {
            k: escape_html(str(v)) if isinstance(v, (str, int, float)) and k != 'image_file_id' else v 
            for k, v in kwargs.items()
        }
        
        formatted_text = template.format(**escaped_kwargs)
        
        formatted_text = re.sub(r'\*(.*?)\*', r'<b>\1</b>', formatted_text)
        formatted_text = re.sub(r'_(.*?)_', r'<i>\1</i>', formatted_text)
        formatted_text = re.sub(r'`(.*?)`', r'<code>\1</code>', formatted_text)
        
        return formatted_text
    except Exception as e:
        print(f"Error in format_html: {e}")
        return template