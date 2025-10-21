#Efficiently chaining coroutines using asyncio.gather
# This example demonstrates how to chain coroutines where one coroutine's
# result is needed for the next coroutine, while still running multiple chains concurrently.

import asyncio
import random
import time

# Chained coroutines: fetching a user and then their posts
async def main():
    user_ids = [1, 2, 3]
    start = time.perf_counter()
    await asyncio.gather(
        *(get_user_with_posts(user_id) for user_id in user_ids)  # Unpacking a generator expression
    )
    end = time.perf_counter()
    print(f"\n==> Total time: {end - start:.2f} seconds")

# Chained coroutines: fetching a user and then their posts
async def get_user_with_posts(user_id):
    user = await fetch_user(user_id)
    await fetch_posts(user)

# Simulated async function to fetch user data
async def fetch_user(user_id):
    delay = random.uniform(0.5, 2.0)
    print(f"User coro: fetching user by {user_id=}...")
    await asyncio.sleep(delay)  # Simulate network delay
    user = {"id": user_id, "name": f"User{user_id}"}
    print(f"User coro: fetched user with {user_id=} (done in {delay:.1f}s).")
    return user

# Simulated async function to fetch posts for a user
async def fetch_posts(user):
    delay = random.uniform(0.5, 2.0)
    print(f"Post coro: retrieving posts for {user['name']}...")
    await asyncio.sleep(delay)
    posts = [f"Post {i} by {user['name']}" for i in range(1, 3)]
    print(
        f"Post coro: got {len(posts)} posts by {user['name']}"
        f" (done in {delay:.1f}s):"
    )
    for post in posts:
        print(f" - {post}")

if __name__ == "__main__":
    asyncio.run(main())