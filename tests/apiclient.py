import logging
import requests


class APIClient:
    """
    A simple API client to interact with a REST APIs

    Attributes:
        url (str): The base URL of the API.
    """

    def __init__(self, url):
        """
        Initializes the APIClient with the base URL.

        Args:
            url (str): The base URL of the API.
        """
        self.url = url

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the GET request to.
            params (dict, optional): The query parameters to include in the request.

        Returns:
            response: The response object from the GET request.
        """
        url = f"{self.url}{endpoint}"
        logging.info(f"GET {url}, params={params}")
        response = requests.get(url, params=params)
        logging.debug(f"GET {url}, params={params}, response={response.json()}")
        return response

    def post(self, endpoint, data=None):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the POST request to.
            data (dict, optional): The JSON data to include in the request body.

        Returns:
            response: The response object from the POST request.
        """
        url = f"{self.url}{endpoint}"
        logging.info(f"POST {url}, data={data}")
        response = requests.post(url, json=data)
        logging.info(f"POST {url}, data={data}, response={response.json()}")
        return response

    def put(self, endpoint, data=None):
        """
        Sends a PUT request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the PUT request to.
            data (dict, optional): The JSON data to include in the request body.

        Returns:
            response: The response object from the PUT request.
        """
        url = f"{self.url}{endpoint}"
        logging.info(f"PUT {url}, data={data}")
        response = requests.put(url, json=data)
        logging.info(f"POST {url}, data={data}, response={response.json()}")
        return response

    def delete(self, endpoint):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to send the DELETE request to.

        Returns:
            response: The response object from the DELETE request.
        """
        url = f"{self.url}{endpoint}"
        logging.info(f"DELETE {url}")
        response = requests.delete(url)
        return response
