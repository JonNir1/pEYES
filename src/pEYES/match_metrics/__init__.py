from src.pEYES._DataModels.EventMatcher import OneToOneEventMatchesType

from src.pEYES.match_metrics.get_features import get_features as features
from src.pEYES.match_metrics.match_evaluation import match_ratio, precision_recall_f1, d_prime


def onset_difference(matches: OneToOneEventMatchesType):
    return features(matches, 'onset', verbose=False)


def offset_difference(matches: OneToOneEventMatchesType):
    return features(matches, 'offset', verbose=False)


def duration_difference(matches: OneToOneEventMatchesType):
    return features(matches, 'duration', verbose=False)


def amplitude_difference(matches: OneToOneEventMatchesType):
    return features(matches, 'amplitude', verbose=False)


def azimuth_difference(matches: OneToOneEventMatchesType):
    return features(matches, 'azimuth', verbose=False)


def center_pixel_distance(matches: OneToOneEventMatchesType):
    return features(matches, 'center_pixel_distance', verbose=False)


def time_overlap(matches: OneToOneEventMatchesType):
    return features(matches, 'time_overlap', verbose=False)


def time_iou(matches: OneToOneEventMatchesType):
    return features(matches, 'time_iou', verbose=False)


def time_l2(matches: OneToOneEventMatchesType):
    return features(matches, 'time_l2', verbose=False)
