import matplotlib.pyplot as plt
from random_robot import RandomRobot
from optimised_robot import OptimisedRobot
from empty_room import EmptyRoom
from furnished_room import FurnishedRoom


# simulation function
def run_simulation(room_type, robot_type, num_trials=10, max_steps=100, width=5, height=5):
    """
    Run a simulation of the given robot in either an empty or furnished room.
    """
    all_results = []

    for trial in range(num_trials):
        # To create room
        if room_type.__name__ == "EmptyRoom":
            room = room_type(width=width, height=height, dirt_amount=10)
        elif room_type.__name__ == "FurnishedRoom":
            room = room_type(width=width, height=height, furniture=[(2, 2), (3, 3)], dirt_amount=10)
        else:
            raise ValueError("Invalid room type")

        # To position robot
        robot = robot_type(room)

        steps = 0
        collisions = 0
        path = [(robot.x, robot.y)]
        coverage_history = [room.get_num_cleaned_tiles() / room.get_num_tiles()]

        while steps < max_steps and not room.is_clean():
            prev_pos = (robot.x, robot.y)
            robot.move()
            if (robot.x, robot.y) == prev_pos:
                collisions += 1

            steps += 1
            path.append((robot.x, robot.y))
            coverage_history.append(room.get_num_cleaned_tiles() / room.get_num_tiles())

        coverage = room.get_num_cleaned_tiles() / room.get_num_tiles()

        all_results.append({
            "room": room_type.__name__,
            "robot": robot_type.__name__,
            "steps": steps,
            "collisions": collisions,
            "coverage": coverage,
            "path": path,
            "coverage_history": coverage_history
        })

    # To return averages + one example path
    avg_result = {
        "room": room_type.__name__,
        "robot": robot_type.__name__,
        "avg_steps": sum(r["steps"] for r in all_results) / num_trials,
        "avg_collisions": sum(r["collisions"] for r in all_results) / num_trials,
        "avg_coverage": sum(r["coverage"] for r in all_results) / num_trials,
        "path": all_results[0]["path"],
        "coverage_history": all_results[0]["coverage_history"]
    }
    return avg_result


# Visualization
def plot_path(results, width, height):
    plt.figure(figsize=(5, 5))
    x, y = zip(*results["path"])
    plt.plot(x, y, marker="o", markersize=2, linewidth=1, label=results["robot"])
    plt.title(f"Path in {results['room']} with {results['robot']}")
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.legend()
    plt.show()


def plot_coverage(results_list):
    plt.figure(figsize=(7, 5))
    for res in results_list:
        plt.plot(res["coverage_history"], label=f"{res['robot']} in {res['room']}")
    plt.title("Coverage Over Time")
    plt.xlabel("Steps")
    plt.ylabel("Coverage")
    plt.legend()
    plt.show()


def plot_comparison(results):
    robots = [f"{r['robot']} ({r['room']})" for r in results]
    coverage = [r["avg_coverage"] * 100 for r in results]
    steps = [r["avg_steps"] for r in results]
    collisions = [r["avg_collisions"] for r in results]

    x = range(len(results))

    plt.figure(figsize=(10, 6))
    plt.bar(x, coverage, width=0.25, label="Coverage (%)", align="edge")
    plt.bar([i + 0.25 for i in x], steps, width=0.25, label="Steps", align="edge")
    plt.bar([i + 0.50 for i in x], collisions, width=0.25, label="Collisions", align="edge")

    plt.xticks([i + 0.25 for i in x], robots, rotation=45, ha="right")
    plt.title("Comparative Performance of Random vs Optimised Robots")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.show()


# Summary report
def print_summary(results):
    print("\n--- Simulation Summary Report ---")
    print(f"{'Robot':<15}{'Room':<15}{'Steps':<10}{'Coverage %':<12}{'Collisions':<10}")
    print("-" * 65)
    for res in results:
        print(f"{res['robot']:<15}{res['room']:<15}"
              f"{res['avg_steps']:<10.1f}{res['avg_coverage'] * 100:<12.1f}{res['avg_collisions']:<10.1f}")
    print("\nRecommendation: Wakabot should adopt the strategy with higher coverage and fewer collisions.")


# Main function
def main():
    width, height = 5, 5
    max_steps = 200
    num_trials = 10

    results = []
    for room_class in [EmptyRoom, FurnishedRoom]:
        for robot_class in [RandomRobot, OptimisedRobot]:
            sim_result = run_simulation(
                room_class, robot_class,
                num_trials=num_trials,
                max_steps=max_steps,
                width=width, height=height
            )
            results.append(sim_result)
            plot_path(sim_result, width, height)  

    plot_coverage(results)     
    plot_comparison(results)   
    print_summary(results)    


if __name__ == "__main__":
    main()
