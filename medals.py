medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]


def createMedalTable(results: list):
    # Create a placing to points conversion dict to be referenced when creating the initial results table giving
    # the winner 3 points, second place 2 points and third place 1 point
    points_conversion_dict = {"1": 3, "2": 2, "3": 1}

    # Create an empty dict to house the nation and the cumulative score
    results_table = {}

    # Iterate through each dict in the results list to get the results of each sport by accessing the 'podium' key
    for sport in results:
        podium_list = sport["podium"]

        for podium_spot in podium_list:
            # Split the results item in the podium_list using the '.' separator to get both the placing and the nation
            placing = (podium_spot.split(".")[0])
            nation = (podium_spot.split(".")[1])
            # Convert the placing to the amount of points
            points_to_award = points_conversion_dict[placing]

            # Exception handling
            # If nation key already in results table += points based on points_to_award
            try:
                results_table[nation] += points_to_award
            # If nation not already in table, create a new dict key for the nation
            except KeyError:
                results_table[nation] = points_to_award
    print(results_table)
    return


def test_function():
    # This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable


createMedalTable(medalResults)
