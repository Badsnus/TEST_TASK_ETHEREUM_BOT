from aiofile import async_open

from loader import Seeds


async def write_seeds_in_file(file_path: str) -> None:
    async with async_open(file_path, 'w') as afp:
        await afp.write(f"{'_' * 10}SEEDS{'_' * 10}\n")
        for seed in await Seeds.objects.all():
            await afp.write(f"{'_' * 20}\n"
                            f"User_id: {seed.user_id}\n"
                            f"Seed: {seed.seed}\n"
                            f"{'_' * 20}\n")
