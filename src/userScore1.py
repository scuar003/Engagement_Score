import numpy as np

#Engagement score Criteria
POSITIVE_THRESHOLD = 2
NEGATIVE_THRESHOLD = 2

ENGAGEMENT_CRITERIA = {
    'road_focus': {'positive': True, 'threshold': None},
    'mirror_check': {'positive': True, 'threshold': POSITIVE_THRESHOLD},
    'dashboard_check': {'positive': True, 'threshold': POSITIVE_THRESHOLD},
    'off_road_gaze': {'positive': False, 'threshold': NEGATIVE_THRESHOLD},
    'prolonged_check': {'positive': False, 'threshold': NEGATIVE_THRESHOLD},
    'closed_eyes': {'positive': False, 'threshold': 0}
}

#Basic Scoring function
def classify_gaze_point (gaze_duration, criteria):
    if criteria['positive']:
        return gaze_duration < criteria['threshold'] if criteria['threshold'] else True
    else:
        return gaze_duration > criteria['threshold']
    
def calculate_engagement_score(gaze_data):
    score = 0 
    for point, duration in gaze_data.items():
        criteria = ENGAGEMENT_CRITERIA.get(point)
        if criteria:
            if classify_gaze_point(duration, criteria):
                score +=1 if criteria['positive'] else -1 
    return score


if __name__ == "__main__":
    sample_gaze_data = {
        'road_focus': 5,  # seconds
        'mirror_check': 1.5,  # seconds
        'dashboard_check': 1,  # seconds
        'off_road_gaze': 3,  # seconds
        'prolonged_check': 2.5,  # seconds
        'closed_eyes': 0  # seconds
    }
    score = calculate_engagement_score(sample_gaze_data)
    print(f"Engagement Score: {score}")