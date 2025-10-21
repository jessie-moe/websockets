import asyncio
import random

#ANSI color codes
COLORS = (
    "\033[0m", # End of color
    "\033[36m", # Cyan
    "\033[91m", # Red
    "\033[35m", # Magenta
)

# Main asynchronous function to run multiple makerrandom tasks or coroutines
async def main():
    return await asyncio.gather(
        makerrandom(1,9),
        makerrandom(2, 8),
        makerrandom(3, 8),
    )

# Asynchronous function to generate random numbers with retries
async def makerrandom(delay, threshold=6):
    color = COLORS[delay]
    print(f"{color}Initiating makerrandom({delay}),")
    while (number := random.randint(0, 10)) <= threshold:
        print(f"{color}makerrandom({delay}) generated {number}, retrying...")
        await asyncio.sleep(delay)
    print(f"{color}---> Finished: makerrandom({delay}) == {number}" + COLORS[0])
    return number
    
if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())     # r1, r2, r3 are results from makerrandom calls
    print(f"Results: {r1}, {r2}, {r3}")