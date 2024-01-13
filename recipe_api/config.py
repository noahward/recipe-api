from pathlib import Path

from omegaconf import OmegaConf

base_dir = Path(__file__).resolve().parent.parent
yaml_config_path = (base_dir).joinpath("config.yaml")
yaml_local_config_path = (base_dir).joinpath("config.local.yaml")

config = OmegaConf.load(yaml_config_path)

if yaml_local_config_path.exists():
    local_config = OmegaConf.load(yaml_local_config_path)
    config = OmegaConf.merge(config, local_config)
