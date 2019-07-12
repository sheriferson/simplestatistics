"""
Implements bayesian_classifier().
"""

class bayesian_classifier():
    """
    A `naive Bayesian classifier`_.

    The implemention of this classifier is very closely modeled after the implementation
    in `simple-statistics <https://github.com/simple-statistics/simple-statistics>`_,
    the javascript analogue of ``simplestatistics``. You can find the javascript implementation
    of the Bayesian classifier `here <https://github.com/simple-statistics/\
    simple-statistics/blob/master/src/bayesian_classifier.js>`_.

    .. _`naive Bayesian classifier`: https://en.wikipedia.org/wiki/Naive_Bayes_classifier

    Examples:
        Making a seventy-five/twenty-five classification.

        >>> model1 = bayesian_classifier()
        >>> model1.train({'species': 'cat'}, 'animal')
        >>> model1.train({'species': 'cat'}, 'animal')
        >>> model1.train({'species': 'cat'}, 'animal')
        >>> model1.train({'species': 'cat'}, 'feline')
        >>> model1.count
        4
        >>> model1.score({'species': 'cat'})
        [('animal', 0.75), ('feline', 0.25)]

        Classifying multiple things

        >>> model2 = bayesian_classifier()
        >>> model2.train({'species': 'cat'}, 'animal')
        >>> model2.train({'species': 'dog'}, 'animal')
        >>> model2.train({'species': 'dog'}, 'animal')
        >>> model2.train({'species': 'cat'}, 'chair')
        >>> model2.score({'species': 'cat'})
        [('animal', 0.25), ('chair', 0.25)]
        >>> model2.score({'species': 'dog'})
        [('animal', 0.5), ('chair', 0)]

        Testing multiple properties

        >>> model3 = bayesian_classifier()
        >>> model3.train({'species': 'cat'}, 'animal')
        >>> model3.train({'species': 'cat'}, 'animal')
        >>> model3.train({'species': 'cat'}, 'animal')
        >>> model3.train({'species': 'cat'}, 'chair')
        >>> model3.train({'species': 'cat', 'color': 'white'}, 'chair')
        >>> model3.score({'color': 'white'})
        [('chair', 0.2), ('animal', 0)]

        >>> mod = bayesian_classifier()
        >>> mod.score({'color': 'purple'}) # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        RuntimeError: The model has not been trained yet. Train the model ... item.
    """

    def __init__(self):
        # number of items the model trained on
        self.count = 0
        # storage for all property and category keys and values
        self.store = {}

    def train(self, item, category):
        """
        The method to train the instance of the Bayesian classifier
        on an item.

        Args:
            item: A dict of property-value pairs in the form {property_1: value1,
            property2: value2, . . .} for the item.  category: A string of the
            category of the item.

        Returns:
            null
        """

        # if the data store doesn't contain this category,
        # create a new key with the value being an empty
        # dictionary
        if category not in self.store:
            self.store[category] = {}

        # iterate through key/property-value pairs in item
        for item_key in item:
            item_value = item[item_key]

            # if it's the first time the model sees this property for this category,
            # add a dictionary for it
            if item_key not in self.store[category]:
                self.store[category][item_key] = {}

            # if this is the first time the model sees a value for this property + category,
            # add an entry in the dict for that property and set value to 0
            if item_value not in self.store[category][item_key]:
                self.store[category][item_key][item_value] = 0

            # increment the value tied to the property + category
            self.store[category][item_key][item_value] += 1

        # increment count of trained items
        self.count += 1

    def score(self, item):
        """
        Scores a certain item based on the learning the model has done
        on previous items.

        Args:
            item: A dict in the form {property: value} of the item you want to score.

        Returns:
            A list containing tuples of properties and scores. The list is ordered
            in descending order of scores.
        """

        if self.store == {}:
            raise RuntimeError('The model has not been trained yet. Train the '
                               'model before trying to score an item.')

        # iterate through each key in the item to be scored
        # and then iterate through each category used in previous
        # .train() calls

        odds = {}
        odds_sums = {}

        # iterate over properties and their values in the item to score
        for item_key in item:
            # item_key is the property (e.g., color), item_value is value of property (e.g., white)
            item_value = item[item_key]

            # iterate over all categories that the model has trained on in the past
            for category in self.store:
                # if we haven't added this category to our odds dict, add it with a dict as value
                if category not in odds:
                    odds[category] = {}

                if item_key in self.store[category]:
                    # if the model has seen this value for this property for this category before
                    # return the number of times divided by total training trials
                    # we get a score for each unique property+value combination within a category
                    if item_value in self.store[category][item_key]:
                        odds[category][item_key + '_' + item_value] = \
                                self.store[category][item_key][item_value] / self.count

                    # otherwise, mark it zero.
                    else:
                        odds[category][item_key + '_' + item_value] = 0
                # MARK IT ZERO.
                else:
                    odds[category][item_key + '_' + item_value] = 0

        # iterate over all categories in odds dict and sum up prob values
        # for unique property+value combinations
        for category in odds:
            for combination in odds[category]:
                if combination not in odds_sums:
                    odds_sums[category] = 0

                odds_sums[category] += odds[category][combination]

        # return a list of properties and scores in descending order of scores
        return(sorted(odds_sums.items(), key=lambda x: x[1], reverse=True))
