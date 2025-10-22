import emoji

def main():
    prompt = input("Input: ")
    e = emoji.emojize(f'Output: {prompt}', language='alias')
  

if __name__ == "__main__":
    main()