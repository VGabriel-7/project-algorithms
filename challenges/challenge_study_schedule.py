def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for period in permanence_period:
            if target_time >= period[0] and target_time <= period[1]:
                counter += 1

        return counter
    except TypeError:
        return None
