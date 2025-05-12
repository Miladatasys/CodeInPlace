from ai import call_gpt

def main():
    """
    We prompt the user to input their name, a topic
    and then to wait the call_gpt function we print a message. 
    """
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    
    response = call_gpt(f"Create a haiku with {name} and {topic}")
    print(response)
    

if __name__ == "__main__":
    main()

"""
The input was so nice:
% python main.py
Enter your name: Mila
Enter a topic: Music
Creating your haiku...
Mila's laughter flows,  
Notes dance upon the soft breeze,  
Heartbeats sync with song.  
"""