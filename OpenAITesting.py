import os
import openai
import csv

def messageCreator(time):
    # Load your API key from an environment variable or secret management service
    openai.api_key = ""
    # The name of the CSV file you want to read and write to
    filename = "phrases.csv"
    phrase = ''
    found = True
    while found:
        found = False
        response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f"using less than 50 characters, write a unique and sweet {time} message", 
        temperature=0.64, 
        max_tokens=50)
        phrase = response.choices[0].text
        phrase = phrase.lstrip()
        # Open the CSV file in read mode
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            
            # Iterate over each row in the CSV file
            for row in reader:
                # If the first column of the row matches the phrase
                if row and row[0] == phrase:
                    found = True
                    # Break out of the loop if the phrase is found
                    break
            # If the phrase was not found in the CSV file
            if not found:
                found = False
                # Open the CSV file in append mode
                with open(filename, 'a', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    # Add a new row with the phrase in the first column
                    writer.writerow([phrase])
                    print("written")
    return phrase
