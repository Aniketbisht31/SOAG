def analyze_problem(description: str):
    description = description.lower()

    problem_type = None
    constraints = []

    if "search" in description:
        problem_type = "search"

    if "sort" in description:
        problem_type = "sorting"

    if "sorted" in description:
        constraints.append("sorted")

    return {
        "problem_type": problem_type,
        "constraints": constraints
    }

