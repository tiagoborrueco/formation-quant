def transform(legacy_data):
    new_scoring_scale = dict()
    for score_possible in legacy_data.keys():
        for same_score_letter in legacy_data[score_possible]:
            new_scoring_scale[same_score_letter.lower()] = score_possible
    return new_scoring_scale
