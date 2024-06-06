# Define thresholds
POSITIVE_THRESHOLD = 2  # seconds
NEGATIVE_THRESHOLD = 2  # seconds

# Define engagement criteria
ENGAGEMENT_CRITERIA = {
    'road_focus': {'positive': True, 'threshold': None},
    'mirror_check': {'positive': True, 'threshold': POSITIVE_THRESHOLD},
    'dashboard_check': {'positive': True, 'threshold': POSITIVE_THRESHOLD},
    'off_road_gaze': {'positive': False, 'threshold': NEGATIVE_THRESHOLD},
    'prolonged_check': {'positive': False, 'threshold': NEGATIVE_THRESHOLD},
    'closed_eyes': {'positive': False, 'threshold': 0}
}

def classify_positive_gaze(duration, threshold):
    if threshold is None:
        return 1  # Always positive if no threshold
    elif duration < threshold:
        return 1  # Positive
    elif duration == threshold:
        return 0  # Neutral
    else:
        return -1  # Negative

def classify_negative_gaze(duration, threshold):
    if duration > threshold:
        return -1  # Negative
    elif duration == threshold:
        return -1 if threshold > 0 else 0  # Edge case: 0 seconds for `closed_eyes`
    else:
        return 1  # Positive

def classify_closed_eyes(duration):
    if duration > 0:
        return -1  # Negative
    else:
        return 0  # Neutral if eyes are not closed at all

def calculate_engagement_score(gaze_data):
    score = 0
    for point, durations in gaze_data.items():
        criteria = ENGAGEMENT_CRITERIA.get(point)
        if criteria:
            for duration in durations:
                if point == 'closed_eyes':
                    result = classify_closed_eyes(duration)
                elif criteria['positive']:
                    result = classify_positive_gaze(duration, criteria['threshold'])
                else:
                    result = classify_negative_gaze(duration, criteria['threshold'])
                score += result
                print(f"Point: {point}, Duration: {duration}, Criteria: {criteria}, Result: {result}, Total Score: {score}")
    return score

if __name__ == "__main__":
    # Sample data sets
    sample_gaze_data_1 = {
        'road_focus': [5, 6, 7],
        'mirror_check': [1.5, 2.0],
        'dashboard_check': [1, 1.5],
        'off_road_gaze': [3, 2.5],
        'prolonged_check': [2.5, 3],
        'closed_eyes': [0, 0.5]
    }

    sample_gaze_data_2 = {
        'road_focus': [7, 8, 6],
        'mirror_check': [1.0, 1.5],
        'dashboard_check': [1, 2],
        'off_road_gaze': [1.5, 2],
        'prolonged_check': [1.5, 1.8],
        'closed_eyes': [0, 0]
    }

    sample_gaze_data_3 = {
        'road_focus': [3, 4, 2],
        'mirror_check': [2.0, 2.5],
        'dashboard_check': [2, 2.5],
        'off_road_gaze': [4, 3.5],
        'prolonged_check': [3, 3.2],
        'closed_eyes': [0.5, 1]
    }

    # Calculate and print scores for each data set
    data_sets = [sample_gaze_data_1, sample_gaze_data_2, sample_gaze_data_3]
    
    for i, data in enumerate(data_sets, 1):
        print(f"Testing Sample Data Set {i}:")
        score = calculate_engagement_score(data)
        print(f"Engagement Score for sample data set {i}: {score}\n")
