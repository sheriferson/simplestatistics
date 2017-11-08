"""
Implements perceptron().
"""

class perceptron():
    """
    A `perceptron model`_.

    The implementation of the perceptron model is closely modeled after
    the implementation in `simple-statistics <https://github.com/simple-statistics/\
            simple-statistics>`_, the javascript analogue of ``simplestatistics``. You can
    find the javascript implementation of the perceptron model
    `here <https://github.com/simple-statistics/simple-statistics/blob/master/src/perceptron.js>`_.

    .. _`perceptron model`: https://en.wikipedia.org/wiki/Perceptron

    Examples:
        >>> mod = perceptron()
        >>> for ii in range(10):
        ...     mod.train([0,1], 0)
        ...     mod.train([1,0], 0)
        ...     mod.train([1,1], 1)
        ...     mod.train([0,0], 0)
        >>> mod.predict([1, 0])
        0
        >>> mod.predict([1, 1])
        1

        You cannot predict an item with a model that hasn't been trained yet.

        >>> mod2 = perceptron()
        >>> mod2.predict([0, 0])
        Traceback (most recent call last):
            ...
        RuntimeError: The model has not been trained yet.

        When training, labels need to be 0 or 1.

        >>> mod3 = perceptron()
        >>> mod3.train([1, 1], 4)
        Traceback (most recent call last):
            ...
        ValueError: Labels need to be either 0 or 1.

        Once trained on an item, the rest of the training items need to have
        features of the same length.

        >>> mod4 = perceptron()
        >>> mod4.train([1, 0], 1)
        >>> mod4.train([1, 1], 1)
        >>> mod4.train([1, 1, 0], 1) # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        ValueError: The length of features is different ... to use new feature lengths.
    """

    def __init__(self):
        # The weights are the coefficiencts of the model
        # and get updated during training  when the model's
        # prediction is different from the label/correct category
        self.weights = []

        # The bias, or intercept
        self.bias = 0

    def predict(self, features):
        """
        Classifies an item based on the learning the instance of the model has
        done on previous items.

        Args:
            features: A list of the features of the item to classify. The length
            of the list has to be the same as that of the lists of features the
            model trained on.

        Returns:
            0 or 1 denoting the predicted category/classification.
        """
        # if the model hasn't been trained before
        # return an error
        if len(self.weights) == 0:
            raise RuntimeError('The model has not been trained yet.')

        # initialize prediction score as 0
        score = 0

        # the score is the sum of the product of each feature
        # with the corresponding weight
        # then add the bias
        for ii, _ in enumerate(features):
            score += features[ii] * self.weights[ii]

        score += self.bias

        if score > 0:
            return(1)

        # else
        return(0)

    def train(self, features, label):
        """
        The method to train an instance of the perceptron model on an item.

        Args:
            features: A list of numerical features in the form [feature_1,
            feature_2, ...]. The length of the list needs to be the same for each
            item given to the same model/instance.  label: An integer of value 0
            or 1 to denote category of the item.

        Returns:
            null
        """

        # we will require labels to either be 0 or 1
        if label not in [0, 1]:
            raise ValueError('Labels need to be either 0 or 1.')

        # if this is the first set of features the model trains on
        # set the weights to the features, and the bias to 1
        if len(self.weights) == 0:
            self.weights = features
            self.bias = 1

        elif len(self.weights) != len(features):
            raise ValueError('The length of features is different than previous '
                             'features. Reinitialize your model if you want to use '
                             'new feature lengths.')

        # Make a prediction with current weights
        prediction = self.predict(features)

        if prediction != label:
            gradient = label - prediction

            for ii in range(len(self.weights)):
                self.weights[ii] += gradient * features[ii]

            self.bias += gradient
