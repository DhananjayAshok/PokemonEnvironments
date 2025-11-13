from poke_env import BasicPokemonRedEmulator
import click


@click.command()
@click.option("--init_state", type=str, default=None, help="Path to the initial .state file")
def main(init_state):
    env = BasicPokemonRedEmulator(parameters=None, headless=False, init_state=init_state)
    env._human_step_play()

if __name__ == "__main__":
    main()