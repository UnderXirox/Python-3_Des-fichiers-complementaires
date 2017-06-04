#!/usr/bin/python3.4

from itertools import permutations
import asyncio
from time import time


class BoardTester:
    def __init__(self, n):
        self.data = permutations(range(n))

    async def __aiter__(self):
        return self

    async def __anext__(self):
        return await next(self.data)


async def nqueens_async_coroutine(n):
    async for board in BoardTester(n):
        if n == len(set(board[i]+i for i in columns)) \
             == len(set(board[i]-i for i in columns)):
            pass # print(board)
#    await (board for board in permutations(columns)
#                      if n == len(set(board[i]+i for i in columns))
#                           == len(set(board[i]-i for i in columns)))

async def print_nqueen_solutions(n):
    result = await(nqueens_async_coroutine(n))
    print("Résultat trouvé: {}".format(result))

def nqueens_async(n):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_nqueen_solutions(n))
    loop.close()

def nqueens_sync(n):
    columns=range(n)
    for board in permutations(columns):
        if n == len(set(board[i]+i for i in columns)) \
             == len(set(board[i]-i for i in columns)):
            pass # print(board)



if __name__ == '__main__':
    t0=time()
    res=nqueens_sync(9)
    t1=time()
    print('4-Dames en synchrone   : %12.9f secondes' % (t1-t0))
    t0=time()
    res=nqueens_async(9)
    t1=time()
    print('4-Dames en asynchrone  : %12.9f secondes' % (t1-t0))

