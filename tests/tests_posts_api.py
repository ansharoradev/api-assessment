import json
import os
import pytest

from .posts_api import PostsAPI


api = PostsAPI()


# test data used in `test_create_post`
# loads test data from data file in ./data/basic_tests.json
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{dir_path}/data/basic_tests.json", "r") as f:
    data = json.load(f)

# marking test with `pytest.mark.order` to ensure one or more posts exist before running all other tests
@pytest.mark.parametrize("post_content", data["test_create_post"])
def test_create_post(post_content):
    response = api.create_post(post_content)
    assert response.status_code == 201
    for e in post_content:
        assert response.json()[e] == post_content[e]


def test_get_post_by_id():
    post_id = api.get_any_post()["id"]
    response = api.get_post(post_id)
    assert response.status_code == 200


def test_get_nonexistent_post():
    response = api.get_post(9999)  # Assuming 9999 is a non-existent post ID
    assert response.status_code == 404, "Request should fail as the post does not exist"
    assert "error" in response.json(), "Response should contain an error message"
    assert response.json()["error"] == "post not found"


def test_create_post_with_missing_title():
    post_content = {
        "body": "bar",
        "userId": 1
    }
    response = api.create_post(post_content)
    assert response.status_code == 400, "Request should fail due to missing title"
    assert response.json()["error"] == "title is required"


def test_create_post_with_empty_body():
    post_content = {
        "title": "foo",
        "body": "",
        "userId": 1
    }
    response = api.create_post(post_content)
    assert response.status_code == 400, "Request should fail due to empty body"
    assert "error" in response.json(), "Response should contain an error message"
    assert response.json()["error"] == "body is required"


def test_create_post_with_long_title_truncation():
    # setting a hypothetical max length for title
    max_len = 40
    post_content = {
        "title": "This is an example of a very long title that will be truncated",
        "body": "bar",
        "userId": 1
    }
    response = api.create_post(post_content)
    assert response.status_code == 400, "Request should fail due to longer than permitted title"
    assert "error" in response.json(), "Response should contain an error message"
    assert response.json()["error"] == f"titles longer than {max_len} characters are not supported"


def test_update_post_body():
    response =  api.get_any_post()
    updated_post = {
        "title": response["title"],
        "body": response["body"] + " updated",
        "userId": response["userId"]
    }
    response = api.update_post(response["id"], updated_post)
    assert response.status_code == 200
    for e in ["title", "body", "userId"]:
        assert response.json()[e] == updated_post[e]


def test_delete_post():
    post =  api.get_any_post()
    response = api.delete_post(post["id"])
    assert response.status_code == 200

    # Check if the post is actually deleted
    get_response = api.get_post(post["id"])
    assert get_response.status_code == 404, "Post should be deleted and not found"


def test_delete_nonexistent_post():
    response = api.delete_post(9999)  # Assuming 9999 is a non-existent post ID
    assert response.status_code == 404, "Request should fail as the post does not exist"
    assert "error" in response.json(), "Response should contain an error message"
    assert response.json()["error"] == "post not found"
