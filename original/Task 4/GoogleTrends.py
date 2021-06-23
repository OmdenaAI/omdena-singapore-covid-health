from pytrends.request import TrendReq

class PyTrends():
    def __init__(self, value):
        self.name = value

    def pyt(self):

        # if string was passed in, convert to singleton list
        if isinstance(self.name, str):
            kwrd = [self.name]
        else:
            kwrd = self.name

        # pytrends documentation is here https://github.com/GeneralMills/pytrends
        # initialize trend request with 
        # host language for accessing Google Trends "en-CU"
        # and time zone offset 360
        pytrends = TrendReq(hl='en-CU', tz=360)
        pytrends.build_payload(kwrd, cat=0, timeframe='today 5-y', geo='', gprop='')
        df = pytrends.interest_over_time()
        print(df)
        #data = df.to_dict()
        return df


if __name__ == "__main__":
    # example usage of this class
    # note that it takes in a list of queries to search for
    recession_loader = PyTrends("Recession")
    recession_df = recession_loader.pyt()

    # example do stuff with recession dataframe
    print("="*80)
    print("top 5 days by search index:")
    print(recession_df["Recession"].nlargest(5))
