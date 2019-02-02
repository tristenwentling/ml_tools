

class Model:
    """
        General purpose model framework
    """

    def __init__(self, **kwargs):
        """
            Create model attributes using kwargs
        """
        pass

    def data_load(self):
        """
            Data acquisition and load
        """
        pass

    def data_transform(self):
        """
            Type conversions and feature engineering
        """
        pass

    def model_def(self):
        """
            Model definition(s)
        """
        pass

    def model_train(self):
        """
            Training configuration, operation, and outputs
        """
        pass

    def model_test(self):
        """
            Testing configuration, operation, and outputs
        """
        pass

    def model_cache(self):
        """
            Storing weights or serialized model to disk
        """
        pass

    def model_load(self):
        """
            Acquire weights or serialized model from disk
        """
        pass

    def model_predict(self):
        """
            Predict from trained or loaded model
        """
        pass

    def model_deploy(self):
        """
            Deploy as api endpoint
        """
        pass

    def model_vis(self):
        """
            Visualizations for model train, test
        """
        pass

    def model_monitor(self):
        """
            Pass information to model monitoring
        """
        pass

    def run(self):
        """
            Wrap methods into run group for simpler operation
        """
        pass

if __name__ == "__main__":
    params = {None: None}
    model = Model(params)
    model.run()
