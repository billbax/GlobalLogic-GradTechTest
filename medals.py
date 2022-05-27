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
    # Create a placing to points conversion dict to be referenced when creating the results table giving
    # the winner 3 points, second place 2 points and third place 1 point
    points_conversion_dict = {"1": 3, "2": 2, "3": 1}

    # Create an empty dict that will be used to house the nation and their corresponding cumulative scores
    results_table = {}

    # Iterate through the results list to get the results list for each sport by accessing the 'podium' key
    for sport in results:
        podium_list = sport["podium"]

        for placing_and_nation in podium_list:
            # Split the podium_spot item in the podium_list using the '.' separator to get both the placing and the nation
            placing = (placing_and_nation.split(".")[0])
            nation = (placing_and_nation.split(".")[1])
            # Convert the podium placing to the relevant amount of points to be awarded based on the points_conversion_dict
            points_to_award = points_conversion_dict[placing]

            # Use exception handling, if nation key already exists in results_table += points_to_award to nation
            try:
                results_table[nation] += points_to_award

            # If 'nation' key not in results_table, create a new dict key setting points_to_award as the value
            except KeyError:
                results_table[nation] = points_to_award

    # reverse the order of the keys as expectedTable keys ordered inversely to order of occurrence. As using py dicts,
    # default order will == order of occurrence
    nation_keys = list(results_table.keys())
    reversed_keys = nation_keys[::-1]

    # Re-order the points values in results_table to run highest to lowest
    high_to_low_values = sorted(results_table.values(), reverse=True)

    # Empty dict to populate with ordered table
    sorted_dict = {}

    # Re-order the results dict so the highest scoring nations appear at the top of the table.
    # Iterate through the sorted values, will run highest to lowest so the nations with the most points will be added
    # to the sorted table first
    for value in high_to_low_values:

        # Iterate through the reversed_keys list so the dict keys will be added in expectedTable order
        for dict_key in reversed_keys:

            # For each key in the list, check if its value in the unordered table matches the current for loop value,
            # if the value does match add the key:value to the sorted table
            if results_table[dict_key] == value:
                sorted_dict[dict_key] = results_table[dict_key]

    return sorted_dict


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

test_function()