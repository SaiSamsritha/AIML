colors = ['red', 'blue', 'green', 'yellow', 'black']
states = ['telangana', 'karnataka', 'tamilnadu', 'kerala']
neighbors = {
    'telangana': ['karnataka', 'tamilnadu'],
    'karnataka': ['telangana', 'tamilnadu', 'kerala'],
    'kerala': ['karnataka', 'tamilnadu'],
    'tamilnadu': ['telangana', 'karnataka', 'kerala']
}

colors_of_states = {}
def promising(state, color):
    for neighbor in neighbors.get(state, []):
        if colors_of_states.get(neighbor) == color:
            return False
    return True
def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color
    return None 
def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)
main()
