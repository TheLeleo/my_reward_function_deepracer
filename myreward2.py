def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params["all_wheels_on_track"]
    is_crashed = params["is_crashed"]
    progress = params["progress"]
    speed = params["speed"]
    abs_steering = abs(params['steering_angle']) 
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    reward = 1
    if all_wheels_on_track:
        reward = reward * 2
    else:
        reward = reward / 2

    if distance_from_center <= marker_1:
        reward = reward * 2.4
    elif distance_from_center <= marker_2:
        reward = reward * 1.4
    elif distance_from_center <= marker_3:
        reward = reward * 1.1
    else:
        reward = reward * 1e-3  
    
    
    reward = reward * (speed * 2)
    reward = reward * (progress)

    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    if is_crashed:
        reward = reward - 100
    
    return float(reward)




