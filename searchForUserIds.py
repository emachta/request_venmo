import client

# Search for users. You get 50 results per page.
users = client.venmo.user.search_for_users(query="test")
for user in users:
    print(user.username)
