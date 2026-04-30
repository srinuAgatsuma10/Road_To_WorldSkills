import requests

BaseURL = "https://jsonplaceholder.typicode.com/"

# HTTP Call 1
callOne_Response = requests.get(f"{BaseURL}posts/1")
assert callOne_Response.status_code == 200, f"Expected 200 got {callOne_Response.status_code}"
body1 = callOne_Response.json()
print(f"[1] status={callOne_Response.status_code}  userId={body1['userId']}")

# HTTP Call 2
callTwo_Response = requests.post(
    f"{BaseURL}posts",
    json={"title": "Test post", "body": "Content here", "userId": 1}
)
assert callTwo_Response.status_code == 201, f"Expected 201 got {callTwo_Response.status_code}"
body_payload = callTwo_Response.json()
print(f"[2] status={callTwo_Response.status_code}  id={body_payload['id']}")

# HTTP Call 3
callThree_Response = requests.get(f"{BaseURL}posts/9999")
assert callThree_Response.status_code == 404, f"Expected 404 got {callThree_Response.status_code}"
body3 = callThree_Response.json()
print(f"[3] status={callThree_Response.status_code}  body={body3}")