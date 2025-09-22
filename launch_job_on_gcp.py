from configs.config import setup_config
from omegaconf import DictConfig
import hydra

setup_config()


@hydra.main(config_path=".", config_name="config", version_base=None)
def run(config: DictConfig) -> None:
    pass

if __name__ == "__main__":
    run()
