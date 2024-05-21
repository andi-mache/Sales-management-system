import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

fixture_path = 'sms.json'
encoding = detect_encoding(fixture_path)
print(f'Detected encoding: {encoding}')
