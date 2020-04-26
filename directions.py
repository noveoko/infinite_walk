import random 


directions = {
    'north': {'direction':(1, 0), 'if_repeat' :[0.5, 0.05, 0.235,0.235]},
    'south': {'direction':(-1, 0), 'if_repeat' :[0.05,0.5,0.235, 0.235]},
    'east':  {'direction':(0, 1), 'if_repeat' :[0.235,0.235, 0.5,0.05]},
    'west':  {'direction':(0, -1), 'if_repeat' :[0.235,0.235,0.05,0.5]}
    }

def distance_to_travel():
    '''return a distance to travel using a probability distribution'''
    distances = [0,1,2,3,4,5]
    probabilities = [0.1,0.5,0.1,0.2,0.1,0.05]
    return random.choices(distances, probabilities).pop()


def direction(previous_direction=None, return_value='direction'):
    '''return a direction using previous direction as a driver of next direction'''
    
    probability = [0.25,0.25,0.25,0.25]

    if return_value == 'direction':
        dirs = [v['direction'] for k,v in directions.items()]
        choice = None
        if previous_direction:
            dir_probs = directions[previous_direction]['if_repeat']
            choice = random.choices(dirs, dir_probs)
        else:
            choice = random.choices(dirs, probability)
        return choice
    elif return_value == 'number_to_dir':
        return {str(v['direction']):k for k,v in directions.items()}
 

def random_walk(total_steps=100):
    number_to_direction = direction(return_value='number_to_dir')
    steps = []
    for i in range(0,total_steps):
        distance = distance_to_travel()
        if not steps:
            steps.append(direction())
        elif steps[-1]:
            last_step = str(steps[-1][0])
            previous_dir = number_to_direction[last_step]
            this_direction = direction(previous_direction=previous_dir)
            [steps.append(this_direction) for a in range(0, distance)]

    return [a[0] for a in steps]