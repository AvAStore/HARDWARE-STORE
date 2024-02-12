import DB
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

class Recommendations(DB.Database):
    def __init__(self, db_name='database.db'):
        super().__init__(db_name)
        self.history = self.__get_order_history()
        self.matrix = self.__create_matrix(self.history)

    # Function to recommend items for a given user based on collaborative filtering
    def get_recommend_items(self,user_purchases_dic: dict, number_of_recommendations: int = 5):
        """
        Parameters :
        - user_purchases_dic : Current user purchased item in dictionary. Format : {ItemCode:(Quantity,SellingPrice,ItemName)}
        - number_of_recommendations : How many recommendations (default = 5) do you want  Eg - if you give 5, function return top five recommendations.

        Return :
        - return predicted recommendations as a list. First item in the list is highest suggestion. Sometimes return list can be empty.
        """
        # convert user_purchases_dic to list of purchase items
        user_purchases = [x[2] for _,x in user_purchases_dic.items()]

        vectorizer = DictVectorizer(sparse=False)
        X = vectorizer.fit_transform(self.matrix)

        user_profile = [0] * len(X[0])  # Initialize user profile
        for item in user_purchases:
            if item in vectorizer.feature_names_:
                item_index = vectorizer.feature_names_.index(item)
                user_profile[item_index] = 1

        similarities = cosine_similarity([user_profile], X)  # Cosine similarity between the user and other users

        recommendations = defaultdict(float)
        for i, similarity in enumerate(similarities[0]):
            for item in list(self.history.values())[i]:
                if item not in user_purchases:
                    recommendations[item] += similarity
        
        final_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in final_recommendations if x[1] > 0][:number_of_recommendations]

    # Function to create a matrix representation of the purchase history
    def __create_matrix(self, history):
        matrix = []
        for customer, purchases in history.items():
            row = {fruit: 1 for fruit in purchases}
            matrix.append(row)
        return matrix
    
    # Function to gets order history from database and return history
    def __get_order_history(self) -> dict:
        self.cursor.execute("""SELECT Orders.InvoiceNumber,Stock.ItemName FROM Orders INNER JOIN Stock ON Orders.ItemCode = Stock.ItemCode""")
        result = self.cursor.fetchall()
        orders_history = {}
        current_key = ""
        for order_data in result:
            if current_key != order_data[0]:
                order_list = []
                order_list.append(order_data[1])
                current_key = order_data[0]
            else:
                order_list.append(order_data[1])
            orders_history.update({order_data[0]:order_list})
        return orders_history