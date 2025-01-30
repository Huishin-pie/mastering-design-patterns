from world.world import World
from collision.hero_fire import HeroFire
from collision.hero_water import HeroWater
from collision.water_fire import WaterFire
from collision.same_type import SameType

def main():
    try:
        world = World(SameType(WaterFire(HeroFire(HeroWater(None)))))
        world.start()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()