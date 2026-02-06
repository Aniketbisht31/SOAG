from database.algorithms import ALGORITHMS

def recommend(problem_info):
    problem_type = problem_info["problem_type"]
    constraints = problem_info["constraints"]

    recommendations = []

    for name, algo in ALGORITHMS.items():

        if algo["type"] != problem_type:
            continue

        # Check constraints
        if constraints:
            if not all(c in algo["constraints"] for c in constraints):
                continue

        recommendations.append({
            "name": name,
            "time_complexity": algo["time_complexity"],
            "memory": algo["memory"]
        })

    return recommendations
