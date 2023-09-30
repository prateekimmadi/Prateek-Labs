import random

class Random_Generator:
    def __init__(self, max_sequence_length):
        self.max_sequence_length = max_sequence_length
        self.sequence = []

    def generate_next_sequence_item(self):
        next_item = random.randint(1, 4)  # Assuming there are 4 colors (1 to 4)
        self.sequence.append(next_item)
        return next_item

    def generate_full_sequence(self):
        self.sequence = [random.randint(1, 4) for _ in range(self.max_sequence_length)]
        return self.sequence

    def get_sequence(self):
        return self.sequence

    def clear_sequence(self):
        self.sequence = []

# Example usage:
if __name__ == "__main__":
    # Create a Random_Generator with a maximum sequence length of 8
    Random_Generator= Random_Generator(max_sequence_length=8)

    # Generate a random sequence of length 8
    sequence = Random_Generator.generate_full_sequence()
    print("Random Sequence:", sequence)

    # Add the next item to the sequence
    next_item = Random_Generator.generate_next_sequence_item()
    print("Next Item:", next_item)

    # Get the current sequence
    current_sequence = Random_Generator.get_sequence()
    print("Current Sequence:", current_sequence)

    # Clear the sequence
    Random_Generator.clear_sequence()
    print("Cleared Sequence:", Random_Generator.get_sequence())
