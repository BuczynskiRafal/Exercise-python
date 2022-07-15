def clean_hashtags(input_file: str, output_file: str, length: int):
    with open(input_file, 'r') as file:
        text = file.readlines()
    processing_text = sorted(list(set([word.replace('/n', '') for sublist in text for word in sublist.split() if len(word) <= length+1])))
    with open(output_file, 'w') as file:
        for hashtag in processing_text:
            file.write(hashtag + '\n')


input_file = 'hashtags.txt'
output_file = 'process_hashtags.txt'
print(clean_hashtags(input_file, output_file, length=5))
