import textwrap
import os
import re
from time import time,sleep


def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()

def save_file(data, filename, output_dir='.'):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write(data)
		
def main():
    alltext = open_file('input.txt')
    
    # Split the text into chunks that end with a complete sentence
    max_chunk_size = 4000
    sentences = re.findall('[^.!?]+[.!?]', alltext)
    current_chunk_size = 0
    chunks = []
    chunk_counter = 1
    for sentence in sentences:
        sentence_size = len(sentence)
        if current_chunk_size + sentence_size <= max_chunk_size:
            chunks.append(sentence)
            current_chunk_size += sentence_size
        else:
            # Save the current chunk to a file in the output directory
            save_file("".join(chunks), f"output_{chunk_counter}.txt", output_dir='output_chunked')
            chunks = [sentence]
            current_chunk_size = sentence_size
            chunk_counter += 1
        print("Chunk:", sentence)
    
    # Save the last chunk to a file in the output directory
    save_file("".join(chunks), f"output_{chunk_counter}.txt", output_dir='output_chunked')


if __name__ == '__main__':
     main()