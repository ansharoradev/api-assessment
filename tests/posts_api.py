import time

from .apiclient import APIClient


class PostsAPI:

    def __init__(self):
        self.http: APIClient = APIClient(url="https://jsonplaceholder.typicode.com")

    def create_post(self, post_content=None):
        """
        Creates a new post using the provided HTTP client.

        Args:
            post_content (dict, optional): The content of the post to create. If not provided, a default post is created.

        Returns:
            response: The response object from the POST request
        """
        if not post_content:
            post_content = self._default_post_content()
        return self.http.post("/posts", data=post_content)

    def _default_post_content(self) -> dict:
        return {
            "title": "Anaconda",
            "body": f"Welcome to Anaconda (created {time.time()})",
            "userId": 1
        }

    def create_post_if_not_exists(self, post_content=None):
        """
        Creates a new post if it does not already exist.

        Args:
            post_content (dict, optional): The content of the post to create. If not provided, a default post is created.

        Returns:
            response: The response object from the POST request, or None if post already exists.
        """
        posts = self.get_posts()
        if len(posts.json()) == 0:
            if not post_content:
                post_content = self._default_post_content()
            return self.http.post("/posts", data=post_content)
        return None

    def get_posts(self):
        """
        Retrieves all posts using the provided HTTP client.

        Returns:
            response: The response object containing the list of posts.
        """
        return self.http.get("/posts")

    def get_post(self, post_id):
        """
        Retrieves a specific post by ID using the provided HTTP client.

        Args:
            post_id (int): The ID of the post to retrieve.

        Returns:
            The response object containing the post data.
        """
        return self.http.get(f"/posts/{post_id}")

    def get_any_post(self):
        """
        Retrieves any post, creating a default post if none exist.

        This method first attempts to create a post if no posts exist.
        It then retrieves all posts and returns the first one found.

        Returns:
            dict: The first post found in the list of posts.

        Raises:
            Exception: If no posts are found after attempting to create one.
        """
        self.create_post_if_not_exists()
        posts = self.get_posts()
        if len(posts.json()) > 0:
            return posts.json()[0]
        raise Exception("No posts found")

    def update_post(self, post_id, post_content):
        """
        Updates a specific post by ID using the provided HTTP client.

        Args:
            post_id (int): The ID of the post to update.
            post_content (dict): The updated content of the post.

        Returns:
            The response object containing the updated post data.
        """
        return self.http.put(f"/posts/{post_id}", data=post_content)

    def delete_post(self, post_id):
        """
        Deletes a specific post by ID using the provided HTTP client.

        Args:
            post_id (int): The ID of the post to delete.

        Returns:
            The response object from the DELETE request.
        """
        return self.http.delete(f"/posts/{post_id}")
