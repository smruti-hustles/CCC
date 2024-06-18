def analyze_signal_strength(signal_strengths, threshold):
    if not signal_strengths:
        return {
            "average": 0,
            "max_strength": 0,
            "min_strength": 0,
            "exceeds_threshold_indices": []
        }
    
    total_strength = sum(signal_strengths)
    average_strength = total_strength / len(signal_strengths)
    max_strength = max(signal_strengths)
    min_strength = min(signal_strengths)
    
    exceeds_threshold_indices = [index for index, strength in enumerate(signal_strengths) if strength > threshold]
    
    return {
        "average": average_strength,
        "max_strength": max_strength,
        "min_strength": min_strength,
        "exceeds_threshold_indices": exceeds_threshold_indices
    }

# Example usage
signal_strengths = [45, 50, 55, 40, 65, 70, 60, 50]
threshold = 60
result = analyze_signal_strength(signal_strengths, threshold)

print("Average Signal Strength:", result["average"])
print("Maximum Signal Strength:", result["max_strength"])
print("Minimum Signal Strength:", result["min_strength"])
print("Indices where Signal Strength exceeds threshold:", result["exceeds_threshold_indices"])
