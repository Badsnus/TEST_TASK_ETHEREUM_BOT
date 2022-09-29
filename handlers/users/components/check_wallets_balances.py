import asyncio

from aiohttp import ClientSession
from aiofile import async_open

from data.config import ETHERSCAN_API_KEY


async def do_request(address: str, session: ClientSession()) -> float or None:
    response = await session.get(f"https://api.etherscan.io/api\
?module=account\
&action=balance\
&address={address}\
&tag=latest\
&apikey={ETHERSCAN_API_KEY}")
    if response.status == 200 and (await response.json())['status'] == '1':
        return int((await response.json())['result']) / 10 ** 18
    return None


async def check_wallets_balances(addresses: [str]) -> [(str, float)]:
    async with ClientSession() as session:
        tasks = []
        for address in enumerate(addresses):
            tasks.append(asyncio.create_task(do_request(address[1], session)))
            if address[0] % 4 == 0:
                await asyncio.sleep(1)
        await asyncio.gather(*tasks)
        return [(addresses[i[0]], i[1].result()) for i in enumerate(tasks)]


async def parse_wallets_to_file(balances: [(str, float)], bad_addresses: [int], path_to_file: str) -> None:
    async with async_open(path_to_file, 'w') as afp:
        await afp.write(f"{'_' * 10}GOOD ADDRESSES{'_' * 10}\n")
        for balance in balances:
            await afp.write(f"{'_' * 20}\n"
                            f"Address: {balance[0]}\n"
                            f"Balance: {balance[1]}\n"
                            f"{'_' * 20}\n")
        await afp.write(f"{'_' * 10}INVALID ADDRESSES{'_' * 10}\n")
        for bad_addresses in bad_addresses:
            await afp.write(f"{'_' * 20}\n"
                            f"Address: {bad_addresses}\n"
                            f"{'_' * 20}\n")
