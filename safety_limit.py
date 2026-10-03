def agent():
    max_iters = 10

    for i in range(max_iters):
        print(f"Iteration: {i + 1}")

        # Observe
        observation = "check environment"

        # Decide
        decision = "continue"

        # Act
        print("Action:", decision)

        # Example success condition
        if decision == "success":
            return "success"

    # Safety limit exceeded
    return "failure"


result = agent()
print("Result:", result)
