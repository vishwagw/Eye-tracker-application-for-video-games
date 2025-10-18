def test_accuracy(self):
    test_points = generate_test_grid()
    accuracy_results = []
    
    for target in test_points:
        actual_gaze = self.get_gaze_position()
        error = calculate_distance(target, actual_gaze)
        accuracy_results.append(error)
    
    return np.mean(accuracy_results)