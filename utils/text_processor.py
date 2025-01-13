import re


def clean_raw_content(raw_content):
    cleaned_content = re.sub(r'[-\n]+', ' ', raw_content).strip()
    words = cleaned_content.split()
    trimmed_content = words[5000:len(words) - 12000] if len(words) > 17000 else words[5000:]
    return ' '.join(trimmed_content)


def split_content_into_chunks(content, n=150):
    words = content.split()
    return [' '.join(words[i:i + n]) for i in range(0, len(words), n)]
