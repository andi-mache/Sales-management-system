import codecs
fixture_path = 'sms.json'
def convert_to_utf8(input_file, output_file, original_encoding):
    with codecs.open(input_file, 'r', original_encoding) as file_in:
        with codecs.open(output_file, 'w', 'utf-8') as file_out:
            file_out.write(file_in.read())

fixture_path_utf8 = 'sms_utf8.json'
encoding = 'utf-16'
convert_to_utf8(fixture_path, fixture_path_utf8, encoding)
